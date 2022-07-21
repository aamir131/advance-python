from threading import Thread
class Mythread(Thread):
    def __init__(self,a):
        Thread.__init__(self)
        print("Child Thread constructor",a)
        
    def run(self):
        pass
t = Mythread(10)
t.start()
print("MAin Thread")