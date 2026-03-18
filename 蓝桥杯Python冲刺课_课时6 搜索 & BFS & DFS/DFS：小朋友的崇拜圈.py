# https://www.lanqiao.cn/problems/182/learning/?page=1&first_category_id=1&tags=%E7%9C%81%E8%B5%9B,DFS&tag_relation=intersection&difficulty=20
import sys
input = lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(10000)  # 增加递归深度至少大于n，因为 python 默认为 1000
n = int(input())
g = [0] + list(map(int, input().split()))
res = 0
d = {}
def dfs(u, idx):
    global res
    if d.get(u) is not None:
        res = max(res, idx - d[u])   # 找到闭环，序号差就是环长
        return
    d[u] = idx
    dfs(g[u], idx + 1)
for u in range(1, n + 1):   # 确保访问所有连通分量
    dfs(u, 1)
print(res)