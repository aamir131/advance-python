f = open('writeline.txt','r')
data = f.readlines()       # this method is used to read all elements or all data
data1= f.readline()        # this method is used to read a single line 
data3= f.readline()
print(data)
print(data1)
print(data3)
f.close()
print("Complete!!!!")