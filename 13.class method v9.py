class Mobile:
    fp = 'Yes'
    @classmethod            # decorator
    def show(cls,r):        # class method
        cls.ram = r
        print("FingerPrint: ",cls.fp)
        print("RAM: ",cls.ram)
    
realme = Mobile()
Mobile.show("4GB")
