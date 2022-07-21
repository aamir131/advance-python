# storing object in the file
import pickle,clas
n = int(input("Enter number Student: "))
with open("Student.dat",'wb') as f:
    for i in range(n):
        name = input("Enter Student Name: ")
        roll = int(input("Enter Student Roll No.: "))
        address = input("Enter Student Adrees")
        stu1 = clas.Student(name, roll, address)
        pickle.dump(stu1,f)                           # This method is used for Storing the object
    
print("Picklink Done!!!!")