## 时间复杂度
$$
 O(1): 常数时间  \\
 O(log n): 对数时间 \\
 O(n): 线性时间\\
 O(n log n): 线性对数时间 \\
 O(n^2): 平方时间 \\
 O(2^n): 指数时间\\
$$



## 示例
$O(1)$

```python
def constant_time(n):
    return n + 1
```

$O(log n)$

python

```python
def logarithmic_time(n):
    i = 1
    while i < n:
        i *= 2
```

$O(n)$

python

```python
def linear_time(n):
    for i in range(n):
        pass
```

$O(n log n)$

python

```python
def linearithmic_time(n):
    for i in range(n):
        j = 1
        while j < n:
            j *= 2
```

$O(n^2)$

python

```python
def quadratic_time(n):
    for i in range(n):
        for j in range(n):
            pass
```

$O(2^n)$

python

```python
def exponential_time(n):
    if n <= 1:
        return n
    return exponential_time(n-1) + exponential_time(n-2)
```

## 竞赛技巧

- 优先选择低时间复杂度算法
- 避免嵌套循环
- 使用内置函数（如 `sorted()` 是 O(n log n)）

## 哈希

[1. 两数之和 - 力扣（LeetCode）](https://leetcode.cn/problems/two-sum/?envType=problem-list-v2&envId=o85r8WFa)[1. 两数之和 - 力扣（LeetCode）](https://leetcode.cn/problems/two-sum/?envType=problem-list-v2&envId=o85r8WFa)

给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 和为目标值 *`target`* 的那 两个 整数，并返回它们的数组下标。

示例 1：

```
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
```

提示：

- `2 <= nums.length <= 1e5`
- 只会存在一个有效答案



思路：暴力

```python
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i == j: continue
                if nums[i] + nums[j] == target:
                    return [i, j]
```



```python
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                if i == j: continue
                if x + y == target:
                    return [i, j]
```



```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 前缀哈希
        d = {}
        n = len(nums)
        for i, x in enumerate(nums):
            if d.get(target - x) is not None:
                return [i, d[target - x]]
            d[x] = i

```



## 一维前缀和

问题定义
$$
\begin{aligned}
&对于长度为 n的数组a,给定q组区间[l,r], \\
&对每组区间[l,r]求 \sum_{i=l}^r{a[i]} = a[l] + a[l + 1] + \cdots+a[r],其中 l\le r
\end{aligned}
$$
数据范围

$n \in [1, 10^5], q \in [1, 10^5] $

思路：暴力

- 每次查询显然可以对区间求和，单次最坏复杂度 $O(n)$；

- 总复杂度为 $O(q \times n)$，超时；



算法基础：前缀和

- 预处理前缀和，可前缀和之差，以 $O(1)$ 完成单次区间求和；

- 总复杂度为$O(n)$ 预处理 +  $O(q)$ 询问，即 $O(q + n)$；

$\text{定义: }p[i] = \sum(a[:i]), \\$
$$
\begin{aligned}
则有:
p[0] = \sum(a[:0]) &= 0 \\
p[1] = \sum(a[:1]) &= a[0] \\ 
p[n - 1] = \sum(a[: n - 1]) &= a[0] + ... + a[n - 2] \\ 
p[n] = \sum(a[:n]) &= a[0] + ... + a[n - 2] + a[n - 1] = \sum(a) \\
显然可以发现 p[n] - p[n-1] &= a[n-1] \\
\end{aligned}
$$
即 $p[n] = p[n - 1] + a[n-1],$

即 $p[n + 1] = p[n] + a[n],$

模板

``` python
p = 0 * [n + 1]
for i in range(n):
    p[i + 1] = p[i] + a[i]
```

$a[l] + ... + a[r] = p[r + 1] - p[l]$

[P8218 【深进1.例1】求区间和 - 洛谷 (luogu.com.cn)](https://www.luogu.com.cn/problem/P8218)

```python
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
a = list(map(int, input().split()))
q = int(input())

# 前缀和模板, p[i] = sum(a[:i])
p = [0] * (n + 1)
for i in range(n):
    p[i + 1] = p[i] + a[i]

for _ in range(q):
    l, r = map(int, input().split())
    print(p[r] - p[l - 1])
```

