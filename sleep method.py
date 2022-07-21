# sleep() method is used to stop execution of a program temporarily for a given amount of time. when this function is called, PVM(Python Vartual Machine) stops program execution for given amount of time
import time
for i in range(20):
    print(i)
    if i==10:
        time.sleep(5)