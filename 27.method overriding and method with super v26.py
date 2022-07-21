class Add:                                              # Father Class
    def result(self,x,y):                               # instance Method x, y is a parameter
        print("Addition of Two Numbers: ",x+y)
class Multi(Add):                                       # Child Class
    def result(self,a,b):                               # instance Method
        super().result(40,10)                # calling parent method class without creating a new object
        print("Multiplication of Two Numbers: ",a*b)
re = Multi()                                            # Calling Object
re.result(5,20)                                        # calling Method