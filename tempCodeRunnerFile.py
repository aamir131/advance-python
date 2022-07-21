from threading import Thread, current_thread
class Flight(Thread):
    def __init__(self,available_seat):
        self.available_seat = available_seat
    def reserve(self,need_seats):
        print("Available Seat",self.available_seat)
        if(self.available_seat>=need_seats):
            name = current_thread().name
            print(f'{self.available_seat} seat is alloted for {name}')
            self.available_seat-=need_seats
        else: