#This is r+ topic
#f = open("Filemode.txt",'r+')
#print(f.tell())
#data = f.read()
#print(f.tell())
#f.write("Google")   # string is not show because apply first read method
#print(f.tell())
#print(data)
#print(f.tell())
print()
# This is W+ topic
#w = open("flemode.txt","w+")
#print(w.tell())
#w.write("YoutubeVideos")  # string is not show because Blinkink cursor is at the end of the string
#print(w.tell())
#w.seek(0)                 # this method is used to show the string
#print(w.tell())
#data = w.read()
#print(w.tell())
#print(data)
#print(w.tell())
print()
# This is a+ topic
a = open("flemode.txt","a+")
print(a.tell())
a.write("Google")  # string is not show because Blinkink cursor is at the end of the string
print(a.tell())
a.seek(0)          # this method is used to show the string
print(a.tell())
data = a.read()
print(a.tell())
print(data)
print(a.tell())
