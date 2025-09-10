'''
https://leetcode.cn/problems/two-sum/?envType=problem-list-v2&envId=o85r8WFa
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 前缀哈希
        d = {}
        n = len(nums)
        for i, x in enumerate(nums):
            if d.get(target - x) is not None:
                return [i, d[target - x]]
            d[x] = i
