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
    obj.walk()          # call object
d = Duck()
myfunction(d)

h = Horse()
myfunction(h)

c = Cat()
myfunction(c)