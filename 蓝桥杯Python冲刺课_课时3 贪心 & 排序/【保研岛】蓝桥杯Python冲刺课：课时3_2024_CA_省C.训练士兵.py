'''
P10387 [蓝桥杯 2024 省 A] 训练士兵
https://www.luogu.com.cn/problem/P10387
'''
import sys
input = lambda:sys.stdin.readline().strip()
n, S = map(int, input().split())
nums = [[0, 0]] * n # 用于排序
p, c = [0] * n, [0] * n
# 数据预处理
for i in range(n):
    nums[i] = list(map(int, input().split()))
# 排序：根据nums[i][1]即次数排序，默认是由低到高
nums.sort(key = lambda x: x[1])
for i in range(n):
    p[i], c[i] = nums[i][0], nums[i][1]
res = cnt = 0
tot = sum(p)
for i in range(n):
    if tot >= S:    # 团购合适
        res += (c[i] - cnt) * S
        cnt = c[i]
    else:   # 团购不合适，此人单独训练
        res += (c[i] - cnt) * p[i]
    tot -= p[i] # 第i人完成训练，减去他的单独训练成本
print(res)







