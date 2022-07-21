class Mobile:
    def __init__(self):             # Constructor
        self.modal = "Realme X"     # Instance Variable
    def show(self):                 # Instance Method
        print(self.modal)           # Accessing instance varibale
realme = Mobile()                   # Object
redmi = Mobile()
mak = Mobile()
print(realme.modal)
print(redmi.modal)
print(mak.modal)
print()

redmi.modal = "redmi note 9"
print(realme.modal)
print(redmi.modal)
print(mak.modal)
print()