from datetime import *
t1 = date(1901, 1, 1)
t2 = date(2000, 12, 31)

res = 0
while t1 <= t2:
    if t1.weekday() == 0:
        res += 1
    t1 += timedelta(days = 1)
print(res)
