from math import inf
n, m = map(int, input().split())
g = [[inf] * n for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    g[u][v] = g[v][u] = w 
    g[u][u] = g[v][v] = 0 # 原地不动，距离是0
