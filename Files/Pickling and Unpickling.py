import pickle
class Student:
    def __init__(self,name,roll,address):
        self.name = name
        self.roll = roll
        self.address = address
    def disp():
        print(f'Name:{self.name} Roll:{self.roll} Address:{self.address}')

with open("Student.dat",'wb') as f:
    stu1 = Student("Mak", 211, 'Mumbai')
    pickle.dump(stu1,f)
    print("Picklink Done!!!!")