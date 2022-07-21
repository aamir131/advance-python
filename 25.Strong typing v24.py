class Duck:
    def walk(self):
        print("thapak thapak thapak thapak")
class Horse:
    def walk(self):
        print("tabdak tabdak tabdak tabdak")

class Cat:
    def talk(self):
        print("Meow Meow")


def myfunction(obj):            # this function
    if hasattr(obj, 'walk'):
        obj.walk()               # call object
    if hasattr(obj,'talk'):
        obj.talk()


d = Duck()
myfunction(d)

h = Horse()
myfunction(h)
print()
c = Cat()
myfunction(c)