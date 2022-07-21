class Mobi:
    def __init__(self,m,v = 90):
        self.modal = m
        self.volume = v
    def show(self,p):
        price = p
        print("Modal: ",self.modal ," and Price",price)
        print("Volume: ",self.volume)
realme = Mobi("Realme 5 Pro")
realme.show(14999)
