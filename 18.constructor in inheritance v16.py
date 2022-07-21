class Father:
    def __init__(self,m):
        self.money = m
        print("Father Class Constructor")
    def show(self):
        print("Father Class Instance Method ")

class Son(Father):
    def disp(self):
        print("Son Class Instance Method")

s = Son(20101)
print(s.money)
s.show()
s.disp()