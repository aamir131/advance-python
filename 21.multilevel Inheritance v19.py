class Father:
    def __init__(self):
        print("Father Class Constructor")
    def showF(self):
        print("Father Class Method")

class Son(Father):
    def __init__(self):
        super().__init__()          # calling Father class constructor 
        print("Son Class Constructor")
    def showS(self):
        print("Son Class Method")
class Grandson(Son):
    def __init__(self):
        super().__init__()          # calling Son class constructor
        print("Grandson Class Constructor")
    def showG(self):
        
        print("Grandson Class Method")
g = Grandson()
print()
g.showG()
g.showF()
g.showS()
