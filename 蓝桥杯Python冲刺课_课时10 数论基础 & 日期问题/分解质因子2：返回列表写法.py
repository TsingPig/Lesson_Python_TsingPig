from math import *
# 统计质因子及其出现次数
def breakdown(x):
    res = []
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            cnt = 0
            while x % i == 0:
                x //= i
                cnt += 1
            res.append((i, cnt))
    if x > 1: res.append((x, 1))
    return res
print(breakdown(2 ** 3 * 3 ** 4 * 5 ** 2 * 7 * 14)) # [(2, 4), (3, 4), (5, 2), (7, 2)]
