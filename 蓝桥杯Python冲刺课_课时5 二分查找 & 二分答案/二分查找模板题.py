from bisect import *
import sys
input = lambda: sys.stdin.readline().strip()
n, m = map(int, input().split())
nums = list(map(int, input().split()))
Q = list(map(int, input().split()))

s = set(nums) # nums构成的集合，如果待查询数组q not in s，直接返回-1
for q in Q:
    if q not in s: print(-1, end = " ")
    else: # q 一定出现在nums中, 利用技巧将“大于等于x”转化成“大于x-1”
        print(bisect(nums, q - 1) + 1, end = " ")
    
