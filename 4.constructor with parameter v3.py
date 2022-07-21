# march 09 2021
# constructor with parameter
class Mobile:
    def __init__(self,m,v = 80): # This is a Constructor
        self.modal = m           # This is a Instance variable
        self.volume = v
    def show(self,p):            # instance method or This is a defination or Function   
        price = p                # Local variable
        print("modal: ",self.modal,"and Price: ",price) # Accessing Instance Variable
        print("Volume: ",self.volume)                   # Accessing Instance Variable

realme = Mobile("Realme X Pro")  # passing arguments to constructor and calling constructor
realme.show(15000)               # passing arguments to Functyion and calling function
print()
redmi = Mobile("Redmi Note Pro",40)
redmi.show(11000)
print()
oppo = Mobile("Oppo A7",60)
oppo.show(17000)