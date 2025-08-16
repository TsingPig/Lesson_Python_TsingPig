from functools import *
class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(maxsize = None)
        def dfs(n):
            return 1 if n == 1 or n == 0 else dfs(n - 1) + dfs(n - 2)            
        return dfs(n)
s = Solution()
print(s.climbStairs(3)) # 3
