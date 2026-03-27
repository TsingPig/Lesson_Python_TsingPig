from math import inf
n, m = map(int, input().split())
g = [[inf] * n for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    g[u][v] = g[v][u] = w
    g[u][u] = g[v][v] = 0


d = [inf] * n
d[4] = 0
s = set() # S集合为已经确定的节点集合


for _ in range(n - 1):
    x = -1
    # 从 U - S中找出距离S最近的节点
    for u in range(n):
        if u not in s and (x < 0 or d[u] < d[x]):
            x = u
    s.add(x)

    # 松弛，对每个节点判断以x作为中间节点时，是否距离原点更加
    for u in range(n):
        d[u] = min(d[u], d[x] + g[u][x])

print(d) # [10, 11, 16, 7, 0]
