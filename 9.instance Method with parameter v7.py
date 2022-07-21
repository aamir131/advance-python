class Mobile:
    def __init__(self,m):       # m is a Parameter
        self.modal = m
    def show(self,p):           # p is a Parameter
        self.price = p
        print("Modal: ",self.modal," and Price: ",self.price)

mak = Mobile("Realme 5")        # Realme 5 is a Arguments
mak.show(10999)                 # 10999 is a Arguments