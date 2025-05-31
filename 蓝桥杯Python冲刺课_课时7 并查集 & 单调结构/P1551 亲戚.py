# https://www.luogu.com.cn/problem/P1551
import sys
input = lambda: sys.stdin.readline().strip()
n, m, p = map(int, input().split())


# 并查集模板
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
    # 通过合并，表示可达、连通关系
    union(u, v)

for _ in range(p):
    u, v = map(int, input().split())
    print('Yes' if find(u) == find(v) else 'No')
