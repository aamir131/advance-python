class Mobile:
    def __init__(self):                # Constructor
        self.modal = "Realme 5 Pro"    # instance Variable
        
    def show(self):                    # INSTANCE METHOD
        print("Modal: ",self.modal)

real = Mobile()                        # real is a Object
real.show()