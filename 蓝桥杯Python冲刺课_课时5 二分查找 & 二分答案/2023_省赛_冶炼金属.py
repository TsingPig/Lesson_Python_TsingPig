import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
a, b = zip(*[map(int, input().split()) for _ in range(n)])

def bisect(lo, hi, check):
    while lo < hi:
        mid = (lo + hi) // 2
        if check(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo

m = bisect(1, 10**9, lambda v: all(A // v <= B for A, B in zip(a, b)))
M = bisect(1, 10**9, lambda v: any(A // v < B for A, B in zip(a, b))) - 1
print(m, M)
