f = open('tellandseek.txt','r')
print(f.tell())                       # this method is used to check current blinking cursor position of the file
f.seek(4)                             # this method is used to move the cursor  
data = f.read()                       # this method is used to read a file
print(data)
f.close()
