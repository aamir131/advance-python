from threading import Thread
class MyThread(Thread):
    def run(self):
        for i in range(5):
            print("Child Thread")
t = MyThread()
t.start()
t.join()        # this method is used to first execute child method then execute any other method
for i in range(5):
    print("Main Thread")