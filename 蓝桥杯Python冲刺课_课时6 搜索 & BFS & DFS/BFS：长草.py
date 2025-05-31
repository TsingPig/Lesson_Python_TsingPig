# https://www.lanqiao.cn/problems/149/learning/?page=1&first_category_id=1&tags=BFS&tag_relation=intersection&difficulty=20
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