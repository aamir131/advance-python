class Mobile:
    fp = "yes"
    def __init__(self):
        self.modal = "Realme X"
    def show(self):
        print("Modal: ",self.modal)
    
    @classmethod
    def is_fp(cls):
        print("Finger Print",cls.fp)

realme = Mobile()
redmi = Mobile()
mak = Mobile()

print(Mobile.fp)
print(realme.fp)
print(redmi.fp)
print(mak.fp)
print()
mak.fp = 'No'
print(Mobile.fp)
print(realme.fp)
realme.show()
print(redmi.fp)
print(mak.fp)