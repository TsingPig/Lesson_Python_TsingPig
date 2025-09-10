from heapq import *

hq = []

heappush(hq, 5)
heappush(hq, 9)
heappush(hq, 11)
heappush(hq, 12)
heappush(hq, 13)
heappush(hq, 15)
print(hq)  # 输出: [5, 9, 11, 12, 13, 15]

# 获取堆顶元素（最小），O(1)
print(hq[0]) # 5

# 弹出堆顶元素（最小），O(logn)
heappop(hq)
print(hq) # 输出 [9, 12, 11, 15, 13]

# 注意：python 中堆默认且只能是小顶堆

# 大顶堆，通过取反实现
nums = [15, 13, 9, 5, 11, 12]
hq = []
for x in nums:
    heappush(hq, -x)
    
print(hq) # [-15, -13, -12, -5, -11, -9]

# 获取堆顶元素（最大）
print(-hq[0]) # 15


# 弹出堆顶元素（最大），O(logn)
heappop(hq) 
print(hq) # [-13, -11, -12, -5, -9]
print(-hq[0]) # 13
