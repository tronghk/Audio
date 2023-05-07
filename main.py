import sys
import random
import threading as th 
import pygame
import time  
import ffmpeg
# import main_list_music
from threading import Timer  
from tkinter import messagebox
from tkinter import filedialog
import tkinter
import os
# from timer import timer
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtMultimedia import QMediaPlayer,QMediaContent
# from PyQt5.QtMultimediaWidgets import QVideoWidget
# from PyQt5.QtCore import QUrl
from ui.nhac import Ui_MainWindow
# from main_list_music import Main_List_Music_MainWindow as MainWindowListMusic
# from main_list_music import Main_List_Music_MainWindow
from object.music import *
from unity.volume import *
from dao.SongDAO import *
from controller.MusicController import *
from unity.main_list_music import *
class RepeatTimer(Timer):  
    def run(self):  
        while not self.finished.wait(self.interval):  
            self.function(*self.args,**self.kwargs)  
    
class MainWindow(QMainWindow):
    
    
    list = []
    
    songDao = SongDao()
    controller = MusicController()
    __playMusic=False
    index = 0
    timer = ""
    callBackMusic = False
    ran = False
    volumn = True
    valueVolumn = 50
    valueVolumnOld = 50
    cellSelect = -1
    currentTime = 0
    listTemp = []

   
    def __init__(self):
        super().__init__()
        self.uic= Ui_MainWindow()
        pygame.init()
        self.uic.setupUi(self)
        self.uic.phat.clicked.connect(self.show_music)
        self.uic.dung_lai.clicked.connect(self.stopMusic)
        self.uic.tam_dung.clicked.connect(self.pause_music)
        self.uic.lui_bai.clicked.connect(self.prevMusic)
        self.uic.lap_lai.clicked.connect(self.callBackMus)
        self.uic.chuyen_bai.clicked.connect(self.nextMusic)
        self.uic.ngau_nhien.clicked.connect(self.randomMusic)
        self.uic.loa_active.clicked.connect(self.setVolumn)
        self.uic.table_list.cellClicked.connect(self.setCellClick)
        self.uic.tim_kiem.textChanged.connect(self.searchText)
        self.uic.volume.setValue(self.valueVolumn)
        self.uic.volume.valueChanged.connect(self.setValueVolumn)
        self.list = self.songDao.SelectList()
        self.listTemp = self.createListTeam()
        self.timer = RepeatTimer(1,self.display) 
        self.uic.pushButton.clicked.connect(self.addMusicToFile)
        self.selectListType()
        self.uic.select.currentTextChanged.connect(self.on_combobox_changed)
        self.uic.thu_vien.clicked.connect(self.show_list_music)
        self.uic.noi_dung_mp3.setMinimum(0)
        self.uic.noi_dung_mp3.setMaximum(300)
        self.uic.noi_dung_mp3.setValue(0)
        self.add_guest()
        # #QMediaPlayer
        # self.mediaPlayer = QMediaPlayer(None,QMediaPlayer.VideoSurface)
        # self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile('kk.mp3')))

        # #set Widget
        # self.videoWidget=QVideoWidget()
        # self.uic.verticalLayout.addWidget(self.videoWidget)
        # self.mediaPlayer.setVideoOutput(self.videoWidget)
        self.uic.noi_dung_mp3.valueChanged.connect(self.setCurrentTime)
    def createListTeam(self):
        result = []
        for value in self.list:
            result.append(value)
        return result
    def setCellClick(self,row,col):
        self.index = self.findIndexSong(row)
        self.playMusic()
        self.restartTimer()
        
    #thêm bài hát từ file
    def addMusicToFile(self):    
        root =  tkinter.Tk()
        root.withdraw() #use to hide tkinter window 
        currdir = "/"
        root.sourceFile = filedialog.askopenfilename(parent=root, initialdir= currdir, title='Please select a directory')
        if len(root.sourceFile) > 0:
            link = root.sourceFile
            name = os.path.basename(root.sourceFile)
            name = name[:-4]
            self.controller.addMusic(link,name)
            self.list = self.controller.listSong()
            self.listTemp = self.createListTeam()
            self.add_guest()
        
    #chuyên trang
    def show_list_music(self):
        from unity.main_list_music import Main_List_Music_MainWindow
        self.timer.cancel()
        # Khởi tạo QStackedWidget
        self.stacked_widget = QStackedWidget(self)
        
        # Tạo hai trang con cho QStackedWidget
        self.main_widget = MainWindow()
        # self.main_widget.setObjectName("MainWidget")
        # self.main_widget.setStyleSheet("#MainWidget { background-color: #000; }")
        self.thu_vien = QPushButton("Hãy click tôi để chuyển vào thư viện nhé !!!", self.main_widget)
        self.thu_vien.setGeometry(50, 50, 250, 50)
        
        
        self.list_music_widget = Main_List_Music_MainWindow()
        self.list_music_widget.index = self.index
        self.list_music_widget.currentTime = self.currentTime
        self.list_music_widget.volumn = self.uic.volume.value() 
        self.stacked_widget.addWidget(self.main_widget)
        self.stacked_widget.addWidget(self.list_music_widget)
        
        self.setCentralWidget(self.stacked_widget)
        self.stacked_widget.setCurrentWidget(self.list_music_widget)  
    #tìm kiếm
    def searchText(self):
        text = self.uic.tim_kiem.text()
        self.listTemp = self.controller.searchText(text)
        self.uic.table_list.clear()
        self.add_guest()
    #tua nhạc
    def setCurrentTime(self):
        value = int(self.uic.noi_dung_mp3.value())
        if value > int(self.currentTime) or value < int(self.currentTime):
            if self.currentTime != 0 :
                if self.__playMusic != False:
                    pygame.mixer.music.play(0,value)
                    self.uic.noi_dung_mp3.setValue(value)
                    self.currentTime = value
                    self.restartTimer()

    # đưa danh sách loại nhạc
    def selectListType(self):
        listType = self.controller.listTypeDao()
        self.uic.select.addItem("Tất cả")
        for value in listType:
            self.uic.select.addItem(value.name)
    def on_combobox_changed(self,value):
        
        self.listTemp.clear()
       
        if value != "Tất cả":
            self.listTemp = self.controller.searchListSongType(value)
        else:
            self.listTemp = self.createListTeam()
        self.uic.table_list.clear()
        
        self.add_guest()
        
        
    #bảng danh sách
    def add_guest(self):
        rowPosition = self.uic.table_list.rowCount()
        #chọn full
        self.uic.table_list.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.uic.table_list.insertRow(rowPosition)
        label = [
                 "Tên bài hát",
                "Thể loại",
                "Ca sĩ"
                 ]
        numcols = 3
        numrows = len(self.listTemp)      
        self.uic.table_list.setRowCount(numrows)
        self.uic.table_list.setColumnCount(numcols)  
        self.uic.table_list.setHorizontalHeaderLabels(label)
        header = self.uic.table_list.horizontalHeader()       
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        

        index = 0
        for value in self.listTemp:
            name = value.name
            type = self.controller.searchTypeId(value.idType)
            singer = self.controller.searchSingerId(value.idSinger)
            self.uic.table_list.setItem(index,0,QtWidgets.QTableWidgetItem(name))
            self.uic.table_list.setItem(index,1, QtWidgets.QTableWidgetItem(str(type)))
            self.uic.table_list.setItem(index,2,QtWidgets.QTableWidgetItem(str(singer)))
            index = index+1
       
    #thời gian thực
    def duration(self, song):
        return int(float((ffmpeg.probe(song)['format']['duration'])))
    # giá trị âm lượng
    def setValueVolumn(self):
        self.valueVolumn = self.uic.volume.value()
        set_master_volume(self.valueVolumn)
    #âm lượng 
    def setVolumn(self):
        if self.volumn == True:
            self.valueVolumnOld = self.valueVolumn
            self.uic.volume.setValue(0)
            self.volumn = False
        else:
            self.volumn = True
            self.uic.volume.setValue(self.valueVolumnOld)
    #bật tắt ngẫu nhiên
    def randomMusic(self):
        if(self.ran == False):
            self.ran = True
        else:
             self.ran = False
    #bật tắt lập lại
    def callBackMus(self):
        if(self.callBackMusic == False):
            self.callBackMusic = True
        else:
             self.callBackMusic = False
     #dừng nhạc
    def stopMusic(self):
        self.timer.cancel()  
        pygame.mixer.music.stop() 
        
        self.__playMusic = False
        self.uic.noi_dung_mp3.setValue(0)
        self.uic.time_label.setText("00:00")
    def playMusicToID(self,id):
        index = self.findIndexSongToID(id)
        self.index = index
        self.playMusic()
        self.restartTimer()
    #hàng đợi nhạc
    def queuMusic(self):
        for value in self.list:
            pygame.mixer.music.queue(value.link)
    #hiển thị thời gian
    def tong_thoi_gian_bai_hat(danh_sach_thoi_gian):
        tong = 0
        for thoi_gian in danh_sach_thoi_gian:
            phut, giay = thoi_gian.split(":")
            tong += int(phut) * 60 + int(giay)
        return tong   

    def display(self):
        self.currentTime = self.currentTime + 1
        mi = int(self.currentTime/60)
        if(mi < 10):
            mi = "0" + str(mi)
        second = int(self.currentTime%60)
        if(second < 10):
            second = "0" + str(second)
        self.uic.time_label.setText( "{}:{}".format(mi, second))
        self.uic.noi_dung_mp3.setValue(int(mi)*60+int(second))
        if int(self.currentTime) >= self.duration(self.list[self.index].link)-5:
            self.uic.noi_dung_mp3.setValue(0)
            self.uic.time_label.setText( "{}:{}".format("00", "00"))
            cel = self.findIndexSongTable(self.index)
            self.uic.table_list.selectRow(cel)
            self.nextMusic()
            self.restartTimer()

    #lui bài hát
    def prevMusic(self):
        if(self.callBackMusic == True):
            self.index = self.index
        elif(self.ran == True):
            self.index = self.random()
        elif self.index > 0:
            self.index -= 1   
        else:
            self.index = len(self.list)-1
        
        #chơi nhạc
        self.playMusic()
        self.restartTimer()
    def restartTimer(self):
        self.timer.cancel()
        self.timer = RepeatTimer(1,self.display) 
        self.timer.start()
    # chuyển tiếp bài hát
    def nextMusic(self):
        if(self.callBackMusic == True):
            self.index = self.index
        elif(self.ran == True):
            self.index = self.random()
            
        elif self.index < len(self.list)-1:
            self.index += 1 
        else:
            self.index = 0
        self.playMusic()
        self.restartTimer()
    def showMessageError(self):
        messagebox.showinfo("Error", "Không tìm thấy nguồn bài hát này")
    def playMusic(self):
        self.currentTime = 0
        image = self.list[self.index].image
        linkSong = self.list[self.index].link
        if(os.path.isfile(linkSong)):
            maxTime = self.duration(linkSong)-5
            pygame.mixer.music.load(linkSong)
            self.uic.ten_bai_hat.setText(self.list[self.index].name)
            if(image != ""):
                self.uic.label.setPixmap(QtGui.QPixmap(image))
            else:
                self.uic.label.setPixmap(QtGui.QPixmap("./image/tai_nghe.jpg"))
            cel = self.findIndexSongTable(self.index)
            #index = self.uic.table_list.model().index(cel, 0)
            if cel != -1:
                self.uic.table_list.selectRow(cel)
            self.uic.noi_dung_mp3.setMaximum(maxTime)
            pygame.mixer.music.play()
        else:
            self.showMessageError()
    def random(self):
        return random.randint(0, len(self.list)-2)
     #dừng bài hát
    def pause_music(self):
        pygame.mixer.music.pause()
        self.timer.cancel()
    #tìm vị trí bài hát
    def findIndexSong(self,row):
        song = self.listTemp[row]
        point = 0
        for value in self.list:
            if(song.id == value.id):
                return point
            point = point+1
        return -1
    def findIndexSongToID(self,id):
        point = 0
        for value in self.list:
            if(id == value.id):
                return point
            point = point+1
    #tìm vị trí bài hát trong bảng
    def findIndexSongTable(self,index):
        song = self.list[index]
        point = 0
        for value in self.listTemp:
            if(song.id == value.id):
                return point
            point = point+1
        return -1
    #hiển thị 
    def show_music(self):
        # self.mediaPlayer.play()
        # Tải tệp nhạc vào bộ nhớ
        if(self.__playMusic == False):   
            self.playMusic()
            self.restartTimer()
            self.__playMusic = True
        else:
            pygame.mixer.music.unpause()
            self.restartTimer()
    


    pygame
# Kết thúc game
pygame.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win=MainWindow()
    main_win.show()
    sys.exit(app.exec())
