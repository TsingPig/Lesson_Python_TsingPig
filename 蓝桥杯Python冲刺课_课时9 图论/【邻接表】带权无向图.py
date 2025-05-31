n, m = map(int, input().split())
e = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    e[u].append((v, w))
    e[v].append((u, w))

for row in e:
    print(row)
