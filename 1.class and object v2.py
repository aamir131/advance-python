# march 09 2021
class Mymobile:
    def __init__(self,m):
        self.modal = m
    def show(self,p):
        price = p
        print("Modal: ",self.modal, "price",price)
realme = Mymobile('Realme Narzo 20')
realme.show(10000)
print(id(realme))
print()

redmi = Mymobile("Redmi Note Pro9")
redmi.show(15000)
print(id(redmi))
print()
python = Mymobile('python')
python.show(100)
print(id(python))
print()