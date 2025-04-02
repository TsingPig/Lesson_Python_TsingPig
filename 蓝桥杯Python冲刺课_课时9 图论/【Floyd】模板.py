from math import inf
n, m = map(int, input().split())
g = [[inf] * n for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    g[u][v] = g[v][u] = w
    g[u][u] = g[v][v] = 0

for k in range(n):
    for u in range(n):
        for v in range(n):
            g[u][v] = min(g[u][v], g[u][k] + g[k][v])
            
print(g)
print(g[4][2]) # 16
