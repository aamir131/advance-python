# How to calculate age
from datetime import date
dob = date(2001, 2, 5)
t = date.today()
age = t.year - dob.year - ((t.month, t.day) < (dob.month, dob.day))
print(age)