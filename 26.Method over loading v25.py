class Method:
    def sum(self,a=None,b=None,c=None):                         # Method and a,b,c is a arguments
        if (a!=None and b!=None and c!=None):                   # Task
            s = a+b+c
        elif(a!=None and b!=None):                              # Task
            s = a*b
        else:
            s = 'Provide atleast 2 Numbers'                     # Task
        return s
obj = Method()                                                  # Object
res = obj.sum(10)                                               # calling sum Method and 10 is a parameter
print(res)