# https://leetcode.cn/problems/max-area-of-island/description/
from collections import deque    # 这两行在leetcode上不需要
from typing import List
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