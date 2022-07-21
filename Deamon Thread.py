from time import sleep
from threading import Thread, current_thread
def disp():
    print("Disp Function")
    t2 = Thread(target=Show)
    print("T2: ",t2.isDaemon())
    t2.start()

def Show():
    print("Show Function")

mt = current_thread()
print(mt.getName())
print("Mt:",mt.isDaemon())
t1 = Thread(target=disp)
print("Before T1",t1.isDaemon())
t1.setDaemon(True)
print("After T1",t1.isDaemon())
t1.start()
t1.join()
print()
print()
# 2nd Example
def teacher():
    for i in range(1,11):
        print("Teaching session: ",i)
        sleep(1)
T = Thread(target=teacher)

T.setDaemon(True)
T.start()
sleep(4)
print("Exam Finished",current_thread().name)