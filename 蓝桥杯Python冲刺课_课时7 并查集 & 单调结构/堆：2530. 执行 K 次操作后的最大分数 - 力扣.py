from heapq import *
from math import *
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        res = 0
        hq = []
        for i, x in enumerate(nums):
            nums[i] = -x
            heappush(hq, (-x, i))
        for _ in range(k):
            x, i = heappop(hq)
            res += x 
            heappush(hq, (-ceil(-x / 3), i))
        return -res


