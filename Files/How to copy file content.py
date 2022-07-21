f1 = open("Student.txt","r")
f2 = open("student1.txt",'w')
data = f1.read()
f2.write(data)          # This Method is used to copy file content from file one to another
f1.close()
f2.close()
