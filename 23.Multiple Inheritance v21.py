class Father:
    def __init__(self):
        super().__init__()
        print("Father class Constructor")
    def showF(self):
        print("Father class Method")
class Mother:
    def __init__(self):
        super().__init__()
        print("Mother class Constructor")
    def showM(self):
        print("Mother class Method")
class Son(Father,Mother):
    def __init__(self):
        super().__init__()
        print("Son class Constructor")
    def showS(self):
        print("Son Class Method")
s = Son()
s.showS()
s.showF()
s.showM()