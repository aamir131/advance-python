class Father:
    def __init__(self,m):
        self.money = m
        print("Father class Constructor")
    def show(self):
        print("Father Class Instance Method")

class Son(Father):
    def __init__(self,m,j):
        super().__init__(m)        # calling fatherclass constructor using super method
        print("Son Class Constructor")
        self.job = j
    def disp(self):
        print("Son Class Instance Method",self.money,"Job: ",self.job)

s = Son(1000,"python")
s.disp()