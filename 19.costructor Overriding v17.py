class Father:
    def __init__(self):
        self.money = 2000
        print("Father class Constructor")
    def show(self):
        print("Father Class Instance Method")

class Son(Father):
    def __init__(self):
        self.money = 50000
        self.car = "BMW"
        print("Son Class Constructor")
    def disp(self):
        print("Son Class Instance Method")
f = Father()
s = Son()
print(s.money)
print(s.car)
print()
s.show()
s.disp()