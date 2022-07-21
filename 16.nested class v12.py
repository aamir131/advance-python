class Army:                            # Outer Class
    def __init__(self):                # Constructor
        self.name = "Rahul"            # Instance Variable

    def show(self):                    # Instance Method
        print('Name: ',self.name)

    class Gun:                         # Inner Class
        def __init__(self):
            self.name = "AK47"         # Instance Variable
            self.capacity = "75 Round" # Instance Variable
            self.length = "34.3 In"    # Instance Variable
        def disp(self):                # Instance Method
            print("Gun Name: ",self.name,)
            print("Gun Capacity: ",self.capacity)
            print("Gun Length: ",self.length)

a = Army()              # Outer Class Object
a.show()                # Calling Outer Instance Method
print()
g = Army().Gun()        # Inner Class Object

print(g.name)
print(g.capacity)
print(g.length)
print()
g.disp()                # Calling Inner Instance Method