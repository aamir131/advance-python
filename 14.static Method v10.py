class Mobile:
    @staticmethod       # decorator
    def show(m,p):      # static method with parametr
        modal = m
        price = p
        print("Modal: ",modal,"Price: ",price)
real = Mobile()
Mobile.show("Realme 6",12999)