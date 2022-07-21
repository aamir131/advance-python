# datetime Module
from datetime import datetime
dt = datetime(year=2020, month=5, day=29)
dt1= datetime(year=2020, month=4, day=18, hour=11,minute=44)
dt2= datetime(2019, 8, 25)
dt3= datetime(2004, 2, 4, 18, 39)
print(dt)
print(dt1)
print(dt2) 
print(dt3)
print()
ct = datetime.now()
print(ct.hour)