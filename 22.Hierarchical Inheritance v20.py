class Father:
    def __init__(self):
        print("Father class Constructor")
    def showF(self):
        print("Father Class Method")
class Son(Father):
    def __init__(self):
        super().__init__()
        print("Son class Constructor")
        
    def showS(self):
        print("Son Class method")
class Daughter(Father):
    def __init__(self):
        super().__init__()
        print("Daughter class Constructor")
    def showD(self):
        print("Daughter Class method")

d = Son()
