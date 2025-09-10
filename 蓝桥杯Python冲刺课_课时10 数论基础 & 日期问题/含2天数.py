from datetime import *

t1 = date(1900, 1, 1)
t2 = date(9999, 12, 31)
delta = timedelta(1)
res = 0
while t1 < t2:
    if '2' in ''.join([str(t1.year), str(t1.month), str(t1.day)]): res += 1
    t1 += delta
print(res + 1) # 1994240

