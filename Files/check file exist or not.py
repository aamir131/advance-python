import os
if os.path.isfile('stud.txt'):
    f = open('stud.txt')
    print("File Opened")
    f.close()
else:
    print("File Not Found")