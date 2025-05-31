# 【朴素二分】实现 bisect，支持传递check函数
def bisect(a, x, lo = 0, hi = None, check = lambda y: y):
    if hi is None: hi = len(a)
    while lo < hi:
        i = (lo + hi) >> 1
        if check(a[i]) > x:
            hi = i
        else:
            lo = i + 1
    return lo
# 示例用法
a = [1, 9, 9, 9, 200, 500]
# 找到 a[i] ** 3 + a[i] * 2 + 1 恰好大于x的位置
x = 1000
print(bisect(a, x, check = lambda y: y ** 3 + y * 2 + 1)) # 4
