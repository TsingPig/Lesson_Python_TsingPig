n, m = map(int, input().split())
e = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    e[u].append((v, w))
    e[v].append((u, w))

s = set() # 已经访问的
def dfs(u):
    for v, _ in e[u]:
        if v not in s:
            dfs(v)
    
dfs(0) # 0 1 2 3 4 
print() 
s.clear() #已经访问的
dfs(4) # 4 3 0 1 2 
