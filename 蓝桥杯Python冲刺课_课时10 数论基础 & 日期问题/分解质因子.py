from math import *
def solve(x):
    for i in range(2, int(sqrt(x)) + 1):	# i = 2; i * i <= x
        if x % i == 0:
            s = 0
            while x % i == 0:
                s += 1
                x //= i
            print(f'{i} {s}')		# i 是质因子， s 表示幂次
    if x > 1:
        print(f'{x} 1')
    print()

solve(2 ** 3 * 3 ** 4 * 5 ** 2 * 7 * 14)
