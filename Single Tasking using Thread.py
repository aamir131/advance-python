from threading import Thread
from time import sleep
class MyExam(Thread):
    def question_solve(self):
        self.q1()
        self.q2()
        self.q3()
        self.q4()
    def q1(self):
        print("Question 1 solved")
        sleep(5)
    def q2(self):
        print("Question 2 solved")
        sleep(5)
    def q3(self):
        print("Question 3 solved")
        sleep(5)
    def q4(self):
        print("Question 4 solved")
mye = MyExam()
t = Thread(target=mye.question_solve)
t.start()