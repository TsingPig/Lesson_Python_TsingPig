# https://www.luogu.com.cn/problem/P1536
import sys
input = lambda: sys.stdin.readline().strip()

while True:
    s = input()
    if s == '0': break
    n, m = map(int, s.split())
    fa = list(range(n + 1))
    def find(x):
        if fa[x] == x: return x
        fa[x] = find(fa[x])
        return fa[x]
    def union(u, v):
        if find(u) != find(v):
            fa[find(v)] = find(u)
    for _ in range(m):
        u, v = map(int, input().split())
        union(u, v)

    # 压缩成严格菊花集
    for x in range(1, n + 1):
        fa[x] = find(x)
        
    cnt = len(set(fa)) - 1 # 连通块数量，-1是减去下标0
    print(cnt - 1)  # cnt - 1是需要修路数量
