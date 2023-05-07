import sys
import pygame
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QPushButton
# from PyQt5.QtMultimedia import QMediaPlayer,QMediaContent
# from PyQt5.QtMultimediaWidgets import QVideoWidget
# from PyQt5.QtCore import QUrl
from ui.Danh_Sach_Nhac import Ui_MainWindow as Danh_Sach_Nhac_Ui_MainWindow
# from main import MainWindow
from threading import Timer
from main import *
from controller.MusicController import *
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
from main import RepeatTimer
class Main_List_Music_MainWindow(QMainWindow):
    list = []
    index = -1
    currentTime = 0
    timer = ""
    volumn = 0
    controller = MusicController()
    def __init__(self):
        super().__init__()
        self.uic= Danh_Sach_Nhac_Ui_MainWindow()
        self.uic.setupUi(self)
        self.timer = RepeatTimer(1,self.setCurrent) 
        self.timer.start()
        self.uic.tro_ve.clicked.connect(self.ve_main)
        self.getListSong()
    def ve_main(self):
        from main import MainWindow
        self.timer.cancel()
        # Khởi tạo QStackedWidget
        self.stacked_widget = QStackedWidget(self)
        
        # Tạo hai trang con cho QStackedWidget
        self.main_widget = Main_List_Music_MainWindow()
        # self.main_widget.setObjectName("MainWidget")
        # self.main_widget.setStyleSheet("#MainWidget { background-color: #000; }")
        self.thu_vien = QPushButton("Hãy click tôi để chuyển vào trang chủ nhé nhé !!!", self.main_widget)
        self.thu_vien.setGeometry(50, 50, 250, 50)
        
        self.list_music_widget = MainWindow()
        cel = self.list_music_widget.findIndexSongTable(self.index)
        self.list_music_widget.uic.table_list.selectRow(cel)
        self.list_music_widget.currentTime = self.currentTime
        self.list_music_widget.index = self.index
        if(self.list_music_widget.list[self.index].image != ""):
                self.list_music_widget.uic.label.setPixmap(QtGui.QPixmap(self.list[self.index].image))
        else:
                self.list_music_widget.uic.label.setPixmap(QtGui.QPixmap("./image/tai_nghe.jpg"))
        self.list_music_widget.uic.ten_bai_hat.setText(self.list_music_widget.list[self.index].name)
        self.list_music_widget.uic.volume.setValue(self.volumn)
        self.list_music_widget.timer.start()
        self.stacked_widget.addWidget(self.main_widget)
        self.stacked_widget.addWidget(self.list_music_widget)
        
        self.setCentralWidget(self.stacked_widget)
        self.stacked_widget.setCurrentWidget(self.list_music_widget)

    def setCurrent(self):
           self.currentTime = self.currentTime+1
    def getListSong(self):
        self.list = self.controller.listSong()
        self.uic.ten1.setText(self.list[0].name)
        self.uic.ten2.setText(self.list[1].name)
        self.uic.ten3.setText(self.list[2].name)
        self.uic.ten4.setText(self.list[3].name)
        self.uic.ten5.setText(self.list[4].name)
        self.uic.ten6.setText(self.list[5].name)
        self.uic.ten7.setText(self.list[6].name)
        self.uic.ten8.setText(self.list[7].name)
        self.uic.ten9.setText(self.list[8].name)

        if(self.list[0].image != ""):
                self.uic.anh1.setPixmap(QtGui.QPixmap(self.list[0].image))
        else:
                self.uic.anh1.setPixmap(QtGui.QPixmap("./image/tai_nghe.jpg"))
        if(self.list[1].image != ""):
                self.uic.anh2.setPixmap(QtGui.QPixmap(self.list[1].image))
        else:
                self.uic.anh2.setPixmap(QtGui.QPixmap("./image/tai_nghe.jpg"))
        if(self.list[3].image != ""):
                self.uic.anh4.setPixmap(QtGui.QPixmap(self.list[3].image))
        else:
                self.uic.anh4.setPixmap(QtGui.QPixmap("./image/tai_nghe.jpg"))
        if(self.list[4].image != ""):
                self.uic.anh5.setPixmap(QtGui.QPixmap(self.list[4].image))
        else:
                self.uic.anh5.setPixmap(QtGui.QPixmap("./image/tai_nghe.jpg"))
        if(self.list[5].image != ""):
                self.uic.anh6.setPixmap(QtGui.QPixmap(self.list[5].image))
        else:
                self.uic.anh6.setPixmap(QtGui.QPixmap("./image/tai_nghe.jpg"))

        if(self.list[6].image != ""):
                self.uic.anh7.setPixmap(QtGui.QPixmap(self.list[6].image))
        else:
                self.uic.anh7.setPixmap(QtGui.QPixmap("./image/tai_nghe.jpg"))
        if(self.list[7].image != ""):
                self.uic.anh8.setPixmap(QtGui.QPixmap(self.list[7].image))
        else:
                self.uic.anh8.setPixmap(QtGui.QPixmap("./image/tai_nghe.jpg"))
        if(self.list[8].image != ""):
                self.uic.anh9.setPixmap(QtGui.QPixmap(self.list[8].image))
        else:
                self.uic.anh9.setPixmap(QtGui.QPixmap("./image/tai_nghe.jpg"))
        if(self.list[2].image != ""):
                self.uic.anh3.setPixmap(QtGui.QPixmap(self.list[2].image))
        else:
                self.uic.anh3.setPixmap(QtGui.QPixmap("./image/tai_nghe.jpg"))


        self.uic.nghesi1.setText(self.controller.searchSingerId(self.list[0].idSinger))
        self.uic.nghesi2.setText(self.controller.searchSingerId(self.list[1].idSinger))
        self.uic.nghesi3.setText(self.controller.searchSingerId(self.list[2].idSinger))
        self.uic.nghesi5.setText(self.controller.searchSingerId(self.list[3].idSinger))
        self.uic.nghesi4.setText(self.controller.searchSingerId(self.list[4].idSinger))
        self.uic.nghesi6.setText(self.controller.searchSingerId(self.list[5].idSinger))
        self.uic.nghesi7.setText(self.controller.searchSingerId(self.list[6].idSinger))
        self.uic.nghesi8.setText(self.controller.searchSingerId(self.list[7].idSinger))
        self.uic.nghesi9.setText(self.controller.searchSingerId(self.list[8].idSinger))
        self.uic.phat_1.clicked.connect(partial(self.playMusic,self.list[0].id))
        self.uic.phat_2.clicked.connect(partial(self.playMusic,self.list[1].id))
        self.uic.phat_3.clicked.connect(partial(self.playMusic,self.list[2].id))
        self.uic.phat_4.clicked.connect(partial(self.playMusic,self.list[3].id))
        self.uic.phat_5.clicked.connect(partial(self.playMusic,self.list[4].id))
        self.uic.phat_6.clicked.connect(partial(self.playMusic,self.list[5].id))
        self.uic.phat_7.clicked.connect(partial(self.playMusic,self.list[6].id))
        self.uic.phat_8.clicked.connect(partial(self.playMusic,self.list[7].id))
        self.uic.phat_9.clicked.connect(partial(self.playMusic,self.list[8].id))
    def playMusic(self,id):
        from main import MainWindow
        # Khởi tạo QStackedWidget
        self.stacked_widget = QStackedWidget(self)
        # Tạo hai trang con cho QStackedWidget
        self.main_widget = Main_List_Music_MainWindow()
        # self.main_widget.setObjectName("MainWidget")
        # self.main_widget.setStyleSheet("#MainWidget { background-color: #000; }")
        self.thu_vien = QPushButton("Hãy click tôi để chuyển vào trang chủ nhé nhé !!!", self.main_widget)
        self.thu_vien.setGeometry(50, 50, 250, 50)
        
        self.list_music_widget = MainWindow()
        self.stacked_widget.addWidget(self.main_widget)
        self.stacked_widget.addWidget(self.list_music_widget)
        self.list_music_widget.playMusicToID(id)
        self.setCentralWidget(self.stacked_widget)
        self.stacked_widget.setCurrentWidget(self.list_music_widget)
        
    pygame
# Kết thúc game
pygame.quit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win=Main_List_Music_MainWindow()
    main_win.show()
    sys.exit(app.exec())