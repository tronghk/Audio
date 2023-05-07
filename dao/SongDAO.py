from object.music import *
# from connect import *
class SongDao:
    listMusic = [
        Music(1,"Tìm em","./music/TimEm.mp3","./image/TimEm.jpg",5,5),
        Music(2,"Tình đầu","./music/TinhDau.mp3","./image/TimEm.jpg",4,4),
        Music(3,"Tình yêu khủng long","./music/TinhYeuKhungLong.mp3","./image/TimEm.jpg",3,3),
        Music(4,"Tòng phu","./music/TongPhu.mp3","./image/TimEm.jpg",2,2),
        Music(5,"Trên tình bạn dưới tình yêu","./music/TrenTinhBanDuoiTinhYeu.mp3","./image/TimEm.jpg",1,1),
        Music(6,"Hắc Nguyệt Quang","./music/HacNguyetQuang.mp3","./image/TimEm.jpg",1,1),
        Music(7,"Liên Hoa","./music/LienHoa.mp3","./image/TimEm.jpg",1,1),
        Music(8,"Nhớ Thương Một Người","./music/NhoThuongMotNguoi.mp3","./image/TimEm.jpg",1,1),
        Music(9,"Bất du","/media/tronghk/Workspace/Workspace/Python/ProjectPythonAudio/music/BatDu.mp3","./image/TimEm.jpg",0,0),
        Music(10,"Ưng quá chừng","/media/tronghk/Workspace/Workspace/Python/ProjectPythonAudio/music/UngQuaChung-AMEE-8783624.mp3","./image/TimEm.jpg",0,0),
    ]
    # connect = mydb.cursor()
    def __init__(self):
        pass
    def SelectList(self):
        # self.connect.execute("select * from Song")
        # myresult = self.connect.fetchall()
        # list = []
        # for x in myresult:
        #     value =  Music(x[0],x[1],x[2],x[3],x[4],x[5])
        #     list.append(value)
        # mydb.commit()
        return self.listMusic
    
    # def Update(self,value):
    #     s = (value.name,value.link,value.image,value.idType,value.idSinger,value.id)
    #     self.connect.execute("update Song name = %s, link = %s, image = %s, idType = %s, idSinger = %s where id = %s",s)
    #     mydb.commit()
    # def Delete(self,id):
    #     self.connect.execute("delete from Song where id = %s",id)
    #     mydb.commit()
    def Insert(self,value):
        song = Music(value.id,value.name,value.link,value.image,value.idType,value.idSinger)
        self.listMusic.append(song)
        # sql = "INSERT INTO Song (id,name,link,image,idType,idSinger) VALUES (%s, %s,%s,%s,%s,%s)"
        # s = (value.id,value.name,value.link,value.image,value.idType,value.idSinger)

        # self.connect.execute(sql,s)
        # mydb.commit()
    def searchTypeId(self,id):
        list = []
        for x in self.listMusic:
            if x.idType == id:
                list.append(x)
        # s = [id]
        # self.connect.execute("select * from Song where idType = %s",s)
        # myresult = self.connect.fetchall()
        # list = []
        # for x in myresult:
        #     value =  Music(x[0],x[1],x[2],x[3],x[4],x[5])
        #     list.append(value)
        # mydb.commit()
        return list
    def searchTypeName(self,name):
        for x in self.listMusic:
            if x.name == name:
                return x
        return 
        # s = [name]
        # self.connect.execute("select * from Song where name = %s",s)
        # myresult = self.connect.fetchall()
        # id = myresult[0][0]
        # name  = myresult[0][1]
        # link  = myresult[0][2]
        # image  = myresult[0][3]
        # idType  = myresult[0][4]
        # idSinger  = myresult[0][5]
        # m = Music(int(id),name,link,image,int(idType),int(idSinger))
        # mydb.commit()
        # return m
    def searchListName(self,name):

        list = []
        for x in self.listMusic:
            if x.name == name:
                list.append(x)
        return list
        # s = [name]
        # self.connect.execute("select * from Song where name = %s",s)
        # myresult = self.connect.fetchall()
        # list = []
        # for x in myresult:
        #     value =  Music(x[0],x[1],x[2],x[3],x[4],x[5])
        #     list.append(value)
        # mydb.commit()
        # return list
    def searchListSongJoinType(self,id):
        list = []
        for x in self.listMusic:
            if x.idType == id:
                list.append(x)
        return list
        # s = [id]
        # self.connect.execute("select Song.id,Song.name,Song.link,Song.image,Song.idType,Song.idSinger"+
        #                       "from Song INNER JOIN TypeSong on Song.idType=TypeSong.id where TypeSong.id = %s",s)
        # myresult = self.connect.fetchall()
        # list = []
        # for x in myresult:
        #     value =  Music(x[0],x[1],x[2],x[3],x[4],x[5])
        #     list.append(value)
        # mydb.commit()
        # return list
    def searchListSongJoinSinger(self,id):
        list = []
        for x in self.listMusic:
            if x.idSinger == id:
                list.append(x)
        return list
        # s = [id]
        # self.connect.execute("select Song.id,Song.name,Song.link,Song.image,Song.idType,Song.idSinger"+
        #                       "from Song INNER JOIN Singer on Song.idSinger=Singer.id where Singer.id = %s",s)
        # myresult = self.connect.fetchall()
        # list = []
        # for x in myresult:
        #     value =  Music(x[0],x[1],x[2],x[3],x[4],x[5])
        #     list.append(value)
        # mydb.commit()
        # return list
    def addMusic(self,link,name):
        maxId = len(self.SelectList())+1
        song = Music(maxId,name,link,'',0,0)
        self.listMusic.append(song)
        
        # s = [str(maxId),name,link,'','0','0']
        # self.connect.execute("INSERT INTO Song(id,name,link,image,idType,idSinger)"+
        #                      "Values(%s,%s,%s,%s,%s,%s)",s)
        # mydb.commit()