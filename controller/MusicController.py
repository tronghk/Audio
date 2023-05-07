from object.music import *
from dao.TypeDAO import *
from dao.SingerDAO import *
from dao.SongDAO import *
class MusicController:
    typeDao = TypeDao()
    singerDao = SingerDao()
    songDao = SongDao()
    def __init__(self) -> None:
        pass
    def searchTypeId(self,id):
        return self.typeDao.searchId(id)
    def searchSingerId(self,id):
        return self.singerDao.searchId(id)
    def listTypeDao(self):
        return self.typeDao.SelectListType()
    def searchListSongType(self,type):
        idType = self.typeDao.searchName(type)
        return self.songDao.searchTypeId(idType)
    def searchText(self, text):
        list = []
        while(len(list) == 0 ):
            list = self.searchNameSong(text)
            if len(list) > 0:
                return list
            list = self.searchListSongToType(self.searchNameType(text))
            if len(list) > 0:
                return list
            list = self.searchListSongToSinger(self.searchNameSinger(text))
            if len(list) > 0:
                return list
            if len(text) == 0:
                break
            text = text[1:]
           
        return list
    def searchNameSong(self,name):
        result = []
        length = len(name)
        list = self.songDao.SelectList()
        for value in list:
            if name == value.name[0:length]:
                result.append(value)
        return result
    def searchNameType(self,name):
        result = []
        length = len(name)
        listType = self.typeDao.SelectListType()
        for value in listType:
            if name == value.name[0:length]:
                result.append(value)
        return result
    def searchListSongToType(self,list):
        listSong = self.listSong()
        result = []
        for value in list:
            for song in listSong:
                if value.id == song.idType:
                    result.append(song)
        return result
    def searchNameSinger(self,name):
        result = []
        length = len(name)
        list = self.singerDao.SelectList()
        for value in list:
            if name == value.name[0:length]:
                result.append(value)
        return result
    def searchListSongToSinger(self,list):
        listSong = self.listSong()
        result = []
        for value in list:
            for song in listSong:
                if value.id == song.idSinger:
                    result.append(song)
        return result
    def listSong(self):
        return self.songDao.SelectList()
    def addMusic(self,link,name):
        self.songDao.addMusic(link,name)
