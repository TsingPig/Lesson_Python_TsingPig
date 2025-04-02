# 【朴素二分】实现 bisect
def bisect(a, x, lo=0, hi=None):
    if hi is None: hi = len(a)
    while lo < hi:
        i = (lo + hi) >> 1
        if a[i] > x:
            hi = i
        else:
            lo = i + 1
    return lo

# 示例用法
a = [1, 9, 9, 9, 200, 500]

print(bisect(a, 9))  # 输出: 4
print(bisect(a, 7000))  # 输出: 6
