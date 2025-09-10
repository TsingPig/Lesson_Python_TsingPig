'''
https://www.luogu.com.cn/problem/P8218
'''
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
a = list(map(int, input().split()))
q = int(input())

# 前缀和模板, p[i] = sum(a[:i])
p = [0] * (n + 1)
for i in range(n):
    p[i + 1] = p[i] + a[i]

for _ in range(q):
    l, r = map(int, input().split())
    print(p[r] - p[l - 1])