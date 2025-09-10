
import sys
input = lambda: sys.stdin.readline().strip()
# 请在此输入您的代码
# 4 7 5 6 20 1 4 15 30             6
# 4
from heapq import *
n, m = map(int, input().split())
s = input()

hq = []
res = ''
L = 0
for i in range(m):
    heappush(hq, (s[i], i))
for R in range(m, n):
    heappush(hq, (s[R], R))
    
    mn, mni = heappop(hq)
    while mni < L:
        mn, mni = heappop(hq)
    res += mn 
    L = mni + 1
print(res)
