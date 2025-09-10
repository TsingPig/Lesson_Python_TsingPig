# https://www.luogu.com.cn/problem/P1048
import sys
input = lambda: sys.stdin.readline().strip()

W, N = map(int, input().split())
w, v = [0] * (N + 1), [0] * (N + 1)
for i in range(1, N + 1):
    w[i], v[i] = map(int, input().split())
# f[i][j] 表示在前i个物品中，重量不超过j的所有选择方案的集合中，获得的最大价值
# 最终要求 f[N][W]
f = [[0] * (W + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, W + 1):
        if j - w[i] >= 0: # 可以选i，也可以不选i
            f[i][j] = max(f[i - 1][j], f[i - 1][j - w[i]] + v[i])
        else:
            f[i][j] = f[i - 1][j] # 只能不选i
print(f[N][W])
