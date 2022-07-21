# Read object from the file
import pickle,clas
with open("Student.dat",'rb') as f:
    while True:
        try:
            obj = pickle.load(f)            # This method is used for read the object
            obj.disp()
        except EOFError:
            print("Unpickling Done!!!!!!!!")
            break
    