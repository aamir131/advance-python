class Student:
    def __init__(self,name,roll,address):
        self.name = name
        self.roll = roll
        self.address = address
    def disp(self):
        print(f'Name:{self.name} Roll:{self.roll} Address:{self.address}')
