# bisect(nums, x, lo = 0, hi = len(nums))
# 在升序nums的[lo, hi)区间中, 返回第一个严格大于x的位置的索引
# 一个bisect()函数通吃

from bisect import *
# 示例数组
#      0  1  2  3  4    5
arr = [1, 9, 9, 9, 200, 500]

# 查找插入位置
print(bisect(arr, 3))  # 输出: 1 (第一个大于 3 的索引)
print(bisect(arr, 1))  # 输出: 1 (第一个大于 1 的索引)
print(bisect(arr, -99))  # 输出: 0 (第一个大于 -99 的索引)
print(bisect(arr, 9)) # 输出: 4 (第一个大于9 的索引)
print(bisect(arr, 7000)) # 输出: 6 (第一个大于7000 的索引，此时等于数组长度)

# 如果需要找第一个大于等于x的位置索引
# bisect(nums, x - 1) ？
print(bisect(arr, 9 - 1))  # 输出: 1 (第一个大于等于 9 的索引)
print(bisect(arr, 200 - 1))  # 输出: 4 (第一个大于等于 200 的索引)

# 逆序数组，找到第一个小于x的位置索引
#      0     1   2  3  4  5
arr = [500, 200, 9, 9, 9, 1]
arr = [-x for x in arr]
print(bisect(arr, -9))  # 输出: 5 (第一个小于 9 的位置索引)