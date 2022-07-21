from threading import*
class Flight():
    def __init__(self,available_seat):
        self.available_seat = available_seat
        self.l = BoundedSemaphore(2)
        print(self.l)                                          # this is a Thread syncronization
    def reserve(self,need_seats):
        self.l.acquire()  
        print(self.l._value)                                       
        print("Available Seat",self.available_seat)
        if(self.available_seat>=need_seats):
            name = current_thread().name
            print(f'{need_seats} seat is alloted for {name}')
            self.available_seat -=need_seats
        else:
            print('Sorry! All seats has alloted')
        self.l.release()
        
f = Flight(2) 
t1 = Thread(target=f.reserve,args=(1,),name='Mak')
t2 = Thread(target=f.reserve,args=(1,),name='Aamir')
t3 = Thread(target=f.reserve,args=(1,),name='AamirKhan')
t1.start()
t2.start()
t3.start()
