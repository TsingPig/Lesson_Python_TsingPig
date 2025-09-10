### 枚举DFS

[5.最大数字 - 蓝桥云课 (lanqiao.cn)](https://www.lanqiao.cn/problems/2193/learning/?page=1&first_category_id=1&tags=DFS,国赛&tag_relation=intersection&difficulty=20)

**思路**

- 贪心，从左到右，尽可能构造 9。

- 对每一位数字，只会用一种操作。
- 记 $dfs(i, n, a, b)$表示当前考虑到第 $i$位，剩下 $a$次操作1和 $b$次操作2情况下，当前获得的最大数为 $n$ 
- 对于操作1，考虑 $d=min(9-x,a)$，即当前能够执行操作1的次数
- 则 $n ← n \times 10 + (x + d)$，$a ← a - d $
- 对于操作2，考虑 $b$ 是否大于等于 $x + 1$，是则可以得到9，且 $b ← b - (x + 1)$

```python
import sys
input = lambda: sys.stdin.readline().strip()
N, A, B = map(int, input().split())
sN = str(N)
res = 0
def dfs(i, n, a, b):
    global res 
    if i >= len(sN):
        res = max(res, n) 
        return 
    x = int(sN[i])
    d = min(9 - x, a)
    dfs(i + 1, n * 10 + (x + d), a - d, b)
    if b >= x + 1:
        dfs(i + 1, n * 10 + 9, a, b - (x + 1))
dfs(0, 0, A, B)
print(res)
```



### 图上DFS

[1.小朋友崇拜圈 - 蓝桥云课 (lanqiao.cn)](https://www.lanqiao.cn/problems/182/learning/?page=1&first_category_id=1&tags=省赛,DFS&tag_relation=intersection&difficulty=20)

**语言整理**

一个有向图，每个节点 $u$ 有且仅有一条出边 $u→v$。给定 $g$ 数组，$g[u]=v$ 表示这条出边。

求图中最长环的长度。

**思路**

- $dfs(u)$ 表示当前访问节点 $u$，集合 $s$ 表示访问过的节点集
- 如果 $u$ 在 $s$ 中，说明找到了环
- 如果 $u$ 不在 $s$ 中，添加到集合中，并且访问后续节点 $dfs(g[u])$
- 遍历所有节点，确保考虑到所有连通分量。

类似代码：

```python
s = set
def dfs(u):
    if u in s: return # 找到了环
    s.add(u)
    dfs(g[u])
for u in range(1, n + 1):
    dfs(u)
```

- 那么怎么求解环的长度？

**思路**

- 时间戳思想，额外记录每次访问节点 $u$ 的序号 $idx$，字典 $d$ 存放 $u:idx$ 键值对
- 如果 $u$ 在 $d$ 中，说明第二次访问到 $u$ ，构成闭环。两次序号之差 $idx - d[u]$ 即环的长度
- 如果 $u$ 不在 $d$ 中，添加到字典中，并且访问后续节点 $dfs(g[u], idx + 1)$ 
- 遍历所有节点，确保考虑所有连通分量
- 在外层用 $res$ 记录最大环长。

正解代码：

```python
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
```



### 模拟 BFS



**网格图模拟BFS**

- 是给定一个二维网格，以及一些初始位置，并说明初始位置的蔓延条件。
- 通过队列 $q$ 存储位置。初始值即为初始位置
- 每次考虑当前位置 $(x,y)$ 的四周，尝试蔓延

![img](https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg)

网格图BFS模板。

```python
# 设置q的初始值，如 q.append(...)
q = deque([(3, 4)]) # 或者 q = deque() 之后，q.append((3, 4))
g[3][4] = 0 # 标记访问过
di = [(0, 1), (0, -1), (1, 0), (-1, 0)]
while q:
    x, y = q.popleft() # 弹出队首
    for dx, dy in di:   # 遍历四个方向，尝试蔓延
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 1: # 判断蔓延是否合法
            q.append((nx, ny))  # 加到队尾，表示后续开始蔓延的位置
            g[nx][ny] = 0 # 标记访问过
            # 其他操作
```



[695. 岛屿的最大面积 - 力扣（LeetCode）](https://leetcode.cn/problems/max-area-of-island/description/)

**思路**

- 枚举每个连通的岛屿，通过将访问过的位置设置为0，即 $grid[i][j] = 0$ 进行记录
- 每个岛屿的“登陆点”即为 $q$ 的初始内容
- 每次将 $q$ 的队首弹出，考虑其上下左右是否有陆地，是则加入到队尾，并且标记访问过，更新岛屿面积
- 重复操作，直到 $q$为空。

```python
class Solution:
    def maxAreaOfIsland(self, g: List[List[int]]) -> int:
        n, m = len(g), len(g[0])
        q = deque()
        res = 0
        di = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def bfs(i, j):  # 考虑登陆点为 (i, j)的岛屿
            ans = 1
            q = deque([(i, j)]) 
            g[i][j] = 0 # 登陆点设置为0，表示已经访问过
            while q:
                x, y = q.popleft() # 弹出队首
                for dx, dy in di:   # 遍历四个方向，考虑是否有陆地
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and g[nx][ny]:   
                        q.append((nx, ny))  # 有陆地，加到队尾，表示后续需要考虑的位置
                        ans += 1
                        g[nx][ny] = 0 # 标记访问
            return ans             
        for i, row in enumerate(g):
            for j, x in enumerate(row):
                if x == 1:  # 遍历所有连通分量
                    res = max(res, bfs(i, j))
        return res 
```



[1.长草 - 蓝桥云课 (lanqiao.cn)](https://www.lanqiao.cn/problems/149/learning/?page=1&first_category_id=1&tags=BFS&tag_relation=intersection&difficulty=20)

````python
import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()
n, m = map(int, input().split())
g = [[0] * m for _ in range(n)]
di = [(0, 1), (0, -1), (1, 0), (-1, 0)]
q = deque()
for i in range(n):
    r = input()
    for j, x in enumerate(r):
        if x == 'g':
            g[i][j] = 1
            q.append((i, j))
k = int(input())
while q and k:
    for _ in range(len(q)):
        x, y = q.popleft()
        for dx, dy in di:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == 0:
                g[nx][ny] = 1
                q.append((nx, ny))
    k -= 1
for row in g:
    print(''.join('g' if x else '.' for x in row))
````

