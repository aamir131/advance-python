class Father():
    money = 1000
    def show(self):
        print("Parents Class Instace method")
    @classmethod
    def showmoney(cls):
        print("Parents class Class method",cls.money)
    @staticmethod
    def stat():

        a = 10
        print("Parents Class Static Method",a)

class Son(Father):
    def disp(self):
        print("Child Class Instance Method")
s = Son()
s.disp()
s.show()
s.showmoney()
s.stat()