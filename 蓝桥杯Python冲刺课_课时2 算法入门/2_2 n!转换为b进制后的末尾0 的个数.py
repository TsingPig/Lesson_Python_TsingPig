import sys
input = lambda: sys.stdin.readline().strip()
from math import *
# 统计 n! 中质因子 p 出现的次数
def fpf(n, p):   # factorial_prime_factor
    res = 0
    while n:
        res += n // p
        n //= p
    return res
# 统计质因子及其出现次数
def breakdown(n):
    res = []
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                n //= i
                cnt += 1
            res.append((i, cnt))
    if n > 1: res.append((n, 1))
    return res
def solve():
    n, b = map(int, input().split())
    pf = breakdown(b) # 对b进行质因子分解
    res = inf
    for f, c in pf:
        res = min(res, fpf(n, f) // c)
    return res
print(solve())