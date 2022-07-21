class A:
    def __init__(self,x):
        self.x = x
    def __add__(self,other):
        return self.x + other.x
class A1:
    def __init__(self,x):
        self.x = x
a=A(90)
b=A1(110)
print(a+b)