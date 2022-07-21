from abc import ABC,abstractmethod

class DefenceForce(ABC):
    @abstractmethod             # 4 to 6 all are interface method
    def area(sefl):
        pass
    
class Army(DefenceForce):
    def gun(self):
        print("Gun: AK47")
    def area(self):
        print("Army Area: Land")
class AirForce(DefenceForce):
    def gun(self):
        print("Gun: AK40")
    def area(self):
        print("AirForce Area: Sky")
class Navy(DefenceForce):
    def gun(self):
        print("Gun: AK42")
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