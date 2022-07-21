f = open('writemethod.txt',"w")
f.write("Hello\n")      # w mode in this method is alway data overrite because blinkking cursor are begnning
n =(f.write("Mak\n"))   # Count length of the string
f.write("How Are You")
f.close()
print(n)

print()
e = open('exclusivemethod.txt',"x")
e.write("Hello\n")      # x mode in this method is alway required new file
n =(e.write("Mak\n"))   # Count length of the string
e.write("How Are You")
e.close()
print(n) 
print()
ap = open('appendmethod.txt',"a")
ap.write("Hello ")      # a mode in this method data is not overrite because blinkking cursor at the end of the file
n =(ap.write("Mak\n"))   # Count length of the string
ap.write("How Are You")
ap.close()
print(n)