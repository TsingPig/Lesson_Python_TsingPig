from math import *
def solve(x):
    res = []
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            res.append(i)
            if i != x // i:
            	res.append(x // i)
    return res
print(solve(24)) # [2, 12, 3, 8, 4, 6]
