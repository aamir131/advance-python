class Students:
    def __init__(self,n,r):
        self.name = n
        self.roll = r
    def disp(self):
        print("Students Name: ",self.name)
        print("Students Roll: ",self.roll)

class User:
    @staticmethod
    def show(s):
        print("Username: ",s.name)
        print("Userroll: ",s.roll)
        s.disp()
stu = Students("Mak",211)
User.show(stu)
