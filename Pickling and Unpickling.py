import pickle
class Student:
    def __init__(self,name,roll,address):
        self.name = name
        self.roll = roll
        self.address = address
    def disp(self):
        print(f'Name:{self.name} Roll:{self.roll} Address:{self.address}')

with open("Student.dat",'wb') as f:
    stu1 = Student("Mak", 211, 'Mumbai')
    stu2 = Student("Aamir", 212, 'Delhi')
    pickle.dump(stu1,f)
    pickle.dump(stu2,f)
    print("Picklink Done!!!!")

with open("Student.dat",'rb') as f:
    obj1 = pickle.load(f)
    obj2 = pickle.load(f)
    print("Unpickling Done!!!")
    obj1.disp()
    obj2.disp()