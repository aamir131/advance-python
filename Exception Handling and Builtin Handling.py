a = 20
b = 5
try:
    c = a/b 
    print(c)
except (NameError,ZeroDivisionError) as obj:
    print(obj)
print("Rest of the code")