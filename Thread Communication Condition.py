from threading import Thread,Condition
from time import sleep
lst=[]
def produce():
    cv.acquire()
    for i in range(1,6):
        lst.append(i)
        sleep(1)
        print("Item Produce.....")
    cv.notify()
    cv.release()
def consume():
    cv.acquire()
    cv.wait(timeout=0)
    cv.release()
    print(lst)
cv = Condition()
t1 = Thread(target=produce)
t2 = Thread(target=consume)
t1.start()
t2.start()