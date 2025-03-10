def f(x):
    return x ** 3 + x + 1
def bisect(lo, hi, target, check):
    while lo < hi:
        i = (lo + hi) >> 1
        if check(i, target):
            hi = i
        else:
            lo = i + 1
    return lo


target = 99999
res = bisect(1, 10 ** 18, target, lambda x, target: f(x) > target)
# 找到恰好 f(x) > target的地方
print(res)  # 47
print(f(res))  # 103871
print(f(res - 1))  # 97383
