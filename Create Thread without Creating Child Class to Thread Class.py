from threading import Thread
class Mythread(Thread):
    def disp(self,a,b):
        print(a,b)
myt = Mythread()                              # This is class object
t = Thread(target=myt.disp, args=(15,55))     # this is Thread object
t.start()