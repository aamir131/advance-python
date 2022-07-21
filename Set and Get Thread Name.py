from threading import Thread, current_thread
def disp():
    pass
t = Thread(target=disp)

print("Child: ",t.getName())     # 1 to 8 is a object thread
t.setName("Mak")
print("New Child:",t.getName())
print()
print("default child:",t.name)      # 10 to 12 is a property method
t.name = "Spyder"
print("new name: ",t.name)


