from abc import ABC,abstractmethod

class DefenceForce(ABC):
    @abstractmethod
    def area(sefl):
        pass
    def gun(self):
        print("Gun: AK47")
class Army(DefenceForce):
    def area(self):
        print("Army Area: Land")
class AirForce(DefenceForce):
    def area(self):
        print("AirForce Area: Sky")
class Navy(DefenceForce):
    def area(self):
        print("Navy Area: Sea")

a = Army()
af = AirForce()
n = Navy()
a.gun()
a.area()
print()
af.gun()
af.area()
print()
n.gun()
n.area()