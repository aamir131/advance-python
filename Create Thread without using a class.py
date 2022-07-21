# Create Thread without using a class 
from threading import Thread
def disp():
    for i in range(5):
        print("Publish Video C")
t = Thread(target=disp)
t.start()
for i in range(5):
    print("Publish Video M")
