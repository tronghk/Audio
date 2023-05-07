from object.music import *
# from connect import *
class TypeDao:
    listType = [
        Type(0,"Unknown"),
        Type(1,"Nhạc trẻ"),
        Type(2,"Nhạc Trữ Tình"),
        Type(3,"Nhạc Không Lời"),
        Type(4,"Nhạc Hoa"),
        Type(5,"Nhạc Remix"),
    ]
    # connect = mydb.cursor()
    def __init__(self):
        pass
    def SelectListType(self):
        return self.listType
        # self.connect.execute("select * from TypeSong")
        # myresult = self.connect.fetchall()
        # list = []
        # for x in myresult:
        #     value =  Type(x[0],x[1])
        #     list.append(value)
        # mydb.commit()
        # return list
    # def Update(self,type):
    #     s = (type.name,type.id)
    #     self.connect.execute("update TypeSong name = %s where id = %s",s)
    #     mydb.commit()
    # def Delete(self,id):
    #     self.connect.execute("delete from TypeSong where id = %s",id)
    #     mydb.commit()
    def searchId(self,id):
       
        for x in self.listType:
            if x.id == id:
                return x.name
        return 
        # s = [id]
        # self.connect.execute("select * from TypeSong where id = %s",s)
        # myresult = self.connect.fetchall()
        # name  = myresult[0][1]
        # mydb.commit()
        # return name
    def searchName(self,name):
        for x in self.listType:
            if x.name == name:
                return x.id
        return 
        # s = [name]
        # self.connect.execute("select * from TypeSong where name = %s",s)
        # myresult = self.connect.fetchall()
        # id  = myresult[0][0]
        # mydb.commit()
        # return int(id)
