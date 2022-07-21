f = open('writeline.txt','r')
data = f.read(3)
data1= f.read(3)        # this method is used to read a character 
data3= f.read(6)
print(data)
print(data1)
print(data3)
f.close()
print("Complete!!!!")