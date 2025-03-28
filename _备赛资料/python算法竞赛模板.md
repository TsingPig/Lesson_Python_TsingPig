[TOC]

# 常用数据结构API 

## 1.列表

int 转 list

```python
num = 123
nums = list(map(int, str(num)))
```

list(int) 转 int

```python
nums = [1, 2, 3]
num = int(''.join(map(str, nums)))

def lst_int(nums):
    return int(''.join(map(str, nums)))
```

列表特性

比较大小的时候，不管长度如何，依次比较到第一个元素不相等的位置

比如[1, 2, 3] < [2, 3] 因为在比较1 < 2的时候就终止。

嵌套列表推导：展平二维数组

```python
nums = [e for row in matrix for e in row]
```

## 2.Deque

```python
from collections import deque
list1 = [0, 1, 2, 3]
q=deque(list1)
q.append(4)    # 向右侧加	
q.appendleft(-1)    #向左侧加
q.extend(可迭代元素)    #向右侧添加可迭代元素
q.extendleft(可迭代元素)    
q=q.pop()    #移除最右端并返回元素值
l=q.popleft()    #移除最左端
q.count(1)    #统计元素个数    1
```

```python
# 返回string指定范围中str首次出现的位置
string.index(str, beg=0, end=len(string))
string.index(" ")
list(map(s.index,s))	#返回字符索引数组，如"abcba"->[0,1,2,1,0]
```

## 3.字典

```python
d.pop(key)	#返回key对应的value值，并在字典中删除这个键值对
d.get(key,default_value)	#获取key对应的值，如果不存在返回default_value
d.keys() 	#键构成的可迭代对象
d.values()	#值构成的可迭代对象
d.items()	#键值对构成的可迭代对象
d = defaultdict(list)	# 指定了具有默认值空列表的字典
```

### 字典推导器

字母表对应下标

```python
dic = {chr(i) : i - ord('a') + 1 for i in range(ord('a'), ord('z') + 1)}
```

也可以使用zip初始化dic

[2606. 找到最大开销的子字符串 - 力扣（LeetCode）](https://leetcode.cn/problems/find-the-substring-with-maximum-cost/description/?utm_campaign=lcsocial&utm_medium=article&utm_source=zhihu&utm_content=643258718&utm_term=expertise)

```python
dic = dict(zip(chars, vals))	
for x in s:
	y = dic.get(x, ord(x) - ord('a') + 1)
```

## 4.map映射函数

用法:

```python
map(function, iterable, ...)
```

```python
def square(x) :            # 计算平方数
   return x ** 2

map(square, [1,2,3,4,5])   # 计算列表各个元素的平方
# [1, 4, 9, 16, 25]

map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
# [1, 4, 9, 16, 25]

# 提供了两个列表，对相同位置的列表数据进行相加
map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
# [3, 7, 11, 15, 19]
```

## 5. 自定义Set规则

```python
class MySet(set):
    def add(self, element):
        sorted_element = tuple(sorted(element))
        if not any(sorted_element == e for e in self):
            super().add(sorted_element)
```

```
s = MySet()
s.add((2, 1, 1))
s.add((1, 2, 1))
print(s)  # 输出：{(1, 1, 2)}
```

## 6. 基本输入输出

快读快写

```python
import sys
sys.setrecursionlimit(1000000)
input=lambda:sys.stdin.readline().strip()
write=lambda x:sys.stdout.write(str(x)+'\n')
```

读到文件结尾

```python
import sys

for line in sys.stdin:
    line = line.strip()   					
```

[3701. 非素数个数 - AcWing题库](https://www.acwing.com/problem/content/description/3704/)

```python
import sys
n = 10 ** 7
primes = []
is_prime = [1] * (n + 1)
is_prime[0] = is_prime[1] = 0
for i in range(2, n + 1):
    if is_prime[i]: primes.append(i)
    for p in primes:
        if i * p > n: break
        is_prime[i * p] = 0
        if i % p == 0: break 

a = [0] * (n + 1)
for i in range(2, n + 1):
    a[i] = a[i - 1] + (1 if not is_prime[i] else 0)

for line in sys.stdin:
    input = line.strip()    
    l, r = map(int, input.split())
    print(a[r] - a[l - 1])
```



## 7.优先队列 / 堆

```python
from heapq import heapify, heappop, heappush
    heapify(nums)
    score = heappop(nums)
    heappush(nums, val)
# 注意：
# python中堆默认且只能是小顶堆
```

```python
nums = []
heapq.heappush(nums, val)	#插入
heapq.heappop(nums)			#弹出顶部
```

## 8. 有序列表 / 有序集合

**SortedList** 

```python
from sortedcontainers import SortedList
```

SortedList 相当于 multiset

添加元素：$O(\log ~n)$；`s.add(val)`

添加一组可迭代元素：$O(k \log n)$；`s.upadte(*iterable*)`

查找元素：$O(\log n)$；`s.count(val)`，返回元素的个数

删除元素：$O(\log n)$； $s.remove(val)$

删除指定下标元素：$s.pop(index =- 1)$

```python
class SortedList:
    def __init__(self, iterable=[], _load=200):
        """Initialize sorted list instance."""
        values = sorted(iterable)
        self._len = _len = len(values)
        self._load = _load
        self._lists = _lists = [values[i:i + _load] for i in range(0, _len, _load)]
        self._list_lens = [len(_list) for _list in _lists]
        self._mins = [_list[0] for _list in _lists]
        self._fen_tree = []
        self._rebuild = True
 
    def _fen_build(self):
        """Build a fenwick tree instance."""
        self._fen_tree[:] = self._list_lens
        _fen_tree = self._fen_tree
        for i in range(len(_fen_tree)):
            if i | i + 1 < len(_fen_tree):
                _fen_tree[i | i + 1] += _fen_tree[i]
        self._rebuild = False
 
    def _fen_update(self, index, value):
        """Update `fen_tree[index] += value`."""
        if not self._rebuild:
            _fen_tree = self._fen_tree
            while index < len(_fen_tree):
                _fen_tree[index] += value
                index |= index + 1
 
    def _fen_query(self, end):
        """Return `sum(_fen_tree[:end])`."""
        if self._rebuild:
            self._fen_build()
 
        _fen_tree = self._fen_tree
        x = 0
        while end:
            x += _fen_tree[end - 1]
            end &= end - 1
        return x
 
    def _fen_findkth(self, k):
        """Return a pair of (the largest `idx` such that `sum(_fen_tree[:idx]) <= k`, `k - sum(_fen_tree[:idx])`)."""
        _list_lens = self._list_lens
        if k < _list_lens[0]:
            return 0, k
        if k >= self._len - _list_lens[-1]:
            return len(_list_lens) - 1, k + _list_lens[-1] - self._len
        if self._rebuild:
            self._fen_build()
 
        _fen_tree = self._fen_tree
        idx = -1
        for d in reversed(range(len(_fen_tree).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(_fen_tree) and k >= _fen_tree[right_idx]:
                idx = right_idx
                k -= _fen_tree[idx]
        return idx + 1, k
 
    def _delete(self, pos, idx):
        """Delete value at the given `(pos, idx)`."""
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens
 
        self._len -= 1
        self._fen_update(pos, -1)
        del _lists[pos][idx]
        _list_lens[pos] -= 1
 
        if _list_lens[pos]:
            _mins[pos] = _lists[pos][0]
        else:
            del _lists[pos]
            del _list_lens[pos]
            del _mins[pos]
            self._rebuild = True
 
    def _loc_left(self, value):
        """Return an index pair that corresponds to the first position of `value` in the sorted list."""
        if not self._len:
            return 0, 0
 
        _lists = self._lists
        _mins = self._mins
 
        lo, pos = -1, len(_lists) - 1
        while lo + 1 < pos:
            mi = (lo + pos) >> 1
            if value <= _mins[mi]:
                pos = mi
            else:
                lo = mi
 
        if pos and value <= _lists[pos - 1][-1]:
            pos -= 1
 
        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value <= _list[mi]:
                idx = mi
            else:
                lo = mi
 
        return pos, idx
 
    def _loc_right(self, value):
        """Return an index pair that corresponds to the last position of `value` in the sorted list."""
        if not self._len:
            return 0, 0
 
        _lists = self._lists
        _mins = self._mins
 
        pos, hi = 0, len(_lists)
        while pos + 1 < hi:
            mi = (pos + hi) >> 1
            if value < _mins[mi]:
                hi = mi
            else:
                pos = mi
 
        _list = _lists[pos]
        lo, idx = -1, len(_list)
        while lo + 1 < idx:
            mi = (lo + idx) >> 1
            if value < _list[mi]:
                idx = mi
            else:
                lo = mi
 
        return pos, idx
 
    def add(self, value):
        """Add `value` to sorted list."""
        _load = self._load
        _lists = self._lists
        _mins = self._mins
        _list_lens = self._list_lens
 
        self._len += 1
        if _lists:
            pos, idx = self._loc_right(value)
            self._fen_update(pos, 1)
            _list = _lists[pos]
            _list.insert(idx, value)
            _list_lens[pos] += 1
            _mins[pos] = _list[0]
            if _load + _load < len(_list):
                _lists.insert(pos + 1, _list[_load:])
                _list_lens.insert(pos + 1, len(_list) - _load)
                _mins.insert(pos + 1, _list[_load])
                _list_lens[pos] = _load
                del _list[_load:]
                self._rebuild = True
        else:
            _lists.append([value])
            _mins.append(value)
            _list_lens.append(1)
            self._rebuild = True
 
    def discard(self, value):
        """Remove `value` from sorted list if it is a member."""
        _lists = self._lists
        if _lists:
            pos, idx = self._loc_right(value)
            if idx and _lists[pos][idx - 1] == value:
                self._delete(pos, idx - 1)
 
    def remove(self, value):
        """Remove `value` from sorted list; `value` must be a member."""
        _len = self._len
        self.discard(value)
        if _len == self._len:
            raise ValueError('{0!r} not in list'.format(value))
 
    def pop(self, index=-1):
        """Remove and return value at `index` in sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        value = self._lists[pos][idx]
        self._delete(pos, idx)
        return value
 
    def bisect_left(self, value):
        """Return the first index to insert `value` in the sorted list."""
        pos, idx = self._loc_left(value)
        return self._fen_query(pos) + idx
 
    def bisect_right(self, value):
        """Return the last index to insert `value` in the sorted list."""
        pos, idx = self._loc_right(value)
        return self._fen_query(pos) + idx
 
    def count(self, value):
        """Return number of occurrences of `value` in the sorted list."""
        return self.bisect_right(value) - self.bisect_left(value)
 
    def __len__(self):
        """Return the size of the sorted list."""
        return self._len
 
    def __getitem__(self, index):
        """Lookup value at `index` in sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        return self._lists[pos][idx]
 
    def __delitem__(self, index):
        """Remove value at `index` from sorted list."""
        pos, idx = self._fen_findkth(self._len + index if index < 0 else index)
        self._delete(pos, idx)
 
    def __contains__(self, value):
        """Return true if `value` is an element of the sorted list."""
        _lists = self._lists
        if _lists:
            pos, idx = self._loc_left(value)
            return idx < len(_lists[pos]) and _lists[pos][idx] == value
        return False
 
    def __iter__(self):
        """Return an iterator over the sorted list."""
        return (value for _list in self._lists for value in _list)
 
    def __reversed__(self):
        """Return a reverse iterator over the sorted list."""
        return (value for _list in reversed(self._lists) for value in reversed(_list))
 
    def __repr__(self):
        """Return string representation of sorted list."""
        return 'SortedList({0})'.format(list(self))
  
```



# 字符串

## KMP / 模式匹配

**暴力匹配所有起始位置**

时间复杂度：$O(mn)$

```python
    for i in range(len_s - len_p + 1):
        ii, j = i, 0
        while j < len_p:
            if s[ii] == p[j]: ii, j = ii + 1, j + 1
            else: break
        if j == len_p: res.append(i)
```

**前缀函数 / next数组** 

时间复杂度：$O(n)$，在线算法

对于一个长度为 $n$ 的字符串，其前缀函数是一个长度为 $n$ 的数组 $\pi$，其中 $\pi(i)$ 定义：子串 $s[0] \sim s[i]$ 中存在的、相等的最长真前缀和真后缀的长度。如果不存在则为0。规定：$\pi[0]=0$，因为其不存在真前后缀。

> 例如：'aabaaab' 的 $\pi$ 数组为 [0, 1, 0, 1, 2, 2, 3]

求解前缀函数：

- 相邻的前缀函数值，至多 + 1。$\pi(i-1)$表示着前一个状态匹配的最长真前后缀，也是下一个待匹配真前缀的最右元素下标。当且仅当 $s[i]=s[\pi(i-1)]$，有$\pi(i) = \pi(i-1)+1$ 。
- 考虑 $s[i] \ne s[\pi(i-1)]$，失配时，希望找到 $s[0] \sim s[i-1]$ 中，仅次于 $\pi[i-1]$ 的第二长度 $j$，使得在位置 $i-1$ 的前后缀性质仍然保持，即  $s[0] \sim s[j-1] = s[i-j] \sim s[i-1]$。

​		实际上，第二长真后缀也完整存在于 当前真前缀 $s[0] \sim s[j-1]$ 中，即有转移方程：$j^{(n-1)}=\pi(j^n-1)$。所以如此往复，要么直到 $s[i]=s[j'] $ ，然后转移到第一种情况；要么直到 $j'=0$ 。两种情况，通过判断 $s[i] $ 是否 $s[j']$ 来确定要不要让 $j'+1$ 统一，最后 $s[i]=s[j']$。

![image.png](https://pic.leetcode.cn/1712915633-ojIXWM-image.png)

```python
def get_pi(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1] 
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]: j += 1
        pi[i] = j
    return pi
```

**KMP算法：找出 $p$ 在 $s$ 中的所有出现**

时间复杂度：$O(n+m)$，其中 $m=len(p),~n=len(s)$

构造字符串 $t=p\#s$，计算其前缀函数 $\pi$。考虑前缀函数 $\pi[m+1]\sim \pi[n+m]$，其中 $\pi(i)=m $ 的地方，一定完成对模式串 $p$ 的匹配。此时，$i$ 位于 $t $  中$s$ 的最后位置，所以原始位置为 $i-m+1-m-1 = i - 2 * m$。

```python
def kmp(p, s):
    res = []
    m, n = len(p), len(s)
    pi = get_pi(p + '#' + s)
    for i in range(m + 1, len(pi)):
        if pi[i] == m: res.append(i - 2 * m)
    return res
```



## 字符串排序

```python
sorted(str) #返回按照字典序排序后的列表，如"eda"->['a','d','e']
s_sorted=''.join(sorted(str))	#把字符串列表组合成一个完整的字符串
```



## Z函数 (扩展KMP)

对于字符串s，函数$z[i]$ 表示 $s$ 和 $s[i:]$ 的最长公共前缀$(LCP)$的长度。特别的，定义$z[0] = 0$。即 
$$
z[i] = len(LCP(s,s[i:]))
$$

> 例如， $z(abacaba) = [0, 0, 1, 0, 3, 0, 1]$

[可视化：Z Algorithm (JavaScript Demo) (utdallas.edu)](https://personal.utdallas.edu/~besp/demo/John2010/z-algorithm.htm)

```python
# s = 'aabcaabxaaaz'
n = len(s)
z = [0] * n
l = r = 0
for i in range(1, n):
    if i <= r:  # 在Z-box范围内
        z[i] = min(z[i - l], r - i + 1)
    while i + z[i] < n and s[z[i]] == s[i + z[i]]:
        l, r = i, i + z[i]
        z[i] += 1
# print(z) # [0, 1, 0, 0, 3, 1, 0, 0, 2, 2, 1, 0]
```

## 判断子序列

判断 p 在删除ss中下标元素后，是否仍然满足s 是 p 的子序列。

> ```
> 例如：
> s = "abcacb", p = "ab", removable[:2] = [3, 1]
> 解释：在移除下标 3 和 1 对应的字符后，"abcacb" 变成 "accb" 。
> "ab" 是 "accb" 的一个子序列。
> ```

```python
    ss = set(removable[:x])
    i = j = 0
    n, m = len(s), len(p)
    while i < n and j < m:
        if i not in ss and s[i] == p[j]:
            j += 1
        i += 1
     return j == m
```

## 字符串哈希

[49. 字母异位词分组 - 力扣（LeetCode）](https://leetcode.cn/problems/group-anagrams/description/)

[2430. 对字母串可执行的最大删除数 - 力扣（LeetCode）](https://leetcode.cn/problems/maximum-deletions-on-a-string/description/)

## 字符串API

- s1.startswith(s2, beg = 0, end = len(s2))

  用于检查字符串s1 是否以字符串 s2开头。是则返回True。如果指定beg 和 end，则在s1[beg: end] 范围内查找。

- 使用 ascii_lowercase遍历26个字母。

  ```python
  from string import ascii_lowercase
  cnt = {ch: 0 for ch in ascii_lowercase}
  ```

  

# 区间问题

## 区间选点问题 / 最大不相交区间数量

- **射气球问题**：给定 $n$ 个气球，用区间表示，选出最少的弓箭将所有气球都能射爆。

- **区间选点问题**：给定 $n$ 个区间，选出最少的点使得每个区间至少包含1个点。

- **最大不相交区间问题**：给定 $n$ 个区间，选出最多的区间，使得区间两两不相交（含端点）。

这几个问题是等价的，最大不相交区间问题中，将区间集合 $U$ 划分成两两不相交的最多的区间集合 $S$ 和 $U-S$ 。任意 $U-S$ 中区间一定和 $S$ 中的区间相交，它们不需要额外占用更多的选点，因此 $|S|$ 就等于最少的弓箭数量、选点数量。

对于 $mxr$ ，考察 $l, r$ 一共有三种情况：

- $mxr <l$，区间个数加一，$mxr = r$

- $l \le mxr <r$，不变
- $r \le mxr$，$mxr =r$

综上，只需要在 $l > mxr$ 时，更新$res, mxr$，否则在 $r < mxr$ 时，更新 $mxr$ 。

复杂度：$O(n)$

[452. 用最少数量的箭引爆气球 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/description/)

[905. 区间选点 - AcWing题库](https://www.acwing.com/problem/content/907/)

[908. 最大不相交区间数量 - AcWing题库](https://www.acwing.com/problem/content/910/)

```python
def solve(nums):
    nums.sort()
    mxr = -inf 
    res = 0
    for l, r in nums:
        if l > mxr:
            res, mxr = res + 1, r
		elif r < mxr:
            mxr = r
        # 或者mxr = min(mxr, r)
    return res 
```

## 区间分组

给定 $n$ 个区间，要求将其分成最少的组，每个组各个区间之间两两不相交（含端点）。

维护所有分组的 $mxr$，对于 $mxr_{\min}$ ，考察 $l$ 与之关系。

- $l > mxr_{\min}$，可以放在这个分组中
- $l \le mxr_{\min}$，需要开辟一个新的分组，最右端点是 $r$ 。

时间复杂度：$O(n \log n)$

[906. 区间分组 - AcWing题库](https://www.acwing.com/problem/content/908/)

```python
def solve(nums):
    nums.sort()
    hq = []
    for l, r in nums:
        if hq and l > hq[0]:
            heappop(hq)
        heappush(hq, r)
    return len(hq)
```

## 区间覆盖

给定 $n$ 个区间和 一个需要覆盖的线段区间 $[L, R]$，找出最少的区间使它们完全覆盖线段区间 $[L,R]$；如果无法完成输出 -1。

[907. 区间覆盖 - AcWing题库](https://www.acwing.com/problem/content/909/)

考察当前已经覆盖到的最远端 $mxr$ ，考察所有 $l \le mxr$，如果第一个 $l > mxr$，无法覆盖线段区间 $[mxr+1,]$记录这些区间的最远右端点 $nmxr$，然后更新 $mxr$ 。一旦超过 $R$ 表示完成覆盖。

```python
def solve(L, R, nums):
    n = len(nums)
    nums.sort()
    mxr = L
    i = res = 0
    while i < n:
        l, r = nums[i]
        if l > mxr: return -1
        nmxr = r
        while i + 1 < n and nums[i + 1][0] <= mxr:
            nmxr = max(nmxr, nums[i + 1][1])
            i += 1
        res += 1
        mxr = nmxr 
        if mxr >= R: return res 
        i += 1
    return -1    
```



## 合并区间

先排序。

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        l, r = intervals[0][0], intervals[0][1]
        for interval in intervals:
            il, ir = interval[0], interval[1]
            if il > r:
                res.append([l, r])
                l = il
            r = max(r, ir)
        res.append([l, r])
        return res
```

[2580. 统计将重叠区间合并成组的方案数 - 力扣（LeetCode）](https://leetcode.cn/problems/count-ways-to-group-overlapping-ranges/description/?envType=daily-question&envId=2024-03-27)

```python
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort(key = lambda x: x[0])
        l, r = ranges[0][0], ranges[0][1]
        nranges = []
        for il, ir in ranges:
            if il > r:
                nranges.append([l, r])
                l = il 
            r = max(ir, r)
```

## 区间交集

[Problem - C - Codeforces](https://codeforces.com/contest/1304/problem/C)

$Lo,Hi$ 记录当前可变温度区间。每次来到新时刻，更新为 $[Lo-dt,~Hi+dt]$。判断该区间是否和当前 $[lo, hi]$ 相交。是则求其交集。

```python
def solve():
    n, m = map(int, input().split())
    tem = [(0, m, m)]
    for _ in range(n):
        at, lo, hi = map(int, input().split())
        tem.append((at, lo, hi))
    Lo = Hi = m
    for i in range(1, n + 1):
        at, lo, hi = tem[i]
        dt = at - tem[i - 1][0]
        
        Lo, Hi = Lo - dt, Hi + dt
        if Lo > hi or Hi < lo: return 'NO'
        Lo, Hi = max(Lo, lo), min(Hi, hi)
    return 'YES'
```



# 回溯 / 递归 / dfs / 分治

## 子集型回溯

**枚举子集，$O(n\cdot2^n)$**

[78. 子集 - 力扣（LeetCode）](https://leetcode.cn/problems/subsets/description/?envType=featured-list&envId=L2JxWeVS?envType=featured-list&envId=L2JxWeVS)

回溯方法1：选  / 不选

```python
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, path = [], []
        def dfs(i):
            if i == n: 
                res.append(path.copy())
                return 
            path.append(nums[i])
            dfs(i + 1)
            path.pop()
            dfs(i + 1)
        dfs(0)
        return res
```

方回溯法2：枚举选哪个数 + 记录可以选的范围

$dfs(i)$  表示当前已经有选择了 $path$ 后，$path$ 下一个元素可以从 $i$ 及其往后选。每一个 $dfs$ 状态都是合法状态，需要记录。

```python
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, path = [], []
        n = len(nums)
        def dfs(i):
            res.append(path.copy())
            for j in range(i, n):
                path.append(nums[j])
                dfs(j + 1)
                path.pop()
        dfs(0)
        return res
```

位运算写法：

```python
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        s = (1 << n) - 1
        res = [[]]
        sub = s
        while sub:
            res.append([nums[j] for j in range(n) if ((sub >> j) & 1)])
            sub = (sub - 1) & s
        return res
```



## 组合型回溯

**枚举所有长度为 $k$ 的组合**

[77. 组合 - 力扣（LeetCode）](https://leetcode.cn/problems/combinations/description/?envType=featured-list&envId=L2JxWeVS?envType=featured-list&envId=L2JxWeVS)

回溯方法1：选 / 不选方法

> 时间复杂度 ：$O(n \cdot2^n)$

```python
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n + 1))
        res, path = [], []
        def dfs(i):
            if i == n:
                if len(path) == k: res.append(path.copy())
                return 
            # 不选
            dfs(i + 1)
            # 选
            path.append(nums[i])
            dfs(i + 1)
            path.pop()
        dfs(0)
        return res
```

回溯方法2：枚举当前选哪个数，以及记录可以选择的范围，每一个状态的合法情况需要记录。

剪枝操作 (1)：确保所有子集长度不会超过 $k$。剪枝操作 (2) ：要确保枚举当前选择的数的位置，不会使得最终整个子集长度达不到 $k$ 。通过两个剪枝操作，确保只会得到长度恰好为 $k$ 的子集。这里倒序 / 正序枚举在当前选择的数的范围影响下界 / 上界。

倒序枚举时， $dfs(i)$  表示当前选择范围为 $nums[0] \sim nums[i]$，含有 $i+1$ 个数。由于下一个状态是 $j-1$，含有$ j$ 个数，根据 $j \ge k - len(path)-1$ 计算下界。

> 时间复杂度：$O(k \cdot C(n,k))$。因为总共组合状态个数有 $C(n,k)$个，每个状态记录的长度不超过$k$ 。

```python
# 倒叙枚举
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n + 1))
        res, path = [], []
        def dfs(i):
            if k == len(path):
                res.append(path.copy())
                return
            for j in range(i, k - len(path) - 2, -1):
                path.append(nums[j])
                dfs(j - 1)
                path.pop()
        dfs(n - 1)
        return res
```

位运算写法 + Gosper's Hack：

> 时间复杂度：$O(n \cdot C(n,k))$

```python
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n + 1))
        s = (1 << n) - 1
        sub = (1 << k) - 1
        res = []
        def next_sub(x):
            lb = x & -x
            left = x + lb 
            right = ((left ^ x) >> 2) // lb
            return left | right 
        while sub <= s:
            res.append([nums[i] for i in range(n) if (sub >> i) & 1])
            sub = next_sub(sub)
        return res
```

**完全背包型组合**

每个元素可以无限重复选择，需要找出目标值等于 $target$ （或小于等于 $target$ ）的所有可行组合。

先排序，利于提前剪枝优化跳出循环。枚举当前选哪个 + 记录可以选择的范围型回溯，记录当前的和。由于可以重复选择，所以当前选择 $j$  以后，下一次的可以选择范围仍然是 $j$。

[39. 组合总和 - 力扣（LeetCode）](https://leetcode.cn/problems/combination-sum/description/?envType=daily-question&envId=2024-04-20)

```python
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n, res, path = len(candidates), [], []
        # 枚举当前选哪个，以及记录可以选择的范围；以及当前的和
        def dfs(i, s):
            if s == target:
                res.append(path.copy())
                return 
            for j in range(i, n):
                x = candidates[j]
                if x + s <= target:
                    path.append(x)
                    dfs(j, s + x)	# 体现可重复选择
                    path.pop()
                else: break
        dfs(0, 0)
        return res
```



**括号生成问题：带限制组合型回溯**

[22. 括号生成 - 力扣（LeetCode）](https://leetcode.cn/problems/generate-parentheses/description/?envType=featured-list&envId=L2JxWeVS?envType=featured-list&envId=L2JxWeVS)

选 / 不选型回溯：枚举当前左 / 右括号，记录当前左括号的个数。记 $lc$ 表示左括号个数， $rc$ 表示右括号个数。

限制1：$lc$ 不能小于 $rc$。

限制2：$lc $ 不能超过 $n/2$。

限制3：当 $lc=rc$，只能回溯左括号。

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 枚举当前左 / 右括号，记录当前左括号的个数
        n <<= 1
        path = [None] * n
        res = []
        def dfs(i, lc):
            rc = i - lc
            if rc > lc or lc > n // 2: return 
            if i == n:
                res.append(''.join(path))
                return 
            path[i] = '('
            dfs(i + 1, lc + 1)
            if rc < lc:  # 可以选右
                path[i] = ')'
                dfs(i + 1, lc)
        dfs(0, 0)
        return res
```

> 时间复杂度：由于状态个数是卡特兰数列，即 $O(C_n) \sim O(\frac{4^n}{n^{\frac{3}{2}} \cdot\sqrt \pi})$

## 排列型回溯

**全排列：排列元素无重复**

[46. 全排列 - 力扣（LeetCode）](https://leetcode.cn/problems/permutations/description/)

写法1：$dfs(i, S)$ 表示枚举到 第 $i$ 位，没有枚举过的集合为 $S$。外层 $path$ 表示当前回溯的路径。

其中 $path$ 可以使用 $path[i] = j$ 的写法，覆盖当前走到哪一步；也可以使用 $append / pop$ 写法，覆盖和恢复现场。但是不可以在外层增加哈希集合维护没有枚举过的，这是因为集合添加操作的乱序性，外层的集合无法正确恢复现场（恢复后遍历顺序不正确）。

时间复杂度：当有 $N$ 个数时，所有状态个数 $M = A_N^N+A_N^{N-1}+~\cdots~+A_N^0=\sum_{k=0}^{N}\frac{N!}{k!} =N! \cdot \sum_{k=0}^{N}\frac{1}{k!}= e\cdot N!$。（麦克劳林展开）。每个状态时间复杂度，可以将集合的复制下方到下一个状态，所以是 $O(n)$。故总复杂度：$O(N \cdot N!)$

```python
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = [0] * n 
        res = []
        # 当前枚举到 位置 i，没有枚举过的集合为 S
        def dfs(i, S):
            if i == n:
                res.append(path.copy())    
                return 
            for j in S:
                path[i] = j
                dfs(i + 1, S - {j})
        dfs(0, set(nums))
        return res
```

写法2：更偏向于回溯。外层$path$ 表示当前回溯的路径，外层 $on\_path$ 维护节点是否已经出现在回溯的路径中。

```python
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        path = []
        on_path = [False] * n
        res = []
        # 当前枚举到 位置 i，on_path 记录是否已经出现在回溯路径path中
        def dfs(i):
            if i == n:
                res.append(path.copy())    
                return 
            for pj, on in enumerate(on_path):
                if not on:
                    on_path[pj] = True
                    path.append(nums[pj])
                    dfs(i + 1)
                    on_path[pj] = False
                    path.pop()
        dfs(0)
        return res
            
```

**全排列：排列元素有重复：只能用$on\_path$ 回溯 / 位运算压缩**

[47. 全排列 II - 力扣（LeetCode）](https://leetcode.cn/problems/permutations-ii/description/)

相同元素，在 $i$处视为一个，加一个集合维护已经出现过的数字。

```python
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n, res = len(nums), []
        path, on_path = [0] * n, [0] * n
        def dfs(i):
            if i == n:
                res.append(path.copy())
                return 
            S = set()       # 相同元素，在i 处视为一个
            for j, on in enumerate(on_path):
                if not on and nums[j] not in S:
                    S.add(nums[j])
                    path[i] = nums[j]
                    on_path[j] = 1
                    dfs(i + 1)
                    on_path[j] = 0
        dfs(0)
        return res
```

[996. 正方形数组的数目 - 力扣（LeetCode）](https://leetcode.cn/problems/number-of-squareful-arrays/?envType=featured-list&envId=ptud3zoQ?envType=featured-list&envId=ptud3zoQ)

相同值的排列视为同一个：在枚举 $i$ 位置放谁的时候加一个集合维护已经出现过的数字。

```python
    def numSquarefulPerms(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        def is_sqr(x):
            return x == int(sqrt(x)) ** 2
        def dfs(i, S, pre):
            nonlocal res 
            if i == n: 
                res += 1
                return 
            # i 位置放谁
            s = set()
            for j in range(n):
                x = nums[j]
                if (S >> j) & 1 == 1 or x in s: continue 
                s.add(x)
                if pre == None or is_sqr(pre + x):
                    dfs(i + 1, S | (1 << j), x)
        dfs(0, 0, None)
        return res 
```



[2850. 将石头分散到网格图的最少移动次数 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-moves-to-spread-stones-over-grid/description/)

暴力枚举可重复全排列匹配 + 位运算压缩。用石头个数大于1 和 没有石头的位置，构造两个列表，进行全排列暴力匹配。

```python
def minimumMoves(self, grid: List[List[int]]) -> int:
        frm, to = [], []
        for i, row in enumerate(grid):
            for j, x in enumerate(grid[i]):
                if x == 0: to.append((i, j))
                elif x > 1: frm.extend((i, j) for _ in range(x - 1))
        res = inf 
        n = len(frm)
        path = [None] * n
        def dfs(i, S):
            nonlocal res
            if i == n:
                cst = sum(abs(x1 - x2) + abs(y1 - y2) for (x1, y1), (x2, y2) in zip(path, to))
                res = min(res, cst)
                return 
            for j in range(n):
                if (S >> j) & 1:
                    path[i] = frm[j]
                    dfs(i + 1, S ^ (1 << j))
        dfs(0, (1 << n ) - 1)
        return res

```



**N皇后问题**

皇后之间不同行，不同列，且不能在同一斜线。如果只满足不同行不同列，等价于每行每列恰好一个皇后。如果用 $col$ 表示皇后的位置，$col[i]$ 表示 第 $i$ 行的皇后在第$col[i]$ 列，则 "每行每列恰好一个皇后" 等价于 枚举 $col$ 的全排列。

加上斜线上不能有皇后的条件，如果从上往下枚举，则左上方向、右上方向不能有皇后。所以问题变成，当前枚举到 第 $i$ 行，可以枚举的列号的集合 $S$ 。枚举列$j \in S$ ，合法情况即在 $\forall r \in [0 ,~ i-1]$ ，其列值 $c = col[r]$ 都不满足 $i+j=r+c$ 或者 $i-j=r-c$。

![image.png](https://pic.leetcode.cn/1712744334-oWlDrA-image.png)

写法1：$ dfs(i, S)$ 枚举当前到第 $i$ 行（选第$i$ 个数），可以选择的列号的集合是 $S$ （没选择过的数字集合S）

```python
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        path = [0] * n
        # 当前枚举到第 i 行，可以继续枚举的列号集合是 S
        def valid(i, j):
            for r in range(i):
                c = path[r]
                if r + c == i + j or r - c == i - j:
                    return False 
            return True
        def dfs(i, S):
            if i == n:
                res.append(['.' * j + 'Q' + (n - j - 1) * '.' for j in path])
                return 
            for j in S:
                if valid(i, j):
                    path[i] = j
                    dfs(i + 1, S - {j})
        dfs(0, set(range(n)))
        return res
```

写法2：回溯全排列 + 位运算 + 集合优化$O(1)$ 判断斜线方向

由于判断 $i+j$ 和 $i - j$ 是否在之前回溯中出现过需要$O(n)$的时间，实际上只需要用集合记录出现过的 $i+j$ 和 $i - j$ 即可。对于出现过$i+j$ 和 $i-j$ 分别（防止相互干扰）放进集合 $lu$ 和$ru$ 中（由于 位运算中 $i-j$ 可能出现负值，所以存放的元素改成 $i-j+10$）。

```python
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        path = [0] * n
        lu = ru = 0
        # 当前枚举到第 i 行，可以继续枚举的列号集合是 S
        def dfs(i, S):
            nonlocal lu, ru
            if i == n:
                res.append(['.' * j + 'Q' + (n - j - 1) * '.' for j in path])
                return 
            for j in range(n):
                if (S >> j) & 1 and (lu >> (i + j)) & 1 == 0 and (ru >> (i - j + 10)) & 1 == 0:
                        path[i] = j
                        lu, ru = lu | (1 << (i + j)), ru | (1 << (i - j + 10))
                        dfs(i + 1, S & ~(1 << j))
                        lu, ru = lu ^ (1 << (i + j)), ru ^ (1 << (i - j + 10))
        dfs(0, (1 << n) - 1)
        return res
```

## 回溯分割字符串

记录当前切割到的位置，枚举下一个切割位置，判断切割合法性。

[LCR 086. 分割回文串 - 力扣（LeetCode）](https://leetcode.cn/problems/M99OJA/)

```python
    def partition(self, s: str) -> List[List[str]]:
        n, path, res = len(s), [], []
        # 当前分割的位置，枚举下次分割位置
        def dfs(i):
            if i == n:
                res.append(path.copy())
                return 
            for j in range(i + 1, n + 1):
                t = s[i: j]
                if t == t[::-1]:
                    path.append(t)
                    dfs(j)
                    path.pop()
        dfs(0)
        return res 
```

[93. 复原 IP 地址 - 力扣（LeetCode）](https://leetcode.cn/problems/restore-ip-addresses/description/?envType=featured-list&envId=L2JxWeVS?envType=featured-list&envId=L2JxWeVS)

增加了字符串段数限制：恰好等于4。时间复杂度：$O(n \times C(n,3))$

```python
    def restoreIpAddresses(self, s: str) -> List[str]:
        n, path, res = len(s), [], []
        # 记录当前分割位置，枚举下一个分割位置
        def dfs(i):
            if len(path) == 4:
                if i == n:
                    res.append('.'.join(path))
                return 
            for j in range(i + 1, n + 1):
                t = s[i: j]
                if t == '0' or '0' not in t[0] and int(t) <= 255:
                    path.append(t)
                    dfs(j)
                    path.pop()
        dfs(0)
        return res
```

[2698. 求一个整数的惩罚数 - 力扣（LeetCode）](https://leetcode.cn/problems/find-the-punishment-number-of-an-integer/description/?envType=featured-list&envId=L2JxWeVS?envType=featured-list&envId=L2JxWeVS)

判断一个数，其平方是否可能划分成若干字符串，其各段对应数字之和等于本身。例如 $36\times36=1296,1+29+6=36$

```python
    def check(x):
        sx = str(x * x)
        n = len(sx)
        def dfs(i, s):
            if i == n: return s == x
            t = 0
            for j in range(i + 1, n + 1):
                t = t * 10 + int(sx[j - 1])
                if t + s <= x and dfs(j, s + t):
                    return True
            return False 
        return dfs(0, 0)
```

## 分治

[395. 至少有 K 个重复字符的最长子串 - 力扣（LeetCode）](https://leetcode.cn/problems/longest-substring-with-at-least-k-repeating-characters/description/)

$f(s)$ 表示字符串s 中所有字符不少于 $k$ 个的子串中的最大长度。考察所有在当前 $s$ 串中出现次数少于 $k$ 的字符（记作分割字符），最终最大串肯定不包含之。因此，每一层递归，以找到的第一个分割字符作为隔板，将 $s$ 分成 若干个小的子串，取其中最大值即可。

时间复杂度：$O(26N)$，这是由于每一层递归必然完全删除一个小写字母，且每一层需要遍历整个字符串，时间复杂度是$O(N)$；所以总复杂度是 $O(26N)$。

```python
    def longestSubstring(self, s1: str, k: int) -> int:
        # s1中所有字符数量 >= k 个最长子串
        def f(s1):
            cnt = Counter(s1)
            for ch, c in cnt.items():
                if c < k:
                    return max(f(sub) for sub in s1.split(ch))
            return len(s1)
        return f(s1)
```



[1763. 最长的美好子字符串 - 力扣（LeetCode）](https://leetcode.cn/problems/longest-nice-substring/description/)

$f(s)$ 表示字符串 $s$ 中所有字符出现大小写的最长子串。以 $s1$ 中只出现大写 / 小写的字母作为分割点，将问题分治，返回最大长度中出现最早的字符串。时间复杂度：$O(26 \times n)$，因为每一层需要 $O(n)$ 的复杂度，每一层递归至少减少一个字符。

```python
from collections import *
from string import ascii_lowercase, ascii_uppercase 
L, U = ascii_lowercase, ascii_uppercase 
def f(s1):
    s = set(s1)
    for l, u in zip(L, U):
        if (l in s) != (u in s):
            ss = s1.split(l if l in s else u)
            res = ''
            for sub in ss:
                cur = f(sub)
                if len(cur) > len(res): res = cur 
            return res 
    return s1

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        return f(s)
```



# 排序

**次最值问题**

[1289. 下降路径最小和 II - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-falling-path-sum-ii/description/?envType=featured-list&envId=DuoJVDZI?envType=featured-list&envId=DuoJVDZI)

其中需要维护上一层的最小值、次小值及其对应的坐标。

```python
	mn = mn_2 = (inf, -1)
	if y < mn[0]: mn_2, mn = mn, (y, j)
    elif y == mn[0]: mn_2 = (y, j)
    elif y < mn_2[0]: mn_2 = (y, j)       
```



## 计数排序

**带修求第 $k$ 小 / 大的数**

使用哈希表维护每个数值出现次数，适用于数值的值域较小的情况。

例如：当 $nums[i] \in [a,~b]$，可以在 $O(b-a)$ 的时间复杂度内，找出第 $k$ 大的数（有时表现会比 SortedList更好）。

```python
def get_min_k(cnt, k):
    cur = 0
    for x in range(a, b):
        if cnt[x] == 0: continue 
        cur += cnt[x]
        if cur >= k: return x
    return b
```



[2653. 滑动子数组的美丽值 - 力扣（LeetCode）](https://leetcode.cn/problems/sliding-subarray-beauty/description/?envType=featured-list&envId=DMKTNBLj?envType=featured-list&envId=DMKTNBLj)

定长滑动窗口 + 哈希维护计数 + 计数排序。时间复杂度：$O(nU),U$ 是值域极差。

```python
     def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        cnt = Counter(nums[:k])
        def get_min_k():
            cur = 0
            for y in range(-50, 0):
                cur += cnt[y]
                if cur >= x: return y
            return 0
        res = [get_min_k()]
        for r in range(k, n):
            nl, nr = nums[r - k], nums[r]
            cnt[nr] += 1
            cnt[nl] -= 1
            if cnt[nl] == 0: cnt.pop(nl)
            res.append(get_min_k())
        return res 
```



# 离散化

二分写法

```python
sorted_nums = sorted(set(nums))
nums = [bisect.bisect_left(sorted_nums, x) + 1 for x in nums]
```

字典写法

```python
    sorted_nums = sorted(set(nums))
    mp = {x: i + 1 for i, x in enumerate(sorted_nums)}
    nums = [mp[x] for x in nums]
```

二分 + 还原

```python
tmp = nums.copy()
sorted_nums = sorted(set(nums))
nums = [bisect.bisect_left(sorted_nums, x) + 1 for x in nums]
mp_rev = {i: x for i, x in zip(nums, tmp)}
```



# 二分查找

```python
from bisect import *
l = [1,1,1,3,3,3,4,4,4,5,5,5,8,9,10,10]
print(len(l)) # 16

print(bisect(l, 10))     # 相当于upper_bound, 16
print(bisect_right(l, 10))    # 16

print(bisect_left(l, 10)) # 14
```

## 多维二分

```python
a = [(1, 20), (2, 19), (4, 15), (7,12)]
idx = bisect_left(a, (2, )) # 1
```

## 二分答案

**正难则反思想**，二分答案一般满足两个条件：

- 当发现问需要的最少/最多时间时
- 答案具有单调性。例如问最少的时候，你发现取值越大越容易满足条件。

check(x) 函数对单调x 进行检验。

```python
y = 27
def check(x):
    if x > y:
        return True
    return False
left = a
res = left + bisect.bisect_left(range(left, mx), True, key = check))
```

[3048. 标记所有下标的最早秒数 I - 力扣（LeetCode）](https://leetcode.cn/problems/earliest-second-to-mark-indices-i/description/)

**求“至少”问题**

```python
n, m = len(nums), len(changeIndices)
def check(mx):  # 给mx天是否能顺利考完试
    last_day = [-1] * n 
    for i, x in enumerate(changeIndices[:mx]):
        last_day[x - 1] = i + 1
    #如果给mx不能完成，等价于有为i遍历到考试日期的考试
    if -1 in last_day:
        return False
    less_day = 0
    for i, x in enumerate(changeIndices[:mx]):
        if last_day[x - 1] == i + 1: # 到了考试日期
            if less_day >= nums[x - 1]:
                less_day -= nums[x - 1]
                less_day -= 1   #抵消当天不能复习
            else:
                return False   #寄了
        less_day += 1
    return True
left = sum(nums) + n # 至少需要的天数, 也是二分的左边界
res = left + bisect.bisect_left(range(left, m + 1), True, key = check)
return -1 if res > m else res
```

**求“最多”问题**

[1642. 可以到达的最远建筑 - 力扣（LeetCode）](https://leetcode.cn/problems/furthest-building-you-can-reach/)

```python
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        d = [max(0, heights[i + 1] - heights[i]) for i in range(n - 1)]
        def check(x):
            t = d[:x]
            t.sort(reverse = True)
            return not (ladders >= x or sum(t[ladders: ]) <= bricks)
        return bisect.bisect_left(range(n), True, key = check) - 1
```

**中位数转化为第 $k$ 小问题**

对于一个长度为 $n$ 的 由于数组，求中位数等价于求数组中第 $\frac{n-1}{2}$ 小的数问题（广义中位数）。

[3134. 找出唯一性数组的中位数 - 力扣（LeetCode）](https://leetcode.cn/problems/find-the-median-of-the-uniqueness-array/description/)

一共有 $(n + 1) \times  n / 2$ 个子数组，其对应的 $f=len (set(sub))$ 的值按照升序排列后，求其中位数。即转换为求数组中 第 $k$ 小问题。

转换为二分查找：给定一个 $x$ ，能得出所有子数组中 $f$ 值小于等于 $x$ 的个数 $res$；可以发现 $x$ 越大，$res$ 越大；因此找到恰好让$res >k$ 的位置即可。这里需要使用到求**“不同元素个数小于等于 $k$ 的子数组个数”** 问题，这是一共广义上不定长滑动窗口问题。

```python
def get_set_subarrays_lower_k(nums, k):
    l = res = 0
    freq = Counter()
    for r, x in enumerate(nums):
        freq[x] += 1
        while len(freq) > k:
            freq[nums[l]] -= 1
            if freq[nums[l]] == 0: freq.pop(nums[l])
            l += 1
        res += r - l + 1
    return res 
class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        m = ((n + 1) * n // 2 - 1) // 2
        lo, hi = 0, n // 2 + 10
        while lo < hi:
            mid = (lo + hi) // 2
            if get_set_subarrays_lower_k(nums, mid) > m:
                hi = mid
            else:
                lo = mid + 1 
        return lo

```



## 朴素二分

在 闭区间[a, b]上二分

```python
    lo, hi = a, b 	# [a, b]
    while lo < hi:
        mid = (lo + hi) // 2
        if check(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

**实现bisect_left**

注意：查找范围为$[lo, hi]$；当 $x>max(nums[lo:hi +1])$  时，结果 $lo$ 值 等于 $hi$ 。

$bisect\_left(nums, x + 1, lo, hi)-1$ 查找闭区间$[lo,hi]$内，恰好大于 $x$ 的首个位置。如果不存在时，$lo = hi$ ，注意需要特判。

当$hi = n$ 时，兼容了存在和不存在两种情况。当不存在时，$lo=n$。

```python
def bisect_left(nums, x, lo, hi):
    def check(pos):
        return nums[pos] >= x
    while lo < hi:
        # 查找恰好比x大于等于的位置
        mid = (lo + hi) >> 1
        if check(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
print(bisect_left(nums, val, 0, len(nums)))
```

[2563. 统计公平数对的数目 - 力扣（LeetCode）](https://leetcode.cn/problems/count-the-number-of-fair-pairs/description/)同 [Problem - 1538C - Codeforces](https://codeforces.com/problemset/problem/1538/C)

```python
def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        L, R = lower, upper
        def bisect_left1(nums, x, lo, hi):
            while lo < hi:
                mid = (lo + hi) >> 1
                if nums[mid] >= x:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        for i, x in enumerate(nums):
            res += bisect_left1(nums, R - x + 1, i + 1, n) - 1 -  bisect_left1(nums, L - x, i + 1, n) + 1
        return res
```





## 自定义比较规则

```python
class node():
    def __init__(self, need, get, idx):
        self.need = need
        self.get = get
        self.idx = idx
    def __lt__(self, other):
        return self.need < other.need
```



# 滑动窗口

## 定长滑动窗口

**维护定长滑动窗口和**

[1343. 大小为 K 且平均值大于等于阈值的子数组数目 - 力扣（LeetCode）](https://leetcode.cn/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/?envType=featured-list&envId=DMKTNBLj?envType=featured-list&envId=DMKTNBLj)

```python
    def numOfSubarrays(self, nums: List[int], k: int, t: int) -> int:
        n = len(nums)
        s = sum(nums[ :k])
        res = 1 if s / k >= t else 0
        for r in range(k, n):
            s = s + nums[r] - nums[r - k]
            if s / k >= t: res += 1
        return res 
```

[2134. 最少交换次数来组合所有的 1 II - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-swaps-to-group-all-1s-together-ii/description/)

将环形数组中所有1聚集到一起的最小交换位置次数，即长度为 $k$ (字符串中1的个数)的滑动窗口中，0个数最少的位置处。

```python
    def minSwaps(self, nums: List[int]) -> int:
        k = nums.count(1)
        if k == 0: return 0
        nums = nums + nums 
        n = len(nums)
        s = sum(nums[:k])
        res = k - s 
        for r in range(k, n):
            s = s + nums[r] - nums[r - k]
            res = min(res, k - s)
        return res 
```



**维护定长滑动窗口 + 字典计数**

[567. 字符串的排列 - 力扣（LeetCode）](https://leetcode.cn/problems/permutation-in-string/description/?envType=featured-list&envId=DMKTNBLj?envType=featured-list&envId=DMKTNBLj)

判断字符串 $s1$ 中是否包含 $s2$ 的一个排列：转化为判断是否存在两个字典计数情况相等。

```python
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k, n = len(s1), len(s2)
        target = Counter(s1)
        cur = Counter(s2[ :k])
        if target == cur: return True 
        for r in range(k, n):
            rch, lch = s2[r], s2[r - k]
            cur[rch] += 1
            cur[lch] -= 1
            if target == cur: return True
        return False
```

[438. 找到字符串中所有字母异位词 - 力扣（LeetCode）](https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/?envType=featured-list&envId=DMKTNBLj?envType=featured-list&envId=DMKTNBLj)

找出字符串 $s1$ 中所有 $s2$ 的排列的下标。

```python
def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        k, n = len(p), len(s)
        target = Counter(p)
        cur = Counter(s[ :k])
        if cur == target: res.append(0)

        for r in range(k, n):
            lch, rch = s[r - k], s[r]
            cur[rch] += 1
            cur[lch] -= 1
            if cur == target:
                res.append(r - k + 1)
        return res 
```

[2841. 几乎唯一子数组的最大和 - 力扣（LeetCode）](https://leetcode.cn/problems/maximum-sum-of-almost-unique-subarray/description/?envType=featured-list&envId=DMKTNBLj?envType=featured-list&envId=DMKTNBLj)

通过 $Counter()$ 维护滑动窗口中，不同元素的个数。（即 $len(set(win))$

```python
def maxSum(self, nums: List[int], m: int, k: int) -> int:
        s = sum(nums[ :k]) 
        cnt = Counter(nums[ :k])
        res = s if len(cnt) >= m else 0
        n = len(nums)
        for r in range(k, n):
            nl, nr = nums[r - k], nums[r]
            s = s + nr - nl 
            cnt[nr] += 1
            cnt[nl] -= 1
            if cnt[nl] == 0: cnt.pop(nl)
            if len(cnt) >= m and s > res: res = s 
        return res 
```



[2009. 使数组连续的最少操作数 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-number-of-operations-to-make-array-continuous/description/?envType=daily-question&envId=2024-04-08)

定长滑动窗口 + 正难则反：需要操作最少次数 = n - 能够不操作的最多的数字。这些数字显然是不重复的，所以首先去重。对于去重完的元素，每一个左边界$ nums[left]$, 在去重数组中 ，$[nums[left] ,~ nums[left] + n -  1]$   区间在数组中出现的次数即为当前可以保留的数字的个数。

```python
def minOperations(self, nums: List[int]) -> int:
    n = len(nums)
    nums = sorted(set(nums))
    res = left = 0
    for i, x in enumerate(nums):
        while x > nums[left] + n - 1:
            left += 1
        res = max(res, i - left + 1)
    return n - res 
```

[1423. 可获得的最大点数 - 力扣（LeetCode）](https://leetcode.cn/problems/maximum-points-you-can-obtain-from-cards/description/?envType=featured-list&envId=DMKTNBLj?envType=featured-list&envId=DMKTNBLj)

定长滑动窗口 + 正难则反：要求前 + 后 的个数为定值 $k$ 个，转换为中间为 $n-k$ 个。

```python
    def maxScore(self, nums: List[int], k: int) -> int:
        n, tot = len(nums), sum(nums)
        if n == k: return tot 
        k = n - k 
        s = sum(nums[:k])
        res = s 
        for r in range(k, n):
            s = s + nums[r] - nums[r - k]
            res = min(res, s)
        return tot - res 
```



## 不定长滑动窗口

**和大于等于 $k$ 的最短数组（最短长度）**

[209. 长度最小的子数组 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-size-subarray-sum/description/)

```python
    def minSubArrayLen(self, k: int, nums: List[int]) -> int:
        l = s = 0
        res = inf 
        for r, x in enumerate(nums):
            s += x 
            while s >= k:
                res = min(res, r - l + 1)
                s, l = s - nums[l], l + 1
        return res if res < inf else 0
```



[2904. 最短且字典序最小的美丽子字符串 - 力扣（LeetCode）](https://leetcode.cn/problems/shortest-and-lexicographically-smallest-beautiful-string/description/?envType=featured-list&envId=DMKTNBLj?envType=featured-list&envId=DMKTNBLj)

求包含恰好 $k$ 个 1的所有子串中，最短、字典序最小的：**转换为 和大于等于 $k$ 的最短数组问题。**

```python
    def shortestBeautifulSubstring(self, s1: str, k: int) -> str:
        if s1.count('1') < k: return ''
        n = len(s1)
        l = s = 0
        resl, resr = 0, n
        for r, ch in enumerate(s1):
            s += int(ch)
            while s >= k:
                width = r - l + 1
                if width < resr - resl + 1 or (width == resr - resl + 1 and s1[l: r + 1] < s1[resl: resr + 1]):
                    resl, resr = l, r 
                s, l = s - int(s1[l]), l + 1
        return s1[resl: resr + 1]
```



**和小于等于 $k$ 的最长子数组（最大长度）**

[1493. 删掉一个元素以后全为 1 的最长子数组 - 力扣（LeetCode）](https://leetcode.cn/problems/longest-subarray-of-1s-after-deleting-one-element/description/)

$s$ 统计0的个数，转换为 $s \le 1 $ 的最长子数组长度。

```python
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        l = s = 0
        # s <= 1 的最长子数组
        for r, x in enumerate(nums):
            s += 1 if x == 0 else 0
            while s > 1:
                s -= 1 if nums[l] == 0 else 0
                l += 1
            if s <= 1:
                res = max(res, r - l)
        return res
```

[2730. 找到最长的半重复子字符串 - 力扣（LeetCode）](https://leetcode.cn/problems/find-the-longest-semi-repetitive-substring/description/)

预处理相邻字符相等情况，转换为 $s \le 1$ 的最长字串。

```python
    def longestSemiRepetitiveSubstring(self, s1: str) -> int:
        l = s = 0
        res = 0
        nums = [1 if s1[i] == s1[i - 1] else 0 for i in range(1, len(s1))]
        # s <= 1 的最长子串
        for r, x in enumerate(nums):
            s += x 
            while s > 1:
                s -= nums[l]
                l += 1
            res = max(res, r - l + 1)
        return res + 1
```





**不包含重复元素的子数组（最长长度 / 最大和）**

**包含重复元素的条件是 $len(win) < r - l+1$。**

[3. 无重复字符的最长子串 - 力扣（LeetCode）](https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/)

方法一：使用 $d$ 字典维护元素出现的最新位置。当 $d[ch]$ 出现在 $[l,~r]$ 区间内表示需要更新 $l=d[ch]+1$。

```python
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = defaultdict(lambda: -inf)
        l = res = 0
        for r, ch in enumerate(s):
            if d[ch] >= l:
                l = d.pop(ch) + 1
            d[ch] = r 
            res = max(res, r - l + 1)
        return res 
```

方法二：

不包含重复元素的条件是 $len(win) = r - l+1$。

```python
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        cnt = Counter()
        for r, ch in enumerate(s):
            cnt[ch] += 1
            while len(cnt) < r - l + 1:
                lch = s[l]
                cnt[lch] -= 1
                if cnt[lch] == 0: cnt.pop(lch)
                l += 1
            res = max(res, r - l + 1)
        return res 
```



[1695. 删除子数组的最大得分 - 力扣（LeetCode）](https://leetcode.cn/problems/maximum-erasure-value/description/)

不包含重复元素的子数组的最大和。不包含重复元素的条件是 $len(win) = r - l+1$。

```python
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        l = s = 0
        cnt = Counter()
        for r, x in enumerate(nums):
            cnt[x] += 1
            s += x
            while len(cnt) < r - l + 1:
                nl = nums[l]
                s -= nl 
                cnt[nl] -= 1
                if cnt[nl] == 0: cnt.pop(nl)
                l += 1
            res = max(res, s)
        return res 
```

[2401. 最长优雅子数组 - 力扣（LeetCode）](https://leetcode.cn/problems/longest-nice-subarray/description/)

不定长滑窗 + 位运算。

子数组中所有数两两 $AND$都是 $0$，要求子数组所有比特位上是 $1$ 的个数最多是 $1$ 。用 $ors$ 维护滑窗中的 $OR$ 值， $r$ 能加入子数组需要满足 $r~ \& ~ors = 0$。（因为 $a | (b ~\&~ c) = (a \&~b) | (a \&~ c)=0   $，即与子数组中所有数相与都是0）。而从子数组中删去 $left$ 只需要做异或操作，因为已经确保了 $ors$ 比特位上面每个 $1$ 都是独属的。

```python
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # nums[i] <= 1e9，30个二进制bit位上 
        ors = 0
        l = 0 
        res = 0 
        for r, x in enumerate(nums):
            while x & ors > 0:
                ors ^= nums[l]
                l += 1
            ors |= x
            res = max(res, r - l + 1)
        return res 
```



**子数组合法方案数问题**

先更新滑动窗口状态（广义上），检查、剔除不合法的元素（如窗口左边界右移、计数器减一等），累积上 $res$ 的方案数（等于窗口长度）。

**乘积小于 $k$ 的子数组的个数（方案数）**

[713. 乘积小于 K 的子数组 - 力扣（LeetCode）](https://leetcode.cn/problems/subarray-product-less-than-k/description/)

```python
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0
        res = 0
        l, prod = 0, 1 
        for r, x in enumerate(nums):
            prod *= x 
            while prod >= k:
                prod, l = prod / nums[l], l + 1
            res += r - l + 1
        return res 
```

**不同值个数小于等于 $k$ 的子数组个数（方案数）**

使用 $freq$ 计数器维护元素出现个数、左边界 $l$ 。当

[3134. 找出唯一性数组的中位数 - 力扣（LeetCode）](https://leetcode.cn/problems/find-the-median-of-the-uniqueness-array/description/)

```python
# 计算不同值元素个数小于对于k 的子数组个数
def get_set_subarrays_lower_k(nums, k):
    l = res = 0
    freq = Counter()
    for r, x in enumerate(nums):
        freq[x] += 1
        while len(freq) > k:
            freq[nums[l]] -= 1
            if freq[nums[l]] == 0: freq.pop(nums[l])
            l += 1
        res += r - l + 1
    return res 
```





## 不定长滑窗 + 哈希计数

不定长滑窗哈希表：所有 $freq[x] \le k$ 的最长子数组，由于单次判断的时间复杂度是 $O(n)$，总复杂度是 $O(n^2) $。
通过 $cnt$ 维护 $freq[x] > k$ 的个数，**在边界处增减1**。转换为 $cnt = 0$ 最长子数组 ，复杂度 $O(n) $





[2958. 最多 K 个重复元素的最长子数组 - 力扣（LeetCode）](https://leetcode.cn/problems/length-of-longest-subarray-with-at-most-k-frequency/description/)

```python
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # 所有freq[x] <= k 的最长子数组
        # 转换为 cnt == 0 最长子数组 （cnt 为 freq[x] > k 的个数）
        freq = Counter()
        l = res = cnt = 0
        for r, x in enumerate(nums):
            cnt += int(freq[x] == k)
            freq[x] += 1
            while cnt > 0:
                nl = nums[l]
                cnt -= int(freq[nl] == k + 1)
                freq[nl] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res 
```

[Problem - 1777C - Codeforces](https://codeforces.com/problemset/problem/1777/C)

不定长滑窗 + 哈希计数。首先对 $nums$ 数组排序 + 去重，对于 $m=1$ 的情况直接返回 $0$ ；否则要求 $2 \sim m $ 中的每一个数，都在滑动窗口中的所有因子构成的集合中出现一次。因为需要维护滑窗集合，所以采用滑窗 + 哈希， $freq$  维护滑窗中所有数的因子的出现个数。由于需要 $2 \sim m $ 中均有 $freq[x] \ge 1$ ，每次判断需要 $O(n)$ 的复杂度，总体是 $O(mn)$ ，无法接受。因此使用 $cnt$ 统计 $freq[x] \ge 1$ 的个数，$cnt $ 在边界情况时增减1。

```python
from collections import *
from math import *
import sys
input = lambda: sys.stdin.readline().strip()

# 预处理 2 ~ mx中所有数的约数的列表
mx = 100001
factors = [[] for _ in range(mx)]
for i in range(2, mx):
    for j in range(i, mx, i):
        factors[j].append(i)
        
t = int(input())
def solve():
    n, m = map(int, input().split())
    nums = list(set(map(int, input().split())))
    nums.sort()
    if m == 1:
        return 0
    # 2, 3, ... , m
    # 求所有滑窗中，freq[2...m] >= 1 的最小极差。
    # 用cnt统计 freq[x] >= 1 的个数，求 cnt == m - 1 的滑窗的最小极差
    freq = Counter()
    l = cnt = 0
    res = inf
    for r, x in enumerate(nums):
        for y in factors[x]:
            if y > m: break
            if freq[y] == 0: cnt += 1
            freq[y] += 1
        while cnt == m - 1:
            nl = nums[l]
            res = min(res, x - nl)
            for y in factors[nl]:
                if y > m: break
                if freq[y] == 1: cnt -= 1
                freq[y] -= 1
            l += 1
    return res if res < inf else -1

for _ in range(t):
    print(solve())

```



## 枚举型滑窗 / 分组滑窗

**枚举出现种类个数**

枚举 + 不定长滑窗 + 哈希计数

显然 $k=1$ 时，原串满足条件直接返回其长度。

考虑 $k>1$，要求子串中所有字符个数 $\ge k$，假设 $s1[l\sim r]$ 满足条件，考虑 $s1[r+1]$，如果是在 $s1$ 中出现过的字符，一定满足；否则一定不满足条件，此时不确定滑窗的左边界 $l$ 是否需要右移，例如 $'bbaaacb'$，当 $r=4$ 时，由于后续的 $c$ 的出现会导致 无法凑出 $bbaaab$，因此需要左移。这实际上比较难以确定。

然而，如果限制 / 约束了子串中不同字母的种类个数 $c$，并依次枚举 $c \in [1, 26]$，对于每个 $c$，采用不定长滑窗 + 哈希计数的方式，可以唯一确定是否需要左移左边界。实现时，需要维护子串中每个字符出现的频次 $freq$、出现且次数不够 $k$ 的字符的个数 $cnt$、字符的种类个数 $tcnt$。

```python
    def longestSubstring(self, s1: str, k: int) -> int:
        if k == 1: return len(s1)
        n = len(s1)
        res = 0
        # 枚举滑窗
        for c in range(1, len(set(s1)) + 1):
            # 滑窗中字母种类个数恰好为 c
            freq = Counter()
            cnt = 0     # 哈希计数
            tcnt = 0    # 种类计数
            l = 0
            for r, ch in enumerate(s1):
                if freq[ch] == 0:
                    cnt += 1
                    tcnt += 1
                if freq[ch] == k - 1:
                    cnt -= 1
                freq[ch] += 1
                
                while tcnt > c:
                    lch = s1[l]
                    if freq[lch] == k: 
                        cnt += 1
                    if freq[lch] == 1:
                        tcnt -= 1
                        cnt -= 1
                    freq[lch] -= 1
                    l += 1
                if tcnt == c and cnt == 0:
                    res = max(res, r - l + 1)
        return res 
```

时间复杂度：$O(26N)$

[2953. 统计完全子字符串 - 力扣（LeetCode）](https://leetcode.cn/problems/count-complete-substrings/description/)

定长滑窗 + 枚举

```python
    def countCompleteSubstrings(self, s1: str, k: int) -> int:
        res = 0
        # s 中每个字符恰好出现 k 次的子串个数
        def f(s):
            # 
            # 枚举字符种类个数
            m = len(set(s))
            n = len(s)
            res = 0
            # 由于是恰好 k个，所以滑窗长度为 c * k
            for c in range(1, m + 1):
                K = c * k 
                if K > n: break 
                freq = Counter()
                cnt = 0 # 等于 k 的个数
                for i in range(K):
                    ch = s[i]
                    if freq[ch] == k - 1: cnt += 1
                    elif freq[ch] == k: cnt -= 1
                    freq[ch] += 1
                res += int(cnt == c)
                for r in range(K, n):
                    ch, lch = s[r], s[r - K]
                    if lch != ch:
                        if freq[ch] == k - 1: cnt += 1
                        elif freq[ch] == k: cnt -= 1

                        if freq[lch] == k: cnt -= 1
                        elif freq[lch] == k + 1: cnt += 1
                        freq[ch] += 1
                        freq[lch] -= 1

                        if freq[lch] == 0: freq.pop(lch)
                    res += int(cnt == c)
            return res 
        sub = ''
        for ch in s1:
            if sub and abs(ord(ch) - ord(sub[-1])) > 2:
                res += f(sub) 
                sub = ch 
            else:
                sub += ch 
        res += f(sub)
        return res 
```

时间复杂度：$O(26N)$



**枚举多起点**



**分组滑窗**

[2831. 找出最长等值子数组 - 力扣（LeetCode）](https://leetcode.cn/problems/find-the-longest-equal-subarray/description/?envType=daily-question&envId=2024-05-23)

按元素对下标分组 + 不定长滑窗

预处理每个元素所有下标构成的数组，对某一元素 $x$，其数组 $a$ 上做不定长滑窗，$a[r] - a[l]  + 1$ 为滑窗长度，$r-l+1$ 为 $x$ 个数。因为最多能删除 $k$ 个，所以要求 $ a[r] - a[l] + 1 - (r - l + 1) \le k$。

```python
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        d = defaultdict(list)
        for i, x in enumerate(nums):
            d[x].append(i)
        res = 1
        for a in d.values():
            m = len(a)
            l = 0
            for r in range(m):
                while a[r] - a[l] + 1 - (r - l + 1) > k:
                    l += 1 
                res = max(res, r - l + 1)
        return res    
```





## 双指针

**相向双指针**

[2105. 给植物浇水 II - 力扣（LeetCode）](https://leetcode.cn/problems/watering-plants-ii/description/?envType=daily-question&envId=2024-05-09)

```python
    def minimumRefill(self, nums: List[int], A: int, B: int) -> int:
        n = len(nums)
        i, j = 0, n - 1
        a, b = A, B
        res = 0
        while i <= j:
            l, r = nums[i], nums[j]
            if i < j:
                if a < l: 
                    a = A - l
                    res += 1
                else:
                    a -= l 
                if b < r:
                    b = B - r
                    res += 1
                else: 
                    b -= r
            else:   
                x = max(a, b)
                if x < l:
                    res += 1
            i, j = i + 1, j - 1 
        return res
```

**同向双指针**

[1574. 删除最短的子数组使剩余数组有序 - 力扣（LeetCode）](https://leetcode.cn/problems/shortest-subarray-to-be-removed-to-make-array-sorted/submissions/490971133/)

同向双指针 + 贪心。

```python
    def findLengthOfShortestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        while l + 1 < n and nums[l] <= nums[l + 1]:
            l += 1
        if l == n - 1: return 0
        while r - 1 >= 0 and nums[r - 1] <= nums[r]:
            r -= 1
        res, mxl = r, l
        for l in range(mxl + 1):
            while r < n and nums[r] < nums[l]:
                r += 1
            res = min(res, r - l - 1)
        return res
```

[1163. 按字典序排在最后的子串 - 力扣（LeetCode）](https://leetcode.cn/problems/last-substring-in-lexicographical-order/description/)

转换问题：子串中字典序最大的串

**性质1： 后缀 $s[i:]$   是以 $s[i]$  为开头的子串中，字典序最大的串。**

**性质2：考察字典序最大的串，记为 $sub$，它的每个字符都小于等于 $sub[0]$。**

> 例如，'ycyba' 是一个可能的最大串，而 'yczba'就不是，因为 'zba' > 'yczba'。



对于两个位置 $i,j$，用偏移 $k$ 考察 $s[i:] $ 和 $s[j:]$ 中各个字符的大小关系：

- $s[i+k] = s[j+k]$，则继续往后考察，$k+1$；

- $s[i+k] < s[j+k]$，应让 $i$ 跳到 $\max (i+k+1, j)$。

    - 首先可以肯定 $[i+1, i+k]$ 都不需要考虑，这是因为由于性质1，2，所以以 $[i+1, i+k]$ 开头的子串一定比 $s[i \sim i+k]$ 小；
    - 其次，如果 $i+k+1 \le j$，则 $j$ 应该曾经已经考虑过 $[i+k+1, j - 1]$ 区间了，他们都没能更新 $i$ ，一定比 $s[i:i+k]$ 小
    - 最后，如果 $i+k+1>j$ ，例如 'yybbyybbyyc' 这种情况，$s[i:i+k] = yybbyyb$，$s[j:j+k] = yybbyyc$，有公共前缀 $yybbyy$ ，以及后缀 $yyc$，即 $[j, i + k]$ 区间一定回比后缀小。

    所以， $i = \max(i+k+1, j)$, $j = i + 1, k = 0 $。

- $s[i+k] > s[j+k]$，让 $j$ 跳到 $j+k+1, k = 0$。



```python
class Solution:
    def lastSubstring(self, s: str) -> str:
        i, j, k = 0, 1, 0
        n = len(s)
        while j + k < n:
            if s[i + k] == s[j + k]:
                k += 1
            else:
                if s[i + k] < s[j + k]:
                    i = j if j > i + k + 1 else i + k + 1
                    j = i + 1
                else: # s[i + k] > s[j + k]:
                    j += k + 1
                k = 0
        return s[i: ]
```



## 分组循环

适用于：数组会被分割成若干组，且每一组的判断/处理逻辑是一样的。

**核心思想**：

- 外层循环负责遍历组之前的准备工作（记录开始位置），和遍历组之后的统计工作（更新答案最大值）。
- 内层循环负责遍历组，找出这一组最远在哪结束。

模板：

```python
n = len(nums)
i = 0
while i < n:
    start = i
    while i < n and ...:
        
        i += 1
    # 从 start 到 i-1 是一组
    # 下一组从 i 开始，无需 i += 1
	ans = max(ans, i - start)
```

时间复杂度：$O(n)$ 



[2760. 最长奇偶子数组 - 力扣（LeetCode）](https://leetcode.cn/problems/longest-even-odd-subarray-with-threshold/description/)

```python
    def longestAlternatingSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = res = 0
        while i < n:
            x = nums[i]
            if x > k or x & 1: 
                i += 1
                continue 
            start = i
            i += 1
            while i < n and nums[i] <= k and nums[i - 1] & 1 != nums[i] & 1: 
                i += 1
            res = max(res, i - start)
        return res 
```



# 单调结构 

## 单调栈

```python
    def trap(self, height: List[int]) -> int:
        # 单调栈：递减栈
        stk, n, res = deque(), len(height), 0
        for i in range(n):
            # 1.单调栈不为空、且违反单调性
            while stk and height[i] > height[stk[-1]]:
                # 2.出栈
                top = stk.pop()
                # 3.特判
                if not stk:
                    break
                # 4.获得左边界、宽度
                left = stk[-1]
                width =  i - left - 1
                # 5.计算
                res += (min(height[left], height[i]) - height[top]) *  width 
            # 6.入栈
            stk.append(i)
        return res
```

[84. 柱状图中最大的矩形 - 力扣（LeetCode）](https://leetcode.cn/problems/largest-rectangle-in-histogram/)

矩形面积求解：维护单调增栈，同时首尾插入哨兵节点。

```python
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-1)
        stk = [-1]
        res = 0
        for i, h in enumerate(heights):
            while len(stk) > 1 and h < heights[stk[-1]]:
                cur = stk.pop()
                l = stk[-1]
                width = i - l - 1
                s = width * heights[cur]
                res = max(res, s)
            stk.append(i)
        return res
```

[1793. 好子数组的最大分数 - 力扣（LeetCode）](https://leetcode.cn/problems/maximum-score-of-a-good-subarray/)

矩形面积求解问题变形：求 $min(nums[i], ~ \cdots~, nums[j]) \times (j -i+1)$ ，并对$i, ~j $ 做了范围约束。

```python
   def maximumScore(self, nums: List[int], k: int) -> int:
        stk = [-1]
        nums.append(-1)
        res = 0
        for i, h in enumerate(nums):
            while len(stk) > 1 and h < nums[stk[-1]]:
                cur = stk.pop()
                l = stk[-1]
                if not(l + 1 <= k and i - 1 >= k): continue	# 约束范围
                width = i - l - 1
                res = max(res, width * nums[cur])
            stk.append(i)
        return res
```

**单调栈维护元素的左右山形边界**

对于 $a[i]=x$ ，希望找到在左侧中的最小 $l$ 满足 $a[l + 1] \sim a[i-1] \ge 或者 \le x$；

对于 $a[i]=x$ ，希望找到在右侧中的最大 $r$ 满足 $a[i + 1] \sim a[r-1] \ge 或者 \le x$；

```python
    stk, left = [], [-1] * n
    for i in range(n):
        x = nums[i]
        while stk and x <= nums[stk[-1]]: stk.pop() 
        if stk: left[i] = stk[-1]
        stk.append(i)
    stk, right = [], [n] * n 
    for i in range(n - 1, -1, -1):
        x = nums[i]
        while stk and x <= nums[stk[-1]]: stk.pop() 
        if stk: right[i] = stk[-1]
        stk.append(i)
```

[2334. 元素值大于变化阈值的子数组 - 力扣（LeetCode）](https://leetcode.cn/problems/subarray-with-elements-greater-than-varying-threshold/description/?envType=featured-list&envId=GklvgyNg?envType=featured-list&envId=GklvgyNg)

在山形边界开区间所夹的区间内，满足所有元素大于等于山形边界元素 $x$ ，即 $x = \min(a[l+1] \sim a[r-1]) $。

```python
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        # 单调栈解法
        stk, left = [], [-1] * n
        for i in range(n):
            x = nums[i]
            while stk and x <= nums[stk[-1]]: stk.pop() 
            if stk: left[i] = stk[-1]
            stk.append(i)
        stk, right = [], [n] * n 
        for i in range(n - 1, -1, -1):
            x = nums[i]
            while stk and x <= nums[stk[-1]]: stk.pop() 
            if stk: right[i] = stk[-1]
            stk.append(i)
        for i, x in enumerate(nums):
            l, r = left[i], right[i]
            k = r - l - 1
            if x > (threshold / k): return k 
        return -1
```



## 单调队列	

**滑窗最大值 ~ 维护递减小队列； 滑窗最小值 ~  维护递增队列**

[239. 滑动窗口最大值 - 力扣（LeetCode）](https://leetcode.cn/problems/sliding-window-maximum/)

```python
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        q = deque()
        for i, x in enumerate(nums):
            # 1.入，需要维护单调减队列的有序性
            while q and x >= nums[q[-1]]:
                q.pop()
            q.append(i)

            # 2.出，当滑动窗口区间长度大于k的时候，弹出去左端的
            if i - q[0] + 1 > k:
                q.popleft()
            
            # 记录元素
            if i >= k - 1:
                res.append(nums[q[0]])
        return res    
```

[2398. 预算内的最多机器人数目 - 力扣（LeetCode）](https://leetcode.cn/problems/maximum-number-of-robots-within-budget/description/)

单调队列 + 滑动窗口

```python
  def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        res = 0
        s = l = 0   # 滑窗的和 / 窗口左边界 
        q = deque()     # 单调队列维护最大值
        # 滑动窗口
        for i, x in enumerate(chargeTimes):
            while q and x >= chargeTimes[q[-1]]:
                q.pop()
            q.append(i)
            s += runningCosts[i]
            while i - l + 1 > 0 and s * (i - l + 1) + chargeTimes[q[0]] > budget:
                s -= runningCosts[l]
                l += 1
                if l > q[0]:
                    q.popleft()
            res = max(res, i - l + 1)
        return res
```

## 单调栈优化dp

[2617. 网格图中最少访问的格子数 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-number-of-visited-cells-in-a-grid/description/?envType=daily-question&envId=2024-03-22)

暴力dp转移做法

```python
class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        f = [[inf] * n for _ in range(m)]
        f[-1][-1] = 0
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                g = grid[i][j] 
                for k in range(1, min(g + 1, m - i)):
                    f[i][j] = min(f[i][j], f[i + k][j] + 1)
                for k in range(1, min(g + 1, n - j)):                    
                    f[i][j] = min(f[i][j], f[i][j + k] + 1)
        return f[0][0] + 1 if f[0][0] != inf else -1
```

单调栈 + 二分 优化dp

倒序枚举$i,~j$
$$
f[i][j]=\min\left\{\min_{k=j+1}^{j+g}f[i][k], ~\min_{k=i+1}^{i+g}f[k][j]\right\}+1
$$
可以发现左边界$i$ 是递减的，右边界$ j +g$ 是不确定的。联想到滑动窗口最值问题，维护一个向左增长的栈，栈元素自左向右递减。

由于栈中元素有序，每次查找只需要二分即可找出最值。

```python
def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        stkyy = [deque() for _ in range(n)]	# 列上单调栈
        f = 0								# 行上单调栈
        for i in range(m - 1, -1, -1):
            stkx = deque()
            for j in range(n - 1, -1, -1):
                g, stky = grid[i][j], stkyy[j]
                f = 1 if i == m - 1 and j == n - 1 else inf
                if g > 0:
                    if stkx and j + g >= stkx[0][1]:
                        mnj = bisect_left(stkx, j + g + 1, key = lambda x: x[1]) - 1
                        f = stkx[mnj][0] + 1
                    if stky and i + g >= stky[0][1]:
                        mni = bisect_left(stky, i + g + 1, key = lambda x: x[1]) - 1
                        f = min(f, stky[mni][0] + 1)
                if f < inf:
                    while stkx and f <= stkx[0][0]:
                        stkx.popleft()
                    stkx.appendleft((f, j))
                    while stky and f <= stky[0][0]:
                        stky.popleft()
                    stky.appendleft((f, i))
        return f if f != inf else -1
```

[LCP 32. 批量处理任务 - 力扣（LeetCode）](https://leetcode.cn/problems/t3fKg1/description/)

二分单调栈

```python
class Solution:
    def processTasks(self, tasks: List[List[int]]) -> int:
        stk = [(-1, -1, 0)]
        tasks.sort(key = lambda x: x[1])
        for l, r, t in tasks:
            p = bisect_left(stk, (l, )) - 1
            blue = stk[-1][2] - stk[p][2]  
            red = max(0, stk[p][1] - l + 1) 
            t -= blue + red 
            if t <= 0: continue 
            nl, nr, nt = r - t + 1, r, stk[-1][2] + t
            while stk:
                ll, rr, _ = stk[-1]
                if nl > rr: break
                nl = ll - (rr - nl + 1)
                stk.pop()
            stk.append((nl, nr, nt))
        return stk[-1][2]
```



## 单调队列优化dp

[2944. 购买水果需要的最少金币数 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-number-of-coins-for-fruits/description/?envType=featured-list&envId=PAkZSAkX?envType=featured-list&envId=PAkZSAkX)

暴力做法：$O(n^2)$

```python
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        # f[i] 表示获得 i及其以后的所有水果的最少开销
        f = [inf] * (n + 1)
        for i in range(n, 0, -1):
            # [i + 1, 2 * i] 免费
            if 2 * i >= n:
                f[i] = prices[i - 1]
            else:
                for j in range(i + 1, 2 * i + 2):
                    f[i] = min(f[i], f[j] + prices[i - 1])
        return f[1]
```

注意到 i递减，区间 $[i + 1, 2 \times i + 1]$是一个长度为为i + 1 的滑动窗口，转移成滑动窗口最值问题。

```python
    def minimumCoins(self, prices: List[int]) -> int:
        n = len(prices)
        # f[i] 表示获得 i及其以后的所有水果的最少开销
        f = [inf] * (n + 1)
        q = deque()
        for i in range(n, 0, -1):
            # i递减，区间[i + 1, 2 * i + 1]是一个定长为i + 1 的滑动窗口
            while q and q[-1][1] - (i + 1) + 1 > i + 1:
                q.pop()
            if 2 * i >= n:
                f[i] = prices[i - 1]
            else:

                f[i] = q[-1][0] + prices[i - 1]
            while q and f[i] <= q[0][0]:
                q.popleft()
            q.appendleft((f[i], i))
        return f[1]
```



# 前缀/差分

## 一维差分

```python
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        n = len(nums)
        d = k - min(nums) 
        for i in range(n): nums[i] += d 
        mx = max(nums) + k
        a = [0] * (mx + 1)
        d = [0] * (mx + 2)
        for x in nums:
            d[x - k] += 1
            d[x + k + 1] -= 1
        a[0] = d[0]
        for i in range(1, mx + 1):
            a[i] = a[i - 1] + d[i]
        return max(a)
```



## 二维差分

```python
d = [[0] * (n + 2) for _ in range(m + 2)]
# 对矩阵中执行操作，使得左上角为(i, j)，右下角为(x, y)的矩阵都加k，等价于如下操作
d[i + 1][j + 1] += k
d[x + 2][y + 2] += k
d[i + 1][y + 2] -= k
d[x + 2][j + 1] -= k

# 还原差分时，直接原地还原
for i in range(m):
    for j in rang(n):
        d[i + 1][j + 1] += d[i][j + 1] + d[i + 1][j] - d[i][j]

```

## 二维前缀

[3070. 元素和小于等于 k 的子矩阵的数目 - 力扣（LeetCode）](https://leetcode.cn/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/description/)

```python
class PreSum2d:
    # 二维前缀和(支持加法和异或)，只能离线使用，用n*m时间预处理，用O1查询子矩阵的和；op=0是加法，op=1是异或
    def __init__(self,g,op=0):
        m,n = len(g),len(g[0])
        self.op = op
        self.p=p=[[0]*(n+1) for _ in range(m+1)]
        if op == 0:
            for i in range(m):
                for j in range(n):
                    p[i+1][j+1] = p[i][j+1]+p[i+1][j]-p[i][j]+g[i][j]
        elif op==1:
            for i in range(m):
                for j in range(n):
                    p[i+1][j+1] = p[i][j+1]^p[i+1][j]^p[i][j]^g[i][j]
    # O(1)时间查询闭区间左上(a,b),右下(c,d)矩形部分的数字和。
    def sum_square(self,a,b,c,d):
        if self.op == 0:
            return self.p[c+1][d+1]+self.p[a][b]-self.p[a][d+1]-self.p[c+1][b]
        elif self.op==1:
            return self.p[c+1][d+1]^self.p[a][b]^self.p[a][d+1]^self.p[c+1][b]
        
class NumMatrix:
    def __init__(self, mat: List[List[int]]):
        self.pre = PreSum2d(mat)
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # pre = self.pre
        return self.pre.sum_square(row1,col1,row2,col2)
    
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0
        p = NumMatrix(grid)
        for i in range(n):
            for j in range(m):
                if p.sumRegion(0, 0, i, j) <= k:
                    res += 1
        return res
                
```

`pre[i + 1][j + 1]` 是左上角为(0, 0) 右下角为 (i, j)的矩阵的元素和。

如果是前缀异或是：

`                    p[i+1][j+1] = p[i][j+1]^p[i+1][j]^p[i][j]^g[i][j]`

```python
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                pre[i + 1][j + 1] = pre[i][j + 1] + pre[i + 1][j] - pre[i][j] + grid[i][j]
        res = 0
        for i in range(m):
            for j in range(n):
                if pre[i + 1][j + 1] <= k:
                    res += 1
        return res
```

**前缀异或 / 自定义前缀操作**

```python
pre = list(accumulate(nums, xor, initial = 0))
```



# 数学

## 数论

### 取整函数

**上下取整转换**
$$
\left\lceil \frac{n}{m} \right\rceil = \left\lfloor \frac{n - 1}{m}  \right\rfloor + 1 = \left\lfloor \frac{n + m -1}{m} \right\rfloor
$$

证明：由于有 $\left\lceil \frac{n}{m} \right\rceil =   \left\lfloor \frac{n}{m}  \right\rfloor$ 当且仅当 $n=k \cdot m$ 时成立，当 $n=k\cdot m-r,r\in(0,m)$，一定有  $k=\left\lceil \frac{k\cdot m}{m} \right\rceil =\left\lceil \frac{k\cdot m-r}{m} \right\rceil = \left\lceil \frac{k\cdot m-r+1}{m} \right\rceil = 1+ \left\lfloor \frac{k\cdot m-r}{m}  \right\rfloor$，显然 $k\cdot m-r+1 \in R$，令其等于$n$  时得证 $\left\lceil \frac{n}{m} \right\rceil =1+ \left\lfloor \frac{n-1}{m} \right\rfloor$。
$$
\left\lfloor \frac{n}{m} \right\rfloor =\left\lceil \frac{n+1}{m} \right\rceil-1
$$

灵神恒等式*

$\left\lfloor\frac{\lfloor n/p\rfloor}q\right\rfloor=\left\lfloor\frac n{pq}\right\rfloor $

[1553. 吃掉 N 个橘子的最少天数 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-number-of-days-to-eat-n-oranges/description/?envType=daily-question&envId=2024-05-12)

实际上这个结论可以推广到任意个数，比如：$\left\lfloor\frac{\left\lfloor\frac{\left\lfloor\frac n{p_1}\right\rfloor}{p_2}\right\rfloor}{p_3}\right\rfloor=\left\lfloor\frac n{p_1\cdot p_2\cdot p_3}\right\rfloor $。

[题目详情 - 数字游戏 - HydroOJ](https://hydro.ac/d/nnu_contest/p/LC2)



**不等式**
$$
x-1<\lfloor x\rfloor\leqslant x\leqslant\lceil x\rceil<x+1
$$

**取余性质**
$$
n \mod m = n - m \cdot \left\lfloor \frac{n}{m}\right\rfloor
$$

**幂等律**
$$
\big\lfloor \left\lfloor x \right\rfloor \big\rfloor = \left\lfloor x \right\rfloor \\
\big\lceil \left\lceil x \right\rceil  \big\rceil = \left\lceil x \right\rceil
$$

### 素数

**素数计数函数近似值**

小于等于$x$ 的素数个数记为 $\pi(x)$，$\pi (x) 近似于 \frac{x}{\ln x}$。

#### **(1). 埃氏筛**

时间复杂度：$O(nloglogn)$

```python
primes = []
is_prime = [True] * (n + 1) # MX为最大可能遇到的质数 + 1
is_prime[1] = is_prime[0] = False

for i in range(2, int(math.sqrt(n)) + 1):	# i * i <= n
    if is_prime[i]:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False
for i in range(2, n + 1):
    if is_prime[i]: primes.append(i)
```

时间复杂度证明

对于2，要在数组中筛大约 $\frac{n}{2}$个数，同理对于素数$p$，约要筛去$\frac{p}{n}$个数。
$$
故有 O\left(\sum_{k=1}^{\pi(n)}\frac{n}{p_k} \right) = O\left(n \sum_{k=1}^{\pi(n)} \frac{1}{p_k}\right)
= O(nloglogn) \space (Mertens 第二定理)
$$
切片优化

```python
primes = []
is_prime = [True] * (n + 1) 
is_prime[0] = is_prime[1] = False
for i in range(2, int(math.sqrt(n)) + 1):
    if is_prime[i]: 
        is_prime[i * i::i] = [False] * ((n - i * i) // i + 1)
for i in range(2, n + 1):
    if is_prime[i]: primes.append(i)
```

#### **(2). 欧拉筛 / 线性筛**

基本思想：每一个合数一定存在最小的质因子。确保每一个合数只被他的最小质因子筛去。 	

```python
primes = []
is_prime = [True] * (n + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, n + 1):
    if is_prime[i]: primes.append(i)
    for p in primes:
        if i * p > n: break
        is_prime[i * p] = False
        if i % p == 0: break
```

正确性证明：

1. 每个合数不会被筛超过一次：

   枚举$i$  从小到大的所有质数，在$i \% p = 0$ 出现之前，$p$ 一定小于$i$ 的所有质因子，$p \cdot i$  的质因子的前缀与$i$ 的质因子前缀相同，故$p$ 一定是$i \cdot p$ 的最小质因子，筛去；在出现$i \% p =0$ 时，$p$ 恰好是$i$ 的最小质因子，同理，然后break。保证每个合数只会被最小的质因子筛去。

2. 每个合数都会被筛最少一次：

   每个合数$x$ 一定存在最小质因子$p$，和对应的$ x / p$。在 $i$ 枚举到 $x / p$ 的时候，一定会筛去$x$

由于保证每个合数一定被晒一次，所以是$O(n)$ 

#### **(3). 分解质因子**

试除法。复杂度不超过$O(\sqrt n )$，实际上是 $O(logn) \sim O(\sqrt {n})$

对于一个数x，最多有一个大于等于$\sqrt n$ 的质因子。（可以用反证法，证明）

所以只需要进行特判，在遍历完$[2, int(\sqrt n)]$ 区间后，如果 x 比 1大，则x 就等于那最后一个质因子。

```python
def solve(x):
    for i in range(2, int(math.sqrt(x)) + 1):	# i = 2; i * i <= x
        if x % i == 0:
            s = 0
            while x % i == 0:
                s += 1
                x //= i
            print(f'{i} {s}')		# i 是质因子， s 表示幂次
    if x > 1:
        print(f'{x} 1')
    print()
```

Oi Wiki 风格：

```python
def breakdown(N):
    result = []
    for i in range(2, int(sqrt(N)) + 1):
        if N % i == 0: # 如果 i 能够整除 N，说明 i 为 N 的一个质因子。
            while N % i == 0:
                N //= i
            result.append(i)
    if N != 1: # 说明再经过操作之后 N 留下了一个素数
        result.append(N)
    return result
```

统计质因子及其出现次数

```python
# 统计质因子及其出现次数
def breakdown(n):
    res = []
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                n //= i
                cnt += 1
            res.append((i, cnt))
    if n > 1: res.append((n, 1))
    return res
```



#### (4). 阶乘分解质因子

**求 $n!$ 中 质因子 $p$ 的出现次数问题**

> 例如 $9!$ 中 $2$ 的出现次数，$9!$ 中有$2,4,6,8$ 分别提供 $1,2,1,3$ 个 $2$ ，出现次数为 $7$ 。

$n!$ 中 $p$ 出现次数，$[1,n]$ 中是 $p$ 的倍数的数各自提供1个$p$，有 $n // p$ 个数；这些数都除$p$ 表示各拿走一个$p$，之后最大的数是 $n//p$，更新上界 $n' \leftarrow n//p$ ，在$[1,n'$] 中 $p$ 的倍数的数各自提供1个$p$ ，有 $n' // p $ 个数，重复上面操作，直到 $n=0$ 。

```python
# 统计 n!中质因子p出现的次数
def fpf(n, p):   # factorial_prime_factor 
    res = 0
    while n:
        res += n // p
        n //= p
    return res
```



**求 $n!$ 转换为 $b$ 进制数字后的末尾0的个数。**

> 例如：$(9!)_{10}=(720)_{10}=(880)_{9} = 8 \times 9^2 + 8 \times 9^1+0\times 1=3^4\times 2^3+2^3 \times 3^2=3^2\times 2^4\times 5$；
>
> $5!=(120)_{10}=1111000_{2}=2^3\times 3^1\times5^1$。

$x$ 在 $b$ 进制下的表示是 $x = \sum d_i b^{i}$，最低非0位 $k$对应 $d_k\times b^k$, 一定能将$x$ 表示成 $b^k \times (\sum d_i\times b^{i-k})$，实际上由于 $x$ 可以表示成标准分解式 $x=p_0^{k_0} \times p_1^{k_1}\cdots$，将 $b$ 分解成 $p_0^{k'_0} \times \cdots$，实际上 $k$ 等于 $\min \frac{k_i}{k_i'}$。转换为：$k_i$ 为 $b$ 的质因子在 $n!$ 中出现的次数。

[Problem - C - Codeforces](https://codeforces.com/contest/1114/problem/C)

```python
# 统计 n!中质因子p出现的次数
def fpf(n, p):   # factorial_prime_factor 
    res = 0
    while n:
        res += n // p
        n //= p
    return res
# 统计质因子及其出现次数
def breakdown(n):
    res = []
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                n //= i
                cnt += 1
            res.append((i, cnt))
    if n > 1: res.append((n, 1))
    return res
def solve():
    n, b = map(int, input().split())
    pf = breakdown(b)
    res = inf
    for f, c in pf:
        res = min(res, fpf(n, f) // c)
    return res
```



### 约数

#### **试除法求所有约数**

复杂度为：$O(\sqrt{n})$

```python
def solve(x):
    res = []
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            res.append(i)
            if i != x // i:
            	res.append(x // i)
	res.sort()  
```

**乘积数的约数个数**

对于一个以标准分解式给出的数 $N = \prod_{i = 1}^k p_i^{\alpha_i}$, 其约数个数为  $\prod_{i = 1} ^k (\alpha_i + 1)$

> 例如 $N = 2^5 \cdot 3^1, 约数个数为(5 + 1) \times (1 + 1) = 12$

**乘积数的所有约数之和**

对于一个以标准分解式给出的数 $N = \prod_{i = 1}^k p_i^{\alpha_i}$, 其约数之和为  $\prod_{i = 1} ^k (\sum_{j = 0}^{\alpha_i} p_i^j)$

> 例如 $N = 2^5 \cdot 3^1, 约数个数为 (2^0 + 2^1 + \cdots + 2^5) \times (3^0 + 3^1)$。展开结果实际上，各个互不相同，每一项都是一个约数，总个数就是约数个数。

[871. 约数之和 - AcWing题库](https://www.acwing.com/problem/content/873/)

```python
from collections import Counter
from math import *
moder = 10 ** 9 + 7
res = 1
t = int(input())
cnt = Counter()
for _ in range(t):
    x = int(input())
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            c = 0
            while x % i == 0:
                c += 1
                x //= i 
            cnt[i] += c 
    if x > 1: cnt[x] += 1
def S(a, n):
    s0 = 1 
    for _ in range(n):
        s0 = (a * s0 + 1) % moder 
    return s0
for a, n in cnt.items():
    res = (res * S(a, n)) % moder
print(res % moder)

```

#### 约数筛 / 约数预处理

求 $[1:mx]$ 范围内每个数的所有约数（包含1 和 自身）列表（**从小到大排列**）。

时间复杂度： $O(n \sqrt n)$

```python
# mx = 10 ** 5 + 1
factors = [[] for _ in range(mx)]
for f in range(1, mx):
    for x in range(f, mx, f):
        factors[x].append(f)
```



### 欧拉函数

定义：$\phi(n) $ 表示 $1 \sim n $ 中 与 $n$  互质（最大公约数为1）的数的个数。

时间复杂度：$O(\sqrt n)$ ，同质因数分解。

对于一个以标准分解式给出的数$N = \prod_{i = 1}^k p_i^{\alpha_i}$，满足：
$$
\phi(N) = N \cdot \prod_{i = 1}^{k} \left( 1 - \frac{1}{p_i} \right)
$$
证明方法：

- 容斥原理。

- 减去 $p_1, p_2, \cdots, p_k $ 的所有倍数的个数，这一步会多筛一些数。例如 一个数既是 $p_1$, 又是$p_2$ 的倍数，会删去两次。
  $$
  N - \sum_{i = 1}^{k} \frac{N}{p_i}
  $$

- 加上所有 $p_i \cdot p_j$ 的倍数
  $$
  N - \sum_{i = 1}^{k} \frac{N}{p_i} + \sum_{i, j \in [0, k] 且 i< j} \frac{N}{p_i \cdot p_j}
  $$

- 减去所有$p_i \cdot p_j \cdot p_u$ 的倍数，以此类推。
  $$
  N - \sum_{i = 1}^{k} \frac{N}{p_i} + \sum_{i, j \in [0, k] 且 i< j} \frac{N}{p_i \cdot p_j} - \sum_{i, j,u \in [0, k] 且 i< j<u} \frac{N}{p_i \cdot p_j \cdot p_u} + \cdots =  N \cdot \prod_{i = 1}^{k} \left( 1 - \frac{1}{p_i} \right)
  $$

最后一步，可以通过观察系数的角度来证明。例如$\frac{1}{p_i} $ 项的系数是 -1。

证明方法二：
$$
\phi(N) = \phi(\prod_{i = 1} ^ k p_i ^ {a_i}) = \prod_{i = 1} ^ {k} \phi(p_i^{a_i}) = \prod_{i = 1}^{k} p_i^{k}(1 - \frac{1}{p_i}) = N \cdot \prod_{i = 1}^{k} (1 - \frac{1}{p_i})
$$

性质：

- 积性函数：对于互质的$p, q$,  $\phi(p \times q) = \phi(p) \times \phi(q)$。 特别的， 对于奇数$p$， $\phi(2p) = \phi(p)$

​		证明：互质的数，质因子分解的集合无交集。$\phi(2) = 1$

- 对于质数$p$ ， $\phi(p^k) = p^k - \frac{p^k}{p} = p^k - p^{k -1}$

​		证明：减去是$p$ 的倍数的数，剩下不是p 的倍数的数，一定和 $p$ 互质。

```python
def solve(n):
    res = n
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            res = res * (i - 1) // i
            while n % i == 0:7
                n //= i 
    if n > 1:
        res = res * (n - 1) // n
    return res
```

#### 1. 筛法求欧拉函数

对于$N$ 的最小质因子$p_1$， $N' = \frac{N}{p_1}$，我们希望筛法中，$N$ 通过$N' \cdot p_1$ 筛掉。

考虑两种情况：

- $ N' \mod p_1 = 0  $，则 $N'$ 包含了$N$ 的所有质因子。

$$
\phi(N) = N \times \prod_{i = 1}^{k} (1 - \frac{1}{p_i}) = N' \cdot p_1 \times \prod_{i = 1}^{k} (1 - \frac{1}{p_i}) = p_i \times \phi(N')
$$

- $N' \mod p_i \ne 0$ ，则$N'$ 与 $p_1$ 互质（证明：质数是因子只有1和本身，因此最大公约数是1，互质）。

​	由欧拉函数的积性性质，互质的数质因子分解无交集：
$$
\phi (N) = \phi(N' \times p_1) = \phi(N') \times \phi(p_1) = \phi(N') \times (p_i - 1)
$$
在筛质数的同时筛出欧拉函数。

```python
primes = []
is_prime = [True] * (n + 1)
phi = [0] * (n + 1) 
phi[1] = 1
for i in range(2, n + 1):
    if is_prime[i]: 
        phi[i] = i - 1
        primes.append(i)
    for p in primes:
        if p * i > n: break
        is_prime[i * p] = False
        if i % p == 0:
            phi[i * p] = p * phi[i]
            break
        phi[i * p] = (p - 1) * phi[i]
```

####  2. 欧拉定理

$$
若 a 与 n互质，则 a^{\phi(n)} \mod n ~ =1
$$

> 例如：$5^ {\phi(6)} \mod 6=5^2 \mod 6=25 \mod 6=1$。

证明：考察$1\sim n$ 中与$n$ 互质的 $\phi(n)$ 个数：$p_1, ~p_2,~\cdots,~p_{\phi(n)}$。将他们乘上 $a$ ，再逐个对 $n$ 取模，得到另一组数 $ap_1 \mod n, ~~ap_2 \mod n,\cdots,~~ap_{\phi(n)} \mod n$。

可以证明这一组数两两不相同（反证法，若$ap_i \equiv ap_j(\mod n)$，则$ap_i - ap_j \equiv 0(\mod n)$，由于 $a,~n$ 互质，则一定有 $p_i = p_j$，矛盾），同时这一组每个数都和 $n$ 互质（因为 $a$ 和 $p_i$ 都与 $n$ 互质）。

则可以得到，新的这组数集 和 原先与 $n$ 互质的数集完全相同。有：$p_1 \cdot p_2 \cdots p_{\phi(n)} \mod n = \prod a p_i \mod n$，即：
$$
a^{\phi(n)} \equiv 1~~ (\bmod~ n)
$$

####  3.费马小定理

若 $a$ 与 素数 $p$ 互质，则 $a^{p-1} \equiv 1 (\mod ~ p)$。



### 裴蜀定理

对正整数 $a,b$，记最大公约数 $d=gcd(a,b)$，

- 对于任意 $x,y$，$ax+by=D,~D$ 是 $d$ 的倍数，即 $d|(ax+by)$
- 一定存在 $x,y$ 使得 $ax+by=d$ 成立。（例如，一定存在 $x,y$ 使得 $12x+8y = 4$）

- 推论：$gcd(a,b )=d \iff $存在  $x,y 使得 ax +by=d$；

    $a,b$ 互质 $\iff$ 存在$x,y$ 使得 $ax+by=1$。

推广：对于任意$n$ 个数 $a1,a2,\cdots , a_n$ ，最大公约数为 $d=gcd(a1, \cdots, a_n)$

- 一定存在 $x1, \cdots, x_n$ 使得 $\sum a_i x_i = d $ 成立。（即对于任意  $\sum a_i x_i = k $，$k$ 一定是 $d$ 的整数倍）
- $gcd(a1, \cdots, a_n) = d \iff $  存在 $x_1, c\dots, x_n$， 使得  $\sum a_i x_i = d$



[1250. 检查「好数组」 - 力扣（LeetCode）](https://leetcode.cn/problems/check-if-it-is-a-good-array/description/)

判断是否能从原给定集合中，选出子集 $A=\{a1, \cdots,a_n\}$，存在一组$X=\{x1, \cdots,x_n\}$，使得$AX=1$。实际只需要整个原集合的 $gcd$ 值为1，则一定存在一个最小子集其$gcd$ 为1，由裴蜀定理，能找到存在一组$X=\{x1, \cdots,x_n\}$，使得$AX=1$。

```python
    def isGoodArray(self, nums: List[int]) -> bool:
        res_gcd = nums[0]
        for x in nums:
            res_gcd = gcd(res_gcd, x)
        return res_gcd == 1
```



[1625. 执行操作后字典序最小的字符串 - 力扣（LeetCode）](https://leetcode.cn/problems/lexicographically-smallest-string-after-applying-operations/description/)

暴力枚举需要 $O(nC+nC) $，其中当 $b $ 是偶数时，$C=10$，否则 $C=10^2$。其中枚举轮转起点位置阶段可以使用裴蜀定理优化。

对于任意起点 $i'=(i\times b) \bmod n = ib - kn$，由裴蜀定理  $\sum a_i x_i = k $，$k$ 一定是 $d$ 的整数倍，所以 $i'=K \times gcd(b,n)$。则在一个字符串轮转中，只需要通过扩展字符串为两倍长度，枚举起点在 $gcd(a,b)$ 的整倍数的位置即可。时间复杂度：$O(nC + \frac{n}{gcd(a,b) }\times C)$，其中当 $b $ 是偶数时，$C=10$，否则 $C=10^2$。

```python
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        res = s
        n = len(s)
        s = s + s
        s_str = set()
        e_lim = 10 if b & 1 else 1   # b为奇数才可以对偶数位置增加
        for o_cnt in range(10): # 对奇数位置增加a的次数
            for e_cnt in range(e_lim):
                tmp = list(map(int, s))
                for i in range(1, 2 * n, 2): tmp[i] = (tmp[i] + a * o_cnt) % 10
                for i in range(0, 2 * n, 2): tmp[i] = (tmp[i] + a * e_cnt) % 10
                s_str.add(''.join(map(str, tmp)))
        def _gcd(a, b):
            return _gcd(b, a % b) if b else a
        g = _gcd(n, b)  
        for i in range(0, n, g):	# 裴蜀定理优化
            for ss in s_str:
                tmp = ss[i: i + n]
                if tmp < res: res = tmp 
        return res

```



### **欧几里得算法**

算法原理：$gcd(a, b) = gcd(b,a\mod b)$

证明：

- 对于任意一个能整除$a$ 且 能整除 b 的数 $d$， $a \mod b $ 可以写成 $a - k \cdot b$ ，其中 $k = a // b$ ，所以 $d$ 一定能够整除 $b, a \mod b$；
- 对于任意一个能整除 $b$  且能整除 $a - k \cdot b$  的数 $d$， 一定能整除$a-k\cdot b + k\cdot b  = a$，所以二者的公约数的集合是等价的。
- 所以二者的最大公约数等价

```python
def gcd(a, b):
    return gcd(b, a % b) if b else a
```

**时间复杂度：$O(\log (\max(a,~b)))$**

证明：

引理1： $a\mod b \in[0,~ b-1]$。例如，$38 \mod 13 = 12$

引理2：取模，余数至少折半。

如果$ b > a//2,~a \mod ~b = a - b < a//2$。例如，a = 9, b = 5, a mod b = 9 - 5 = 4

如果 $b \le a//2, ~ a \mod b \le b - 1 \le a//2 -1$。

情况1：当每次执行 gcd时，如果 $a < b$ ，则交换；情况2：否则$a \ge b$，一定发生引理2的情况，即对 $a$ 取模，一定会让 $a$ 折半。最坏情况下，每两次让 $a$ 折半，所以时间复杂度为 ：

$O(T) =  O(T /2) + 2 = O(T/4) + 4 = O(\frac {T}{2^k}) + k\times2 = 2\log k$，即 $O(\log(\max(a, b)))$



#### 扩展欧几里得

[877. 扩展欧几里得算法 - AcWing题库](https://www.acwing.com/problem/content/879/)

求解 $ax+by=gcd(a,b)$ 的一组整数解。

当 $b=0$，$(x,y)=(1,0)$；否则 $gcd(a,b)=gcd(b, a \bmod b)$，向下递归一层，得到下一层的$(x',y')$。由裴蜀定理，$bx'+(a \%b)y'=bx'+(a-a//b \times b)y'=ax+by$，所以 $a(y')+b(x'-a//b \times y') = ax+by$，可得解为$(y', x'-a//b \times y')$，再回代到上一层，最终可以得到**特解$(x_0, y_0)$**。构造通解：$(x_0+k\times \frac{b}{gcd(a,b)},~y_0-k\times \frac{a}{gcd(a,b)})$。

```python
def exgcd(a, b):
    if b == 0: return 1, 0, a
    x, y, d = exgcd(b, a % b)
    return y, x - a // b * y, d
```



### 线性同余方程

[878. 线性同余方程 - AcWing题库](https://www.acwing.com/problem/content/880/)

**线性同余方程**

- 给定$a,b, m(a\bmod m \ne0)$， 求一个特解$ x$， 使得 $ax \equiv b (\bmod m)$。

- 求方程 $ax+my=b$ 的特解。

无解条件：$b\bmod gcd(a,m) \ne 0$

> 例如 $2x \equiv 3 (\bmod 6)$，无解；$4x \equiv 3 (\bmod 5)$，解的形式是$5k+2$。

转换为 存在整数$y$， 使得$ax = m(-y) +b $，即 $ax+my=b$。由裴蜀定理，这个方程有解的条件是 $b$ 是 $gcd(a, m)$ 的倍数。对应特解通过扩展欧几里得构造，求得一组特解 $(x_0, y_0)$，满足 $ax_0 + my_0 =gcd(a,m)$，将方程除 $gcd(a,m)$ 再乘$b$ ，即最后结果方程一组特解为 $(x_0'=x_0 \times \frac {b}{gcd},~ y_0'= y_0 \times \frac{b}{gcd})$。则其任意解为：$(x'_0+k\times \frac{m}{gcd},~y'_0-k\times \frac{a}{gcd})$，则通解$x' \bmod \frac{m}{gcd} = x'_0$，所以最小特解为$x_m = x_0 \times \frac{b}{gcd} \bmod \frac{m}{gcd},~~y_m=y_0\times \frac{b}{gcd} \bmod \frac{a}{gcd}$。

```python
def exgcd(a, b):
    if b == 0: return 1, 0, a
    x, y, d = exgcd(b, a % b)
    return y, x - a // b * y, d

# 求 ax + by = c 的特解
def liEu(a, b, c):
    x, y, d = exgcd(a, b)
    if c % d != 0: return None
    # x0 + k * (b // d)
    # y0 - k * (a // d)
    return x * (c // d) % (b // d), y * (c // d) % (a // d)
```

​	

**同余**

两个整数$a$,$b$,若它们除以正整数$m$ 所得的余数相等，则称$a$, $b$对于模$m$ 同余， 读作$a$同余于$b$ 模$m$,或读作$a$与$b$关于模$m$ 同余。

**同余性质**

- 保持基本运算：

$$
a\equiv b\quad(\mathrm{mod~}m)\Rightarrow\begin{cases}an\equiv bn&\mathrm{(mod~}m),\forall n\in\mathbb{Z}\\a^n\equiv b^n&\mathrm{(mod~}m),\forall n\in\mathbb{N}^0&\end{cases}.
$$

- 除法原理：若$ka\equiv kb\quad({\mathrm{mod}}\quad m)$且$k,m$ 互质，则$a\equiv b\quad({\mathrm{mod}}\quad m)$



### 乘法逆元

**快速幂求逆元**

条件： 1. 模数 $b$  是质数。2. $a \bmod b \ne0$

$a$ 模 $b$  的乘法逆元是 $a^{b-2} \bmod b$

[876. 快速幂求逆元 - AcWing题库](https://www.acwing.com/problem/content/description/878/)

```python
def qmi(a, n, p):
    res = 1
    while n:
        if n & 1: res = res * a % p
        a = a * a % p 
        n >>= 1
    return res
def inv(a, b):	# 确保 b 是素数且 a % b != 0
    return qmi(a, b - 2, b)
```



**扩展欧几里得求逆元**

条件：1. $gcd(a,b)=1$  。 2. $a \bmod b \ne0$

- 求 $a$ 在模 $b$ 意义下的逆元
- 求线性同余方程 $ax\equiv1 (\bmod b)$ 的解 $a^{-1}$

转化为方程$ax+by=1$ 的解 $x$, 时间复杂度：$ O(log(min(a, b)))$

```python
def exgcd(a, b):
    if b == 0: return 1, 0, a
    x, y, d = exgcd(b, a % b)
    return y, x - a // b * y, d

# 求 ax + by = c 的特解
def liEu(a, b, c):
    x, y, d = exgcd(a, b)
    if c % d != 0: return None
    return x * (c // d) % (b // d), y * (c // d) % (a // d)

def inv(a, b):
    # ax mod b = 1
    # ax + by = 1
    x, y = liEu(a, b, 1)
    return x
```

#### 线性求逆元

[P3811 【模板】模意义下的乘法逆元 - 洛谷 | 计算机科学教育新生态 (luogu.com.cn)](https://www.luogu.com.cn/problem/P3811)

求$1,2, \cdots, n$ 中每个数关于 $p$  的逆元。

已知 $1\times 1\equiv1(\bmod b)$ 恒成立。对于 $i$ 的逆元 $i^{-1}$，考察模数 $p$ 关于 $i$ 的倍数 $k = \lfloor \frac{p}{i} \rfloor$，$j=p \bmod i$，有 $p=ki+j$。放到模$p$ 意义下，$ki+j \equiv0 (\bmod p)$，同乘 $i^{-1} \times j ^{-1}$，得 $kj^{-1} + i^{-1} \equiv 0(\bmod p)$，移项 $i^{-1} \equiv-kj^{-1} (\bmod p) \equiv - \lfloor \frac{p}{i} \rfloor (p \bmod i)^{-1} (\bmod p)$

递推式：
$$
\text{inv}[i] = 
\begin{cases}
1, & \text{if} ~i = 1
\\
-(p //i) \times \text{inv}[p \%i],&\text{otherwise}

\end{cases} 
~(\bmod p)
$$

```python
inv = [1] * (n + 1)
for i in range(2, n + 1):
    k, j = (p // i), p % i
    inv[i] = -k * inv[j] % p
```





**逆元解决除法取模**

如果$b$ 与$p$ 互质，对于$\forall ~a，$如果$a /b$  是整数，则一定存在乘法逆元 $x$，使得 $\frac{a}{b} \equiv a \cdot x (mod~p)$。 $x$ 是 $b$ 的乘法逆元，记为$b^{-1}$（$b$ 模 $p$ 的逆元）。**$b$ 的乘法逆元存在的充要条件：$b$  和 $p$ 互质。**

**逆元性质**

- $b \cdot b^{-1} \equiv1(mod~p)$ （证明：对定义式两边同乘 $b$，得到 $a\equiv a\cdot b ^{-1} \cdot b (mod ~p)$，由于 $a$ 是 $b$ 的倍数，且$b$ 与 $p$ 互质，所以$a$ 与 $p$ 互质，满足同余的除法原理。）
- 当模数 $p$ 为素数时，$b^{-1}_{\bmod p} =b^{p-2}$。（证明：特殊情况下，对于质数 $p$，由费马小定理得 $b^{p-1}\equiv1(mod~p)$，则可知，要求与其互质的数 $b$ 的逆元 $x$ 满足 $bx \equiv 1(mod~p)$，$b^{-1} =x=b^{p-2}$，可以使用快速幂求。



### 中国剩余定理 

条件：整数 $m_1,m_2,\ldots,m_n$ **两两互质**

> $引理：\text{寻找整数 }y_1\text{ 满足 }y_1\text{ 除以3余1、除以5余0、除以7余}0;$
>
> $y1$ 一定是 $5 \times 7 = 35$ 的倍数，设 $y1 = 35k$ ，则有 $35k \equiv 1 (\bmod 3)$，此时 $k$ 是 $35$ 模3的逆元

对于任意的整数$a_1,a_2,\ldots,a_n$ ,方程组
$$
\begin{cases}
x \equiv a_1(\bmod m_1) \\
x \equiv a_2(\bmod m_2) \\
\cdots \\
x \equiv a_n(\bmod m_n) \\
\end{cases}
$$
的最小非负整数解：$x
\equiv
\sum_{i=1}^na_i
\times\frac M{m_i}
\times \text{inv}(\frac{M}{m_i},~m_i)\pmod{N}，
其中 M=\prod_{i=1}^nm_i 。$记 $c_i=\frac{M}{m_i}, x=\sum a_ic_i \cdot \text{inv}(c_i,~m_i)$。

[P1495 【模板】中国剩余定理（CRT）/ 曹冲养猪 - 洛谷 | 计算机科学教育新生态 (luogu.com.cn)](https://www.luogu.com.cn/problem/P1495)

```python
def exgcd(a, b):
    if b == 0: return 1, 0, a
    x, y, d = exgcd(b, a % b)
    return y, x - a // b * y, d
def liEu(a, b, c):
    # ax + by = c 的解
    x, y, d = exgcd(a, b)
    a //= d
    b //= d
    c //= d
    return x * c % b, y * c % a
def inv(a, b):
    x, _ = liEu(a, b, 1)
    return x
def CRT(a, m):
    M = 1
    res = 0
    for mi in m: M *= mi
    for ai, mi in zip(a, m):
        ci = M // mi
        res = (res + ai * ci * inv(ci, mi)) % M
    return res
```

#### 扩展中国剩余定理

[204. 表达整数的奇怪方式 - AcWing题库](https://www.acwing.com/problem/content/206/)

[P4777 【模板】扩展中国剩余定理（EXCRT） - 洛谷 | 计算机科学教育新生态 (luogu.com.cn)](https://www.luogu.com.cn/problem/P4777)

删去条件$m_i$ 两两互质。

前两个方程：$x\equiv a_1(\bmod m_1),x\equiv a_2(\bmod m_2)$，转换成不定方程 $x=pm_1 +a_1=qm_2+a_2$，移项得到 $pm_1-qm_2=a_2-a_1$，由裴蜀定理，当$a_2-a_1$ 不是 $gcd(m_1,m_2)$ 的倍数时，整个方程无解；否则得到$gcd$ 方程的特解$(p_0,q_0)$，由扩展欧几里得，原方程其通解为$(P=p_0 \times\frac{a_2-a_1}{gcd(m_1, m_2)} \bmod \frac{m_2}{gcd(m_1, m_2)}+ k\frac{m_2}{gcd(m_1, m_2)},~~~~Q=q_0\times \frac{a_2-a_1}{gcd(m_1,m_2)} \bmod \frac{m_1}{gcd(m_1, m_2)} - k\frac{m_1}{gcd(m_1, m_2)}) $。

代入有$x=Pm_1+a_1=p'_0m_1+a_1+k\times \frac{m_1m_2}{gcd(m_1,m_2)}=p_0'm_1+a_1+k \cdot \text{lcm}(m_1, m_2)$，所以可以写成$x\equiv a_1' (\bmod m_1')，a_1'=p_0'm_1+a_1,m'_1=\text{lcm}(m_1,m_2)$。每一次合并可以使得方程数量减少1，只需要合并 $n-1$ 次。

每一次将$m_1 \leftarrow abs(\frac{m_1m_2}{gcd(m_1,m_2)}),~a_1 \leftarrow p'_0m_1 + a1$。

```python
def exgcd(a, b):
    if b == 0: return 1, 0, a
    x, y, d = exgcd(b, a % b)
    return y, x - a // b * y, d
def liEu(a, b, c):
    x, y, g = exgcd(a, b)
    a, b, c = a // g, b // g, c // g
    return x * c % b, y * c % a, g
def ex_CRT(a, m):
    a1, m1 = a[0], m[0]
    for i in range(1, len(a)):
        a2, m2 = a[i], m[i]
        # 构造p * m1 + a1 = q * m2 + a2
        p, q, g = liEu(m1, -m2, a2 - a1)
        if (a2 - a1) % g != 0: return -1
        a1 = p * m1 + a1
        m1 = abs(m1 * m2 // g)
    return a1
```

[P8807 [蓝桥杯 2022 国 C\] 取模 - 洛谷 | 计算机科学教育新生态 (luogu.com.cn)](https://www.luogu.com.cn/problem/P8807)

给定 $n,m$, 问是否存在两个不同的数 $x,y$ 使得 $1\leq x<y\leq m$ 且$n\bmod x=n\bmod y$。

考虑反面情况，当且仅当对于任意 $[1,m]$ 的数 $x$ ，$n \bmod x$  两两不相等，则不成立。由于对于任意的 $n$，$n \bmod 1=0$，所以$n \bmod 2$ 只能取1，同理 $n \bmod 3 $只能取2，可以得到 $n \bmod k$ 必须取 $k-1$。所以当且仅当 $\forall k \in [1, m] 有 n \bmod k =k-1$恒成立，才不存在。

```python
def solve():
    n, m = map(int, input().split())
    for k in range(1, m + 1):
        if n % k != k - 1:
            return 'Yes'
    return 'No'
```

由扩展中国剩余定理，$m_1 = 1, a_1=0$，每一次将$m_1 \leftarrow abs(\frac{m_1m_2}{gcd(m_1,m_2)}),~a_1 \leftarrow p'_0m_1 + a1$。最终 $m_1 = lcm(1,2,\cdots,m)$，$a_1 = -1$，有方程$x\equiv -1(\bmod m_1)$，所以必然有当 $ n \bmod L=-1 即L-1$  时，不存在返回 'NO'。由于当 $m$ 比较大的时候，其 $L$ 值增长速度快，值已经超过 $n$，此时$n \bmod L = n < L-1$ 一定返回 'Yes'。

```python
def gcd(a, b):
    return gcd(b, a % b) if b else a
    
def lcm(a, b):
    return a * b // gcd(a, b)
    
Lcm = [1] * 21
for i in range(2, 21):
    Lcm[i] = lcm(i, Lcm[i - 1])
def solve():
    n, m = map(int, input().split())
    if m > 20: return 'Yes'
    L = Lcm[m]
    if n % L == L - 1: return 'No'
    return 'Yes'

```



## 离散数学

### 容斥

[2652. 倍数求和 - 力扣（LeetCode）](https://leetcode.cn/problems/sum-multiples/description/?envType=daily-question&envId=2023-10-17)

给你一个正整数 `n` ，请你计算在 `[1，n]` 范围内能被 `3或者5或者7` 整除的所有整数之和。

返回一个整数，用于表示给定范围内所有满足约束条件的数字之和。

利用等差数列求和公式：$1 \sim n 中 能被 x 整除的数之和 = (x + 2\cdot x+ \cdots + n//x \cdot x) = x \cdot(1 + n // x) * (n // x) // 2$

因而， 

```python
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        # 定义 f(x) 为能被 x 整除的数字之和
        def f(x):
            return x * (1 + n // x) * (n // x) // 2
        return f(3) + f(5) + f(7) - f(15) - f(21) - f(35) + f(105)
```

[3116. 单面值组合的第 K 小金额 - 力扣（LeetCode）](https://leetcode.cn/problems/kth-smallest-amount-with-single-denomination-combination/description/)

容斥 + 预处理最小公倍数：给定无重复集合 $coins'$，$1 \sim x$ 中，能对任意一个 $coins'$ 中元素整除的个数 为 $check(x)$。

将问题转换成，恰好能有 不少于 $k$  个数被任意一个 $coins'$ 中元素整除的 $x$ 的值，使用二分答案。回溯法枚举子集，预处理所有$coins'$ 子集的最小公倍数，所有相同长度、为$l$ 的子集的最小公倍数存放在 $dic[l]$ 中。 对于任意一个数 $y$ ，$1 \sim x$ 中能被它整除的个数为 $int(x/y)$。

```python
   def findKthSmallest(self, coins: List[int], k: int) -> int:
        coins.sort()
        if coins[0] == 1: return k
        c = set(coins)
        n = len(coins)
        for i in range(n):
            for j in range(i + 1, n):
                x, y = coins[i], coins[j]
                if y % x == 0 and y in c:
                    n -= 1
                    c.remove(y)
        coins = list(c)

        # 预处理：dic[i] 表示 从coins 中选出 i个数的子集的最小公倍数
        dic = defaultdict(list)
        dic[1] = coins

        # 回溯枚举子集
        path = []
        def dfs(i):
            l = len(path)
            if i == n:
                if l >= 2:
                    lcm_ = path[0]
                    for j in range(1, l):
                        lcm_ = lcm(lcm_, path[j])
                    dic[l].append(lcm_)
                return 
            dfs(i + 1)
            path.append(coins[i])
            dfs(i + 1)
            path.pop()
        dfs(0)
  
        def check(x):
            # 检查 1 ~ x 中，能被任意一个c 整除的个数res和k的关系
            res = 0
            for l in range(1, n + 1):
                plus = l & 1
                for d in dic[l]:    
                    res = res + (1 if plus else -1) * (x // d)
            return res >= k

        lo, hi = 0, 5 * 10 ** 10 + 10
        while lo < hi:
            mid = (lo + hi) >> 1
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo
```



### 鸽巢原理 / 抽屉原理

常用于求解最坏情况下的解，以及证明不存在解（连最坏情况下，都不存在解，则所有情况不存在解）。

**鸽巢原理定理**

有 $n+1$ 只鸽子，飞入 $n$ 个鸽子巢，则至少有一个巢里有不少于两只鸽子。（反证法：假设没有一个巢中有不少于两只鸽子，则鸽子总数不会超过 $n$， 矛盾）。即将 $n+1$ 个物体，划分成 $n$ 组，至少有一组有不少于两个物体。 

推广：将 $n$ 个物体，划分成 $k$ 组，至少有一组不少于 $\left\lceil \frac{n}{k} \right\rceil$。（证明：反证法，假设所有组少于  $\left\lceil \frac{n}{k} \right\rceil$，则至多  $(\left\lceil \frac{n}{k} \right\rceil - 1) \times k < (\frac{n}{k}) \times k=n$ 个物体，矛盾）

>  例如，53个物体，分成6组，最坏情况下是 9，9，9，9，9，8。

简单应用：

- 任意11个整数中，至少有2个整数之差是10的倍数。（证明，从余数角度来看，11个数对10的余数有11个，一共有10种余数 0 ~ 9，至少有两个数对10同余，故其差也对10同余）
- 一个人骑车10小时内走完了281公里路程，已知他第一小时走了30公里，最后一小时走了17公里。证明：他一定在某相继的两小时中至少走完了58公里路程。（证明：8小时走了234公里，234个物品分到8组，最坏情况下，至少有一组是 $\lceil \frac{234}{8} \rceil=29$公里，其余各组是 $28$ 公里，那么第一小时和第二小时一定至少有58公里）

**Ramsey定理 / 拉姆齐定理**

任意 $n$ 个人，必然有 $\lceil (n-1)/2 \rceil$ 个人相互认识 或者 相互不认识。（证明：考虑其中一个人的视角，剩下 n - 1个人需要划分成两组，$k1$ 表示与它认识，$k2$ 表示与他不认识，其中一组至少为  $\lceil (n-1)/2 \rceil$ 个人。）



**隔板法**

[Problem - 1205 (hdu.edu.cn)](https://acm.hdu.edu.cn/showproblem.php?pid=1205)

> Gardon 有$1\leq K\leq10^6$种糖果，第$i$种糖果有$1\leq a_i\leq10^6$个，Gradon 不喜欢连续两次吃同样种类的糖果，问是否存在可行的吃糖方案。

即给定 $K$ 组物品，各组物品个数有 $a_i$ 个，每次从任意一组种拿出一个，要求连续两个物品不能属于同一组。是否存在一种方案能拿完所有物品？

找到最大个数的数量 $N$, 其余物品数量之和为 $S$， 通过隔板法，当且仅当形成的$N-1$ 个右侧隔间每个至少有一个其他物品时满足条件。所以当 $S \ge N-1$ 成立，反之不成立。





## 数学公式

### 排序不等式

结论：$对于两个有序数组的乘积和，顺序和 \ge 乱序和 \ge 倒序和$。

$对于 a_1 \le a_2 \le \cdots \le a_n，b_1 \le b_2 \le \cdots \le b_n,并有c1,c2,\cdots, c_n是b1, b2, \cdots , b_n 的乱序排列。有如下关系： $
$$
\sum_{i = 1}^{n}a_ib_{n + 1 - i} \le \sum_{i=1}^{n}a_ic_i\le \sum_{i = 1}^{n}a_ib_i。\\
$$
$当且仅当 a_i = a_j 或者b_i = b_j \space (1 \le i, j\le n)时，等号成立。$

### 区间递增k个数

结论：对于$i_0 = a$，每次递增$k$，在区间$[a, b)$ 内的个数是：
$$
(b - a - 1) // k + 1
$$



###  平均数不等式

$$
x_1,x_2,\ldots,x_n\in\mathbb{R}_+\Rightarrow\frac n{\sum_{i=1}^n\frac1{x_i}}
\leq\sqrt[n]{\prod_{i=1}^nx_i}
\leq\frac{\sum_{i=1}^nx_i}n
\leq\sqrt{\frac{\sum_{i=1}^nx_i^2}n} 
\\
\text{当且仅当 }x_1=x_2=\cdots=x_n\text{,等号成立。}
$$

即：调和平均数 ，几何平均数，算术平均数，平方平均数 （调几算方）

应用：

例如当算术平均数为定值，$x_i$ 分布越接近，平方平均数越小，因此可以进行贪心算法：

[3081. 替换字符串中的问号使分数最小 - 力扣（LeetCode）](https://leetcode.cn/problems/replace-question-marks-in-string-to-minimize-its-value/description/) 
各个字母之间的出现次数的差异越小，越均衡，最终结果越小。可以基于贪心 + 堆进行维护，每次取出出现次数最小中字典序最小的字符。

```python
    def minimizeStringValue(self, s: str) -> str:
        cnt = Counter(s)
        hq = [(cnt[ch], ch) for ch in string.ascii_lowercase] 
        heapq.heapify(hq)
        alp = []
        res = list(s)
        for i in range(s.count('?')):
            v, k = heappop(hq)
            v += 1
            alp.append(k)
            heappush(hq, (v, k))
        alp.sort(reverse = True)
        for i, x in enumerate(res):
            if res[i] == '?':
                res[i] = alp.pop()
        return ''.join(res)
```

### 求和公式

$$
\Sigma_1^nn^2 = \frac{n \cdot (n + 1) \cdot (2n + 1)}{6}
$$

### 取模性质

模运算与基本四则运算有些相似，但是除法例外。其规则如下：
(a + b) % p = (a % p + b % p) % p
(a - b) % p = (a % p - b % p) % p
(a * b) % p = (a % p * b % p) % p
a ^ b % p = ((a % p)^b) % p
结合律：
((a+b) % p + c) % p = (a + (b+c) % p) % p
((a*b) % p \* c)% p = (a \* (b*c) % p) % p
交换律：
(a + b) % p = (b+a) % p
(a * b) % p = (b * a) % p
分配律：
(a+b) % p = ( a % p + b % p ) % p
((a +b)% p * c) % p = ((a * c) % p + (b * c) % p) % p

### 数列

**等比数列求和公式**
$$
S_n = \frac{a_1(1-q^n)}{1-q},~q \ne1
$$
**递推方法求等比数列求和（带模运算）**

希望求：$S(a,n) \mod p=(a^0+a^1+\cdots+a^n) \mod p$，不难发现$S(a,n)=a\cdot \big(S(a,n-1) \big) + 1$。

时间复杂度：$O(n)$

```python
def S(a, n):
    s0 = 1 
    for _ in range(n):
        s0 = (a * s0 + 1) % moder 
    return s0
```

## 组合数学

**排列**

$A_m^n = \frac{m!}{n!}$

$\mathrm{A}_n^m=n\mathrm{A}_{n-1}^{m-1}$

递推公式：可理解为“某特定位置”先安排，再安排其余位置。

```python
@lru_cache(None)
def A(n, m):
    if m == 0: return 1
    return n * A(n - 1, m - 1)
```



**组合数学**

$~ C_m^n = \frac{m!}{n!(m-n)!}$

$C_m^n = C_m^{m-n}$

递推公式：

$C_m^n = C_{m -1}^n + C_{m-1}^{n-1}$

```python
@lru_cache(None)
def C(n, m):
    if m == 0 or n == m: return 1
    return C(n - 1, m - 1) + C(n - 1, m)
```

$C_n^0+C_n^1 + \cdots+ C_n^n = 2 ^ n$



[62. 不同路径 - 力扣（LeetCode）](https://leetcode.cn/problems/unique-paths/description/)

路径方案数 $= C(n+m-2,m-1)$

```python
@lru_cache(None)
def C(n, m):
    if m == 0 or n == m: return 1
    return C(n - 1, m - 1) + C(n - 1, m)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m, n = m - 1, n - 1
        return C(m + n, m)
```





### 二项式定理

$$
(a + b) ^n = \sum_{i=0}^n C_n^ia^ib^{n-i}
$$

### 卡特兰数

[5. 卡特兰数（Catalan）公式、证明、代码、典例._c n = n+11 ( n2n )-CSDN博客](https://blog.csdn.net/sherry_yue/article/details/88364746)
$$
给定 ~n ~ 个0 和 ~n~ 个1，排序成长度为2n 的序列。其中任意前缀中0的个数都不少于1的个数的序列的数量为：
\\
H(n) = C_{2n}^n-C_{2n}^{n-1} = \frac{C_{2n}^n}{n+1} = \frac{(2n)!}{(n + 1)!n!}
$$
![image.png](https://pic.leetcode.cn/1712921693-mUZiol-image.png)



证明方法：

看成从从 $(0,~ 0)$ 到 右上角 $(n, ~n )$，每次只能向右或者向上，向上的次数不超过向右的次数的路径数。

对于不合法的情况，超过 $y = x$ ，即一定触碰 $y = x + 1$， 取路径与$y = x + 1$ 交点中，距离原点最近的点，将路径远离原点的部分关于$y = x + 1$ 翻转。由于原来的终点 $(n,n)$ 关于 $y = x + 1$ 翻转的点是$(n - 1, n + 1) $ ，所以不合法的路径数是 $C_{2n}^{n-1}$

**递推公式1：**
$$
H(n+1) = H(0)\cdot H(n) + H(1)\cdot H(n - 1) + \cdots +H(n)\cdot H(0) = \sum_{i=0}^{n} H(i)\cdot H(n-i)
$$
证明方法：从 $(0, 0)$ 到 $(n +1, n+1)$ 的路径数可以看成分三步：

首先从 $(0,0)$ 走到 $(i,i)$ ，其方案数为 $H(i)$；然后从 $(i,i)$ 走到 $(n,n)$ 方案数为 $H(n-i)$；最后从 $(n,n)$ 走到 $(n + 1, n + 1)$ 其方案数为 $H(1)$ = 1。

**递推公式2：**
$$
H(n) = H(n-1) \cdot \frac{2n(2n - 1)}{(n+1)n} = H(n-1) \cdot \frac{(4n - 2)}{(n+1)}
$$


**推论：**

前几项:  1,1,2,5,14,42,132,429,1430

- $n$ 个节点可以构造的不同的二叉树的个数。（证明：$F(n) $为有n个节点的二叉树的所有根节点个数。其左子树的可能情况为 $F(i), i \in [0,n], $对应右子树的情况为 $F(n-i),$ 乘积求和形式即为卡特兰数列的递推式。
- 从 $(0,~ 0)$ 到 右上角 $(n, ~n )$，每次只能向右或者向上，向上的次数不超过向右的次数的路径数。（即不超过 $y = x$ ）
- 一个无穷大栈，进栈顺序为 $1, 2, ... , n$ 的出栈顺序数
- $n$ 个左括号和 $n$ 个右括号构成的括号序列，能够构成的有效括号序列个数。



凸多边形划分问题

**在一个n边形中，通过不相交于n边形内部的对角线，把n边形拆分为若干个三角形，问有多少种拆分方案？**

![image.png](https://pic.leetcode.cn/1712073924-PFLnSL-image.png)

以凸多边形的一边为基，设这条边的2个顶点为A和B。从剩余顶点中选1个，可以将凸多边形分成三个部分，中间是一个三角形，左右两边分别是两个凸多边形，然后求解左右两个凸多边形。

2.设问题的解f(n)，其中n表示顶点数，那么f(n)=f(2)*f(n-1)+f(3)*f(n-2)+……+f(n-2)*f(3)+f(n-1)*f(2)。
其中，f(2)*f(n-1)表示：三个相邻的顶点构成一个三角形，另外两个部分的顶点数分别为2（一条直线两个点）和n-1。
其中，f(3)*f(n-2)表示：将凸多边形分为三个部分，左右两边分别是一个有3个顶点的三角形和一个有n-2个顶点的多边形。

3.设f(2) = 1，那么f(3) = 1, f(4) = 2, f(5) = 5。结合递推式，不难发现f(n) 等于H(n-2)。



## 快速幂

**欧拉降幂 / 快速幂**

```python
def pow(a, n, moder):
    res = 1
    while n:
        if n & 1: res = (res * a) % moder
        n >>= 1
        a = (a * a) % moder
    return res
```



> 矩阵乘法时间复杂度：$O(M_1N_2N_1)$

**矩阵乘法**

```python
moder = 10**9 + 7

def mul(a, b):
    m_a, n_a = len(a), len(a[0])
    m_b, n_b = len(b), len(b[0])
    c = n_a  # 可以加一个n_a和m_b的判等
    res = [[0]*n_b for _ in range(m_a)]
    for i in range(m_a):
        for j in range(n_b):
            tmp = 0
            for k in range(c):
                # tmp = (tmp + (a[i][k] * b[k][j]) % moder) % moder  # 如果需要取模
                tmp += a[i][k] * b[k][j]
            res[i][j] = tmp
    return res
```

### 矩阵快速幂

```python
moder = 10 ** 9 + 7

def mul(a, b):
    ma, na = len(a), len(a[0])
    mb, nb = len(b), len(b[0])
    # ma * nb 
    c = na 
    res = [[0] * nb for _ in range(ma)]
    for i in range(ma):
        for j in range(nb):
            tmp = 0
            for k in range(na):
                tmp = (tmp + a[i][k] * b[k][j] % moder) % moder 
            res[i][j] = tmp 
    return res 

def mat_pow(a, n):
    res = [[6, 6]]
    while n:
        if n & 1: res = mul(res, a)
        a = mul(a, a)
        n >>= 1
    return res
```



[1411. 给 N x 3 网格图涂色的方案数 - 力扣（LeetCode）](https://leetcode.cn/problems/number-of-ways-to-paint-n-3-grid/description/?envType=featured-list&envId=ptud3zoQ?envType=featured-list&envId=ptud3zoQ)

递推方程：$f(0)=(6, 6),~f(i)=(f(i-1,0) \times 2+f(i-1,1)\times 2,~~f(i-1,0) \times 2 + f(i-1,1)\times3)$。

即：
$$
\left[\begin{array}{c}
f(n,0) \\
f(n,1)
\end{array}\right]

=
\left[\begin{array}{c}
6 \\
6
\end{array}\right]
\cdot 

\left[\begin{array}{c}
2 & 2 \\
2 & 3
\end{array}\right]^{n-1}
$$

```python
moder = 10 ** 9 + 7

def mul(a, b):
    ma, na = len(a), len(a[0])
    mb, nb = len(b), len(b[0])
    # ma * nb 
    c = na 
    res = [[0] * nb for _ in range(ma)]
    for i in range(ma):
        for j in range(nb):
            tmp = 0
            for k in range(na):
                tmp = (tmp + a[i][k] * b[k][j] % moder) % moder 
            res[i][j] = tmp 
    return res 

def mat_pow(a, n):
    res = [[6, 6]]
    while n:
        if n & 1: res = mul(res, a)
        a = mul(a, a)
        n >>= 1
    return res
class Solution:
    def numOfWays(self, n: int) -> int:
        m = [[2, 2],
             [2, 3]]
        x = mat_pow(m, n - 1)
        return sum(x[0]) % moder
```



## 高等数学

### 调和级数

$$
\sum_{i=1}^{n} \frac{1}{k} 是调和级数，其发散率表示为\sum_{i=1}^{n} \frac{1}{k} = \ln n + C
$$

 经典应用：求一个数的约数的个数期望值

- 考虑 1~n 所有的数的约数个数。
- 从筛法的角度来看，拥有约数2的所有的数，是 1 ~ n中所有2的倍数，大约是 n // 2个。
- 所以 1~n所有的数的约数个数和 可以看成 所有的倍数的个数 = $n/1 + n / 2 + n /3 + \cdots + n / n = n \sum_{i=1}^n\frac{1}{i} = n \ln n。$
- 所以=，从期望角度来讲，一个数$n$ 的约束个数的期望约是 $\ln n$

### 泰勒展开式

$$
f(x)=f(x_0)+\frac{f'(x_0)}{1!}(x-x_0)+\frac{f''(x_0)}{2!}(x-x_0)^2+\cdots+\frac{f^{(n)}(x_0)}{n!}(x-x_0)^n+R_n
$$

**麦克劳林公式：$x_0 = 0$** 
$$
f(x) = \sum_{k=0}^{n} \frac{f^{(k)}(0)}{k!} \cdot x^k + o(x^n) = f(0) + \frac{f'(0)}{1!} \cdot x + \frac{f''(0)}{2!} \cdot x^2 + \cdots+\frac{f^{(n)}(0)}{n!} \cdot x^n + o(x^n)
$$
常用展开：
$$
e^x = 1+\frac{1}{1!} \cdot x + \frac{1}{2!} \cdot x^2 + \cdots +\frac{1}{n!} \cdot x^n + o(x^n)
$$
所以有：
$$
e = \frac{1}{0!} + \frac{1}{1!} + \frac{1}{2!} + \cdots + \frac{1}{n!} 
$$

### Stirling 斯特林公式

描述阶乘的近似阶：
$$
n!=\sqrt{2\pi n}(\frac n{e})^{n}
$$
所以可以得到卡特兰数列的近似：
$$
O(C_n) \sim O(\frac{4^n}{n^{\frac{3}{2}} \cdot\sqrt \pi})
$$


# 数据结构



## 并查集

合并和查询的时间复杂度： 近似 $O(1)$

`find(u) == find(v)` 表示u, v在同一集合。

**路径压缩**

递归写法

```python
    fa = list(range(n))
    # 查找x集合的根
    def find(x):
        if fa[x] != x:
            fa[x] = find(fa[x])
        return fa[x]

    # v并向u中Z
    def union(u, v):
        if find(u) != find(v):
	        fa[find(v)] = find(u)
```

迭代写法

```python
fa = list(range(n))

def find(x):
    root = x
    while fa[root] != root:
        root = fa[root]
    while fa[x] != x: # 路径压缩
        x, fa[x] = fa[x], root
    return root

def union(u, v):
    root_u = find(u)
    root_v = find(v)
    if root_u != root_v:
        fa[root_v] = root_u
```



常用拓展：

- 记录每个集合大小：绑定到根节点
- 记录每个点到根节点的**距离**：绑定到每一个节点上



**并查集维护连通分量**

[1998. 数组的最大公因数排序 - 力扣（LeetCode）](https://leetcode.cn/problems/gcd-sort-of-an-array/)

 质因子分解 + 并查集判断连通分量。

将所有数看成一个图中的节点。任意两个数 $u, v$ ， 如果不互质（gcd>1) 说明存在一条边$ u \sim v$。显然一种做法是用$O(n^2)$ 的时间维护所有节点对应的连通块。然而，实际上只需要对每个数$x$ 和它的所有质因子进行合并，这样可以保证有相同质因子的两个元素，他们可以在同一个连通分量。

记数组中最大值$ m = max(nums)$,  可以看成一个 有 m 个节点的图。每次质因子分解的时间复杂度是$O(\sqrt x)$ ，所以从 $O(n^2)$   优化到 $O(n \sqrt m)$。最后，将排序好的数组和原数组对应位置上的元素进行对比。判断两个元素是否同属于一个连通分量即可。

时间复杂度：$O\bigg(n\big(\sqrt m \cdot \alpha(m) \big) +n\log n \bigg ) $

```python
    def gcdSort(self, nums: List[int]) -> bool:
        n = len(nums)
        fa = list(range(max(nums) + 1))	
        def find(x):    # x 压缩到 fa[x] 中
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]
        def union(u, v):    # u 合并到 v 中
            if find(u) != find(v):
                fa[find(u)] = find(v)
        
        for i, x in enumerate(nums):
            xx = x
            for j in range(2, int(sqrt(x)) + 1):
                if x % j == 0:
                    union(j, xx)
                    while x % j == 0:
                        x //= j
            if x > 1:
                union(x, xx)
        sorted_nums = sorted(nums)
        for u, v in zip(nums, sorted_nums):
            if u == v: continue 
            # 不在位元素，需要看是否在同一连通分量
            if find(u) != find(v): return False
        return True
```

[952. 按公因数计算最大组件大小 - 力扣（LeetCode）](https://leetcode.cn/problems/largest-component-size-by-common-factor/description/?envType=featured-list&envId=GklvgyNg?envType=featured-list&envId=GklvgyNg)

```python
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        m = max(nums)
        fa = list(range(m + 1))
        def find(x):
            if fa[x] != x: 
                fa[x] = find(fa[x])
            return fa[x]
        def union(u, v):
            if find(u) != find(v):
                fa[find(u)] = find(v)
        for x in nums:
            xx = x
            for j in range(2, int(sqrt(x)) + 1):
                if x % j == 0:
                    union(xx, j)
                    while x % j == 0:
                        x //= j
            if x > 1:
                union(xx, x)
        for x in nums:
            find(x)
        cnt = Counter()
        for x in nums: cnt[fa[x]] += 1
        return max(cnt.values())    
```



**并查集维护连通块大小 ** 

模板代码：

```python
        fa = list(range(n + 1))
        siz = [1] * (n + 1)
        def find(x):
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]
        def union(u, v):
            if find(u) != find(v):
                siz[find(v)] += siz[find(u)]
                fa[find(u)] = find(v)
```



[765. 情侣牵手 - 力扣（LeetCode）](https://leetcode.cn/problems/couples-holding-hands/description/)

诸如 $(0,1), (1, 2), (2, 3), (3,1)$ 应该视作一个连通块内，其交换次数为连通块大小 - 1。

```python
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)
        fa = list(range(n + 1))
        siz = [1] * (n + 1)
        def find(x):
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]
        def union(u, v):
            if find(u) != find(v):
                siz[find(v)] += siz[find(u)]
                fa[find(u)] = find(v)
        s = set()
        for i in range(0, n, 2):
            p = i // 2
            l, r = row[i] // 2, row[i + 1] // 2
            if l == r: continue 
            union(l, r)
        for x in row:
            s.add(find(x // 2))
        res = 0
        for x in s:
            res += siz[find(x)] - 1
        return res  
```



[2867. 统计树中的合法路径数目 - 力扣（LeetCode）](https://leetcode.cn/problems/count-valid-paths-in-a-tree/description/?envType=featured-list&envId=4eH5fI7k?envType=featured-list&envId=4eH5fI7k)

并查集维护所有非质数子连通块的大小。

```python
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        primes = []
        N = n + 10
        is_prime = [True] * N
        is_prime[0] = is_prime[1] = False
        for i in range(2, N):
            if is_prime[i]:
                primes.append(i)
            for p in primes:
                if i * p >= N:
                    break
                is_prime[i * p] = False
                if i % p == 0:
                    break
        e = [[] for _ in range(n + 1)]
        fa = list(range(n + 1))
        siz = [1] * (n + 1)
        def find(x):
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]
        def union(u, v):    # u 合并到 v
            if find(u) != find(v):
                siz[find(v)] += siz[find(u)]
                fa[find(u)] = find(v)
        
        for u, v in edges:
            e[u].append(v)
            e[v].append(u)
            if not is_prime[u] and not is_prime[v]:
                union(u, v)
        res = 0
        vis = [False] * (n + 1) 
        for u in range(1, n + 1):
            if not vis[u] and is_prime[u]:
                # 遍历 u 的所有非质数连通块
                vis[u] = True
                cur_siz = 0
                for v in e[u]:
                    if not is_prime[v]:
                        sz = siz[find(v)]
                        res += sz + sz * cur_siz 
                        cur_siz += sz 
        return res

```

**并查集维护连通块按位与的值**

[100244. 带权图里旅途的最小代价 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-cost-walk-in-weighted-graph/description/)

```python
def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        fa = list(range(n))
        cc_and = [-1] * n
        def find(x):
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]
        def union(u, v, w):    # v 合并到 u 中
            if find(u) != find(v):
                cc_and[find(u)] &= cc_and[find(v)]
                fa[find(v)] = find(u)
        for u, v, w in edges:
            # 各自连通块内更新，只要更新其一即可
            cc_and[find(u)] &= w
            union(u, v, w)
        return [0 if u == v else (-1 if find(u) != find(v) else cc_and[find(u)]) for u, v in query]
```

**并查集维护链**

把考虑过的元素串起来，链条的长度就是当前一段数的长度。关键需要高效串联两条链。

[2334. 元素值大于变化阈值的子数组 - 力扣（LeetCode）](https://leetcode.cn/problems/subarray-with-elements-greater-than-varying-threshold/description/?envType=featured-list&envId=GklvgyNg?envType=featured-list&envId=GklvgyNg)

时间复杂度：$O(nlogn)$

对$nums$ 中每一个元素和对应的下标 按照降序排序，每次向右合并，当前的 $x$ 一定是子数组中最小的。返回合并后并查集大小$k - 1$（ 减一使得不包含哨兵根节点）。不断向右侧合并直到出现符合的。

```python
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        fa = list(range(n + 1))
        siz = [1] * (n + 1)
        def find(x):
            if fa[x] != x: fa[x] = find(fa[x])
            return fa[x]
        def union(u, v):    # v 合并到 u中
            if find(u) != find(v):
                siz[find(u)] += siz[find(v)]
                fa[find(v)] = find(u)
        for x, i in sorted(zip(nums, range(n)), reverse = True):
            union(i, i + 1)
            k = siz[find(i)] - 1
            if x > (threshold / k): return k
        return -1
```



## 字典树

### 26叉字典树

```python
class Trie:

    def __init__(self):
        self.is_end = False
        self.next = [None] * 26

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.next[idx]:
                node.next[idx] = Trie()
            node = node.next[idx]
        node.is_end = True            

    def search(self, word: str) -> bool:
        node = self
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.next[idx]:
                return False
            node = node.next[idx]
        return node.is_end    

    def startsWith(self, prefix: str) -> bool:
        node = self
        for ch in prefix:
            idx = ord(ch) - ord('a')
            if not node.next[idx]:
                return False
            node = node.next[idx]
        return True

```

### 哈希字典树

```python
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        class Node:
            __slots__ = 'children', 'cnt'
            def __init__(self):
                self.children = {}  # 用字典的字典树
                self.cnt = 0
        res = 0
        root = Node()   # 树根
        for word in words:  
            cur = root 
            for p in zip(word, word[::-1]): # (p[i], p[n - i - 1])
                if p not in cur.children:   
                    cur.children[p] = Node()
                cur = cur.children[p]       
                res += cur.cnt 
            cur.cnt += 1
        return res
```

```python
class Trie:

    def __init__(self):
        self.end = False
        self.next = {}

    def insert(self, word: str) -> None:
        p = self 
        for ch in word:
            if ch not in p.next:
                p.next[ch] = Trie()
            p = p.next[ch]
        p.end = True 

    def search(self, word: str) -> bool:
        p = self 
        for ch in word:
            if ch not in p.next:
                return False 
            p = p.next[ch]
        return p.end

    def startsWith(self, prefix: str) -> bool:
        p = self 
        for ch in prefix:
            if ch not in p.next:
                return False 
            p = p.next[ch]
        return True        



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```



## 线段树

### lazy线段树

- 支持单点修改 / 区间修改 / 区间查询

- 支持最小/最大/求和

```python
class SegmentTree:
    __slots__ = ['node', 'lazy', 'n', 'nums', 'op', 'ini', 'ops']

    def __init__(self, nums, ops = 'sum'):
        n = len(nums)
        if ops == 'sum' or ops == 'bin':
            op, ini = lambda a, b: a + b, 0
        elif ops == 'max':
            op, ini = lambda a, b: max(a, b), -inf
        elif ops == 'min':  
            op, ini = lambda a, b: min(a, b), inf
        self.nums = nums
        self.op = op
        self.ini = ini
        self.ops = ops 
        self.node = [ini] * (4 * n)
        self.lazy = [None] * (4 * n)
        self.n = n

    def build(self, idx = 1, l = 1, r = None):
        if r is None: r = self.n
        if l == r:
            self.node[idx] = self.nums[l - 1]
            return
        mid = (l + r) >> 1
        self.build(idx << 1, l, mid)
        self.build((idx << 1) + 1, mid + 1, r)

        self.node[idx] = self.op(self.node[idx << 1], self.node[(idx << 1) + 1])

    def do(self, idx, dl, dr, val = None):
        if self.ops == 'bin':
            self.node[idx] = dr - dl + 1 
            self.lazy[idx] = True
        elif self.ops == 'sum':
            self.node[idx] = self.op(self.node[idx], (dr - dl + 1) * val)
            self.lazy[idx] = val
        else:
            self.node[idx] = self.op(val, self.node[idx])
            self.lazy[idx] = val

    def pushdown(self, idx, pl, pr):
        val = self.lazy[idx]
        mid = (pl + pr) >> 1
        self.do(idx << 1, pl, mid, val)
        self.do((idx << 1) + 1, mid + 1, pr, val)
        self.lazy[idx] = None

    def update(self, ul, ur, val, idx = 1, l = 1, r = None):
        if r is None:r = self.n
        if ul <= l and r <= ur:
            self.do(idx, l, r, val)
            return
        if self.lazy[idx]:
            self.pushdown(idx, l, r)
        mid = (l + r) >> 1
        if ul <= mid: self.update(ul, ur, val, idx << 1, l, mid)
        if ur > mid: self.update(ul, ur, val, (idx << 1) + 1, mid + 1, r)

        self.node[idx] = self.op(self.node[idx << 1], self.node[(idx << 1) + 1])

    def query(self, ql, qr, idx = 1, l = 1, r = None):
        if r is None: r = self.n
        if ql <= l and r <= qr:
            return self.node[idx]

        if self.lazy[idx]:
            self.pushdown(idx, l, r)

        mid = (l + r) >> 1
        ansl, ansr = self.ini, self.ini
        if ql <= mid: ansl = self.query(ql, qr, idx << 1, l, mid)
        if qr > mid:ansr = self.query(ql, qr, (idx << 1) + 1, mid + 1, r)
        return self.op(ansl, ansr)

```

> ```python
> tr = SegmentTree([1, 2, 3, 4, 5], 'sum')
> tr.build()
> print(tr.query(1, 5))  # 15
> print(tr.query(2, 5))  # 14
> tr.update(2, 4, 2)  # 1 4 5 6 5
> print(tr.query(2, 5))  # 20
> 
> 
> tr = SegmentTree([8, 4, 5, 7, 9], 'min')
> tr.build()
> print(tr.query(1, 4)) # 4
> tr.update(1, 4, 5) # [5, 4, 5, 5, 9]
> print(tr.query(4, 5)) # 5
> tr.update(3, 5, -10) # [5, 4, -10, -10, -10]
> print(tr.query(1, 3)) # -10
> ```



lazy 线段树（01翻转）

```python
class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums1)
        node = [0] * (4 * n)
         # 懒标记：True表示该节点代表的区间被曾经被修改，但是其子节点尚未更新
        lazy = [False] * (4 * n)

        # 初始化线段树
        def build(i = 1, l = 1, r = n):
            if l == r:
                node[i] = nums1[l - 1]
                return 
            mid = (l + r) >> 1
            build(i * 2, l, mid)
            build(i * 2 + 1, mid + 1, r)
             # 维护区间 [l, r] 的值
            node[i] = node[i * 2] + node[i * 2 + 1]
        
        
        # 更新节点值，并设置lazy标记
        def do(i, l, r):
            node[i] = r - l + 1 - node[i]
            lazy[i] = not lazy[i]
        

        # 区间更新：本题中更新区间[l, r] 相当于做翻转
        def update(L, R, i = 1, l = 1, r = n):
            if L <= l and r <= R:
                do(i, l, r)
                return 
            
            mid = (l + r) >> 1
            if lazy[i]:
                # 根据标记信息更新p的两个左右子节点，同时为子节点增加标记
                # 然后清除当前节点的标记
                do(i * 2, l, mid)
                do(i * 2 + 1, mid + 1, r)
                lazy[i] = False
        
            if L <= mid:
                update(L, R, i * 2, l, mid)
            if R > mid:
                update(L, R, i * 2 + 1, mid + 1, r)
            
            # 更新节点值
            node[i] = node[i * 2] + node[i * 2 + 1]
        
        build()

        res, s = [], sum(nums2)
        for op, L, R in queries:
            if op == 1:
                update(L + 1, R + 1)
            elif op == 2:
                s += node[1] * L 
            else:
                res.append(s)
        return res
```



### lazy线段树（带动态开点）

```python
class Node:
    __slots__ = ['l', 'r', 'lazy', 'val']

    def __init__(self, val = 0):
        self.l = None
        self.r = None
        self.lazy = None
        self.val = val

class SegmentTree:
    __slots__ = ['root', 'node', 'op', 'ini', 'ops', 'max_val']

    def __init__(self, ops: str = 'sum', max_val: int = int(1e9)):
        if ops == 'sum' or ops == 'bin':
            op, ini = lambda a, b: a + b if a is not None else b, 0
        elif ops == 'max':
            op, ini = lambda a, b: max(a, b), -inf
        elif ops == 'min':
            op, ini = lambda a, b: min(a, b), inf
        self.root = Node(ini)
        self.op = op
        self.ini = ini
        self.ops = ops
        self.max_val = max_val

    def __do(self, node, dl, dr, val = None):
        if self.ops == 'bin':
            node.val = dr - dl + 1
            node.lazy = True
        elif self.ops == 'sum':
            node.val = self.op(node.val, (dr - dl + 1) * val)
            node.lazy = self.op(node.lazy, val)
        else:
            node.val = self.op(node.val, val)
            node.lazy = val


    # 下放lazy标记。如果是孩子为空，则动态开点
    def __pushdown(self, node, pl, pr):
        val = node.lazy


        # 根据lazy标记信息，更新左右节点，然后将lazy信息清除
        mid = (pl + pr) >> 1
        self.__do(node.l, pl, mid, val)
        self.__do(node.r, mid + 1, pr, val)
        node.lazy = None

    def update(self, ul, ur, val, node = None, l = 1, r = None):
        # 查询默认从根节点开始
        if node is None: node = self.root
        if r is None: r = self.max_val

        if ul <= l and r <= ur:
            self.__do(node, l, r, val)
            return

        if node.l is None: node.l = Node(self.ini)
        if node.r is None: node.r = Node(self.ini)
        # 下放标记、根据标记信息更新左右节点，然后清除标记
        if node.lazy is not None:
            self.__pushdown(node, l, r)

        mid = (l + r) >> 1
        if ul <= mid: self.update(ul, ur, val, node.l, l, mid)
        if ur > mid: self.update(ul, ur, val, node.r, mid + 1, r)
        # node.val 为 True 表示这个节点所在区间，均被“跟踪”
        node.val = self.op(node.l.val, node.r.val)

    def query(self, ql, qr, node = None, l = 1, r = None):
        # 查询默认从根节点开始
        if node is None: node = self.root
        if r is None: r = self.max_val

        if ql <= l and r <= qr:
            return node.val

        if node.l is None: node.l = Node(self.ini)
        if node.r is None: node.r = Node(self.ini)

        # 下放标记、根据标记信息更新左右节点，然后清除标记
        if node.lazy is not None:
            self.__pushdown(node, l, r)

        mid = (l + r) >> 1
        ansl, ansr = self.ini, self.ini
        if ql <= mid: ansl = self.query(ql, qr, node.l, l, mid)
        if qr > mid: ansr = self.query(ql, qr, node.r, mid + 1, r)
        return self.op(ansl, ansr)
```

```python
tr = SegmentTree('sum')
tr.update(1, 10, 99)
tr.update(1, 4, 1)
tr.update(5, 10, 1)
print(tr.query(1, 1))  # 100
print(tr.query(1, 10))  # 1000

```



[699. 掉落的方块 - 力扣（LeetCode）](https://leetcode.cn/problems/falling-squares/description/?envType=daily-question&envId=2024-07-28)

```python
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        tr = SegmentTree('max', int(1e8))
        res = []
        for l, sz in positions:
            r = l + sz - 1
            mxh = tr.query(l, r) + sz
            tr.update(l, r, mxh)
            res.append(tr.query(1, int(1e8)))
        return res
```





### 递归动态开点（无lazy) 线段树

区间覆盖统计问题，区间覆盖不需要重复操作，不需要进行lazy传递

但是数据范围较大，需要动态开点

```python
# https://leetcode.cn/problems/count-integers-in-intervals
class CountIntervals:
    __slots__ = 'left', 'right', 'l', 'r', 'val'

    def __init__(self, l = 1, r = int(1e9)):
        self.left = self.right = None
        self.l, self.r, self.val = l, r, 0


    def add(self, l: int, r: int) -> None:

        # 覆盖区间操作，不需要重复覆盖，饱和区间无需任何操作
        if self.val == self.r - self.l + 1: 
            return  

        if l <= self.l and self.r <= r:  # self 已被区间 [l,r] 完整覆盖，不再继续递归
            self.val = self.r - self.l + 1
            return
        
        
        mid = (self.l + self.r) >> 1
        
        # 动态开点
        if self.left is None: 
            self.left = CountIntervals(self.l, mid)  # 动态开点
        
        if self.right is None: 
            self.right = CountIntervals(mid + 1, self.r)  # 动态开点
        
        if l <= mid: 
            self.left.add(l, r)
        if mid < r: 
            self.right.add(l, r)
        
        # self.val 的值，表示区间[self.l, self.r] 中被覆盖的点的个数
        self.val = self.left.val + self.right.val

    def count(self) -> int:
        return self.val

```



### 动态开点 + lazy 线段树 （旧版）			

```python
# https://leetcode.cn/problems/range-module/
class Node:
    __slots__ = ['l', 'r', 'lazy', 'val']
    def __init__(self):
        self.l = None
        self.r = None
        self.lazy = 0
        self.val = False
class SegmentTree:
    __slots__ = ['root']
    def __init__(self):
        self.root = Node()


    def do(self, node, val):
        node.val = val
        node.lazy = 1

    # 下放lazy标记。如果是孩子为空，则动态开点
    def pushdown(self, node):
        if node.l is None:
            node.l = Node()
        if node.r is None:
            node.r = Node()
        
        # 根据lazy标记信息，更新左右节点，然后将lazy信息清除
        if node.lazy:
            self.do(node.l, node.val)
            self.do(node.r, node.val)
            node.lazy = 0

    def query(self, L, R, node = None, l = 1, r = int(1e9)):
        
        # 查询默认从根节点开始
        if node is None:
            node = self.root
        
        if L <= l and r <= R:
            return node.val

        # 下放标记、根据标记信息更新左右节点，然后清除标记
        self.pushdown(node)

        mid = (l + r) >> 1
        
        vl = vr = True
        
        if L <= mid:
            vl = self.query(L, R, node.l, l, mid)
        if R > mid:
            vr = self.query(L, R, node.r, mid + 1, r)
        return vl and vr
    
    
    def update(self, L, R, val, node = None, l = 1, r = int(1e9)):
        
        # 查询默认从根节点开始
        if node is None:
            node = self.root

        if L <= l and r <= R:
            self.do(node, val)
            return 

        mid = (l + r) >> 1

         # 下放标记、根据标记信息更新左右节点，然后清除标记
        self.pushdown(node)

        if L <= mid:
            self.update(L, R, val, node.l, l, mid)
        if R > mid:
            self.update(L, R, val, node.r, mid + 1, r)

        # node.val 为 True 表示这个节点所在区间，均被“跟踪”
        node.val = bool(node.l and node.l.val and node.r and node.r.val)


class RangeModule:

    def __init__(self):
        self.tree = SegmentTree()

    def addRange(self, left: int, right: int) -> None:
        self.tree.update(left, right - 1, True)

    def queryRange(self, left: int, right: int) -> bool:
        return self.tree.query(left, right - 1)

    def removeRange(self, left: int, right: int) -> None:
        self.tree.update(left, right - 1, False)


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
```

[LCP 32. 批量处理任务 - 力扣（LeetCode）](https://leetcode.cn/problems/t3fKg1/description/)

```python
class SegmentTree:
    __slots__ = ['node', 'lazy', 'n', 'nums', 'op', 'ini', 'ops']
    def __init__(self, nums, ops='sum'):
        if ops == 'sum' or ops == 'bin':
            self.op, self.ini = lambda a, b: a + b, 0
        elif ops == 'max':
            self.op, self.ini = lambda a, b: max(a, b), -float('inf')
        elif ops == 'min':
            self.op, self.ini = lambda a, b: min(a, b), float('inf')
        
        self.nums = nums
        self.ops = ops
        self.n = len(nums)
        self.node = {}
        self.lazy = {}
    
    def build(self, idx=1, l=1, r=None):
        if r is None:
            r = self.n
        if l == r:
            self.node[idx] = self.nums[l - 1]
            return
        mid = (l + r) >> 1

        self.build(idx << 1, l, mid)
        self.build((idx << 1) + 1, mid + 1, r)

        self.node[idx] = self.op(self.node.get(idx << 1, self.ini), self.node.get((idx << 1) + 1, self.ini))
    
    def do(self, idx, dl, dr, val=None):
        if self.ops == 'bin':
            self.node[idx] = dr - dl + 1
            self.lazy[idx] = True
        else:
            self.node[idx] = self.op(val, self.node.get(idx, self.ini))
            self.lazy[idx] = val
    
    def pushdown(self, idx, pl, pr):
        if idx not in self.lazy:
            return
        val = self.lazy[idx]
        mid = (pl + pr) >> 1
        if idx << 1 not in self.node:
            self.node[idx << 1] = self.ini
        if (idx << 1) + 1 not in self.node:
            self.node[(idx << 1) + 1] = self.ini
        self.do(idx << 1, pl, mid, val)
        self.do((idx << 1) + 1, mid + 1, pr, val)
        del self.lazy[idx]
    
    def update(self, ul, ur, val, idx=1, l=1, r=None):
        if r is None:
            r = self.n
        
        if ul <= l and r <= ur:
            self.do(idx, l, r, val)
            return
        
        self.pushdown(idx, l, r)

        mid = (l + r) >> 1
        if ul <= mid:
            self.update(ul, ur, val, idx << 1, l, mid)
        if ur > mid:
            self.update(ul, ur, val, (idx << 1) + 1, mid + 1, r)

        self.node[idx] = self.op(self.node.get(idx << 1, self.ini), self.node.get((idx << 1) + 1, self.ini))
    
    def query(self, ql, qr, idx=1, l=1, r=None):
        if r is None:
            r = self.n
        if ql <= l and r <= qr:
            return self.node.get(idx, self.ini)
        
        self.pushdown(idx, l, r)

        mid = (l + r) >> 1
        ansl, ansr = self.ini, self.ini
        if ql <= mid:
            ansl = self.query(ql, qr, idx << 1, l, mid)
        if qr > mid:
            ansr = self.query(ql, qr, (idx << 1) + 1, mid + 1, r)
        return self.op(ansl, ansr)
    
    def update_suffix(self, ul, ur, val, idx=1, l=1, r=None):
        if r is None:
            r = self.n
        siz = r - l + 1
        if ul <= l and r <= ur and siz - self.node.get(idx, 0) <= val:
            ans = siz - self.node.get(idx, 0)
            self.do(idx, l, r)
            return ans
        mid = (l + r) >> 1
        self.pushdown(idx, l, r)
        ans = 0
        if ur > mid:
            ans = self.update_suffix(ul, ur, val, (idx << 1) + 1, mid + 1, r)
        val -= ans
        if val and ul <= mid:
            ans += self.update_suffix(ul, ur, val, idx << 1, l, mid)
        self.node[idx] = self.op(self.node.get(idx << 1, self.ini), self.node.get((idx << 1) + 1, self.ini))
        return ans

class Solution:
    def processTasks(self, nums):
        nums.sort(key=lambda x: x[1])
        n, m = len(nums), nums[-1][1]
        tr = SegmentTree([0] * (m + 1), 'bin')
        for l, r, c in nums:
            l, r = l + 1, r + 1
            c -= tr.query(l, r)
            if c > 0:
                tr.update_suffix(l, r, c)
        return tr.query(0, m + 1)
```



### 

### 线段树优化问题

[2617. 网格图中最少访问的格子数 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-number-of-visited-cells-in-a-grid/description/?envType=daily-question&envId=2024-03-22)

单点修改 + 区间最小值查询

```python
class SegmentTree:
    def __init__(self, n: int):
        self.n = n
        self.tree = [inf] * (4 * n)

    def op(self, a, b):
        return min(a, b)

    def update(self, ul, ur, val, idx = 1, l = 1, r = None):
        if r is None: r = self.n
        if ul <= l and r <= ur:
            self.tree[idx] = val
            return
        mid = (l + r) >> 1
        if ul <= mid:self.update(ul, ur, val, idx * 2, l, mid)
        if ur > mid: self.update(ul, ur, val, idx * 2 + 1, mid + 1, r)
        self.tree[idx] = self.op(self.tree[idx * 2], self.tree[idx * 2 + 1])  # 更新当前节点的值

    def query(self, ql, qr, idx = 1, l = 1, r = None):
        if r is None: r = self.n
        if ql <= l and r <= qr:
            return self.tree[idx]
        mid = (l + r) >> 1
        ansl, ansr = inf, inf
        if ql <= mid:ansl = self.query(ql, qr, idx * 2, l, mid)
        if qr > mid: ansr = self.query(ql, qr, idx * 2 + 1, mid + 1, r)
        return self.op(ansl, ansr)

class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        treey = [SegmentTree(m) for _ in range(n)]
        # treey[j] 是第j 列的线段树
        for i in range(m - 1, -1, -1):
            treex = SegmentTree(n)
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    treex.update(j + 1, j + 1, 1)
                    treey[j].update(i + 1, i + 1, 1)
                    continue
                g = grid[i][j]
                if g == 0: continue
                mnx = treex.query(j + 1 + 1, min(g + j, n - 1) + 1)  if j < n - 1 else inf 
                mny = treey[j].query(i + 1 + 1, min(g + i, m - 1) + 1) if i < m - 1 else inf
                mn =  min(mnx, mny) + 1
                treex.update(j + 1, j + 1, mn)
                treey[j].update(i + 1, i + 1, mn)
        res = treey[0].query(1, 1)
        return res if res != inf else -1
```

最值查询朴素无更新线段树：

```python
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        class SegmentTree:
            def __init__(self, n, flag):
                self.n = n
                self.tree = [inf * flag] * (4 * n)
                self.flag = flag
            def op(self, a, b):
                if self.flag == 1: return min(a, b)
                elif self.flag == -1: return max(a, b)
            def build(self, idx = 1, l = 1, r = None):
                if not r: r = self.n
                if l == r:
                    self.tree[idx] = nums[l - 1]
                    return
                mid = (l + r) >> 1
                self.build(idx * 2, l, mid)
                self.build(idx * 2 + 1, mid + 1, r)
                self.tree[idx] = self.op(self.tree[idx * 2], self.tree[idx * 2 + 1])
            def query(self, ql, qr, idx = 1, l = 1, r = None):
                if not r: r = self.n 
                if ql <= l and r <= qr: 
                    return self.tree[idx]
                ansl, ansr = inf * self.flag, inf * self.flag 
                mid = (l + r) >> 1
                if ql <= mid: ansl = self.query(ql, qr, idx * 2, l, mid)
                if qr > mid: ansr = self.query(ql, qr, idx * 2 + 1, mid + 1, r)
                return self.op(ansl, ansr)
        n = len(nums)
        mxtr, mntr = SegmentTree(n, -1), SegmentTree(n, 1)
        res = 0
        mxtr.build()
        mntr.build()
        for i in range(n):
            for j in range(i + 1, n):
                res += mxtr.query(i + 1, j + 1) - mntr.query(i + 1, j + 1)
        return res

```

[LCP 32. 批量处理任务 - 力扣（LeetCode）](https://leetcode.cn/problems/t3fKg1/)

排序 + 贪心 + lazy 线段树二分优化

```python
class SegmentTree:
    __slots__ = ['node', 'lazy', 'n', 'nums', 'op', 'ini', 'ops']

    def __init__(self, nums, ops = 'sum'):
        n = len(nums)
        if ops == 'sum' or ops == 'bin':
            op, ini = lambda a, b: a + b, 0
        elif ops == 'max':
            op, ini = lambda a, b: max(a, b), -inf
        elif ops == 'min':  
            op, ini = lambda a, b: min(a, b), inf
        self.nums = nums
        self.op = op
        self.ini = ini
        self.ops = ops 
        self.node = [ini] * (4 * n)
        self.lazy = [None] * (4 * n)
        self.n = n

    def build(self, idx = 1, l = 1, r = None):
        if r is None: r = self.n
        if l == r:
            self.node[idx] = self.nums[l - 1]
            return
        mid = (l + r) >> 1
        self.build(idx << 1, l, mid)
        self.build((idx << 1) + 1, mid + 1, r)

        self.node[idx] = self.op(self.node[idx << 1], self.node[(idx << 1) + 1])

    def do(self, idx, dl, dr, val = None):
        if self.ops == 'bin':
            self.node[idx] = dr - dl + 1 
            self.lazy[idx] = True
        else:
            self.node[idx] = self.op(val, self.node[idx])
            self.lazy[idx] = val

    def pushdown(self, idx, pl, pr):
        val = self.lazy[idx]
        mid = (pl + pr) >> 1
        self.do(idx << 1, pl, mid, val)
        self.do((idx << 1) + 1, mid + 1, pr, val)
        self.lazy[idx] = None

    def update(self, ul, ur, val, idx = 1, l = 1, r = None):
        if r is None:r = self.n
        if ul <= l and r <= ur:
            self.do(idx, l, r, val)
            return
        if self.lazy[idx]:
            self.pushdown(idx, l, r)
        mid = (l + r) >> 1
        if ul <= mid: self.update(ul, ur, val, idx << 1, l, mid)
        if ur > mid: self.update(ul, ur, val, (idx << 1) + 1, mid + 1, r)

        self.node[idx] = self.op(self.node[idx << 1], self.node[(idx << 1) + 1])

    def query(self, ql, qr, idx = 1, l = 1, r = None):
        if r is None: r = self.n
        if ql <= l and r <= qr:
            return self.node[idx]

        if self.lazy[idx]:
            self.pushdown(idx, l, r)

        mid = (l + r) >> 1
        ansl, ansr = self.ini, self.ini
        if ql <= mid: ansl = self.query(ql, qr, idx << 1, l, mid)
        if qr > mid:ansr = self.query(ql, qr, (idx << 1) + 1, mid + 1, r)
        return self.op(ansl, ansr)

    def update_suffix(self, ul, ur, val, idx = 1, l = 1, r = None):
        if r is None: r = self.n 
        siz = r - l + 1
        if ul <= l and r <= ur and siz - self.node[idx] <= val:
            ans = siz - self.node[idx]
            self.do(idx, l, r)
            return ans
        mid = (l + r) >> 1
        if self.lazy[idx]:
            self.pushdown(idx, l, r)
        ans = 0
        if ur > mid: ans += self.update_suffix(ul, ur, val, (idx << 1) + 1, mid + 1, r)
        val -= ans
        if val and ul <= mid: ans += self.update_suffix(ul, ur, val, idx << 1,  l, mid)
        self.node[idx] = self.op(self.node[idx << 1], self.node[(idx << 1) + 1])
        return ans 

class Solution:
    def findMinimumTime(self, nums: List[List[int]]) -> int:
        nums.sort(key = lambda x: x[1])
        n, m = len(nums), nums[-1][1]
        tr = SegmentTree([0] * m, 'bin')
        for l, r, c in nums:
            c -= tr.query(l, r)
            if c > 0:
                tr.update_suffix(l, r, c)
        return tr.query(0, m)
```



## 树状数组

下标从1开始，单点修改 + 区间查询

```python
# 下标从1开始
class FenwickTree:
    def __init__(self, length: int):
        self.length = length
        self.tree = [0] * (length + 1)
    def lowbit(self, x: int) -> int:
        return x & (-x)

    # 更新自底向上
    def update(self, idx: int, val: int) -> None:
        while idx <= self.length:
            self.tree[idx] += val
            idx += self.lowbit(idx)

    # 查询自顶向下
    def query(self, idx: int) -> int:
        res = 0
        while idx > 0:    
            res += self.tree[idx]
            idx -= self.lowbit(idx)
        return res

class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.nums = nums
        self.tree = FenwickTree(n)
        for i, x in enumerate(nums):
            self.tree.update(i + 1, x)


    def update(self, index: int, val: int) -> None:
        # 因为这里是更新为val, 所以节点增加的值应为val - self.nums[index]
        # 同时需要更新nums[idx]
        self.tree.update(index + 1, val - self.nums[index])
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        r = self.tree.query(right + 1)
        l = self.tree.query(left)
        return r - l


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
```

### 离散化树状数组 + 还原



```python
class FenwickTree:
    def __init__(self, length: int):
        self.length = length
        self.tree = [0] * (length + 1)

    def lowbit(self, x: int) -> int:
        return x & (-x)

    # 更新自底向上
    def update(self, idx: int, val: int) -> None:
        while idx <= self.length:
            self.tree[idx] += val
            idx += self.lowbit(idx)

    # 查询自顶向下
    def query(self, idx: int) -> int:
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= self.lowbit(idx)
        return res

class Solution:

    def resultArray(self, nums: List[int]) -> List[int]:
        # 离散化 nums
        sorted_nums = sorted(nums)
        tmp = nums.copy()
        nums = [bisect.bisect_left(sorted_nums, x) + 1 for x in nums]
        # 还原
        mp_rev = {i: x for i, x in zip(nums, tmp)}
        n = len(nums)
        t1 = FenwickTree(n)
        t2 = FenwickTree(n)
        a = [nums[0]]
        b = [nums[1]]
        t1.update(nums[0], 1)
        t2.update(nums[1], 1)
        for i in range(2, len(nums)):
            x = nums[i]
            c = len(a) - t1.query(x)
            d = len(b) - t2.query(x)
            if c > d or c == d and len(a) <= len(b):
                a.append(x)
                t1.update(x, 1)
            else:
                b.append(x)
                t2.update(x, 1)
        # 还原为原始数据: i 为离散化秩，x 为还原值
        return [mp_rev[i] for i in a] + [mp_rev[i] for i in b]
```



**可离散化线段树**

```python
class FenwickTree:
    def __lowbit(self, x: int) -> int:
        """
        返回x 的二进制中，最低为的1所构成的数。
        :param x: 整数
        :return: x的二进制中，最低为的1所构成的数
        """
        return x & -x
    def __init__(self, n: int, discretize: bool = False, nums: [List[int]] = None):
        """
        初始化树状数组（Fenwick Tree）数据结构，下标从0开始
        :param n: 值域范围
        :param discretize: 是否对输入值进行离散化
        :param nums: 离散化所需的输入数组
        """
        self.__dic = None
        self.__discretize = discretize
        self.__nums = None
        self.__n = n

        if discretize:
            unique_nums = sorted(set(nums))
            self.__dic = {unique_nums[i]: i + 1 for i in range(len(unique_nums))}
            self.__n = len(unique_nums)

        self.__nums = [0] * (self.__n + 1)

    def __query(self, x: int) -> int:
        """
        查询小于等于x的个数
        :param x: 查询的数
        :return: 查询小于等于x的个数
        """
        res = 0
        while x > 0:
            res += self.__nums[x]
            x -= self.__lowbit(x)
        return res

    def update(self, x: int, val: int) -> None:
        """
        x处对应的值增加val
        :param x: 更新的数
        :param val: 变化值
        """
        if self.__discretize:
            if x not in self.__dic:
                raise ValueError(f"值{x} 不在离散化范围内")
            x = self.__dic[x]

        while x <= self.__n:
            self.__nums[x] += val
            x += self.__lowbit(x)

    def query(self, lx: int, rx: int = None) -> int:
        """
        如果只传入一个参数，则查询小于等于lx的个数
        如果传入两个参数，则查询大于等于lx, 小于等于rx的个数
        :param lx: 查询区间左端点
        :param rx: 查询区间右端点
        :return: 查询区间内的元素个数
        """
        if self.__discretize:
            if lx not in self.__dic:
                raise ValueError(f"值{lx} 不在离散化范围内")
            lx = self.__dic[lx]
            if rx is not None:
                if rx not in self.__dic:
                    raise ValueError(f"值{rx} 不在离散化范围内")
                rx = self.__dic[rx]

        if rx is not None:
            if lx > rx:
                raise ValueError(f"左边界{lx} 大于右边界{rx}")
            return self.__query(rx) - self.__query(lx - 1)
        return self.__query(lx)

```



## ST表 / 可重复贡献问题

> 可重复贡献问题：指对于运算 $opt$， 满足 $ x \space opt  \space x = x$。例如区间最值问题，区间GCD问题。

ST表思想基于倍增，不支持修改操作。

预处理：$O(nlogn)$
$$
f(i, j) 表示[i, i + 2^j - 1]区间的最值，则将其分为两半，left = [i, i + 2^{j-1} -1],right = [i+2^{j-1},i+2^j-1]。\
$$

$$
则f(i, j) = opt(f(i, j - 1), f(i + 2^{j - 1}, j - 1))
$$

$$
初始化时，f(i, 0) = a[i]; \\ 
$$

$$
对于j的上界需要满足 i + 2 ^ j - 1 能够取到 n - 1，即2 ^ j 能够取到n。 \\
所以 外层循环条件 j \in [1, ceil(log_2^j) + 1)。\\
$$

$$
对于i的上界需要满足 i + 2 ^ j - 1 < n，即 i \in[0, n - 2^k + 1)。
$$

$例如，对于 f(4, 3) = opt(f(4, 2), f(8, 2))$

```python
lenj = math.ceil(math.__log(n, 2)) + 1
f = [[0] * lenj for _ in range(n)]
for i in range(n):
    f[i][0] = a[i]
for j in range(1, lenj):
    # i + 2 ^ j < n + 1
    for i in range(n + 1 - (1 << j)):
        f[i][j] = opt(f[i][j - 1], f[i + (1 << (j - 1))][j - 1])
```



单次询问：$O(1)$

$例如， 对于qry(5, 10)，区间长度为6，int(log_2^6) = 2，只需要k = 2^2的两个区间一定可以覆盖整个区间。$

$即opt(5, 10) = opt(opt(5, 8), opt(7, 10))$，即分别是$(l, l + 2^k-1)和(r - 2^k+1,r)$
$$
qry(l, r) = opt(qry(l, k), qry(r - 2 ^k + 1,k))
$$

```python
def qry(l, r):
    k = log[r - l + 1]
    return opt(f[l][k], f[r - (1 << k) + 1][k])
```



可以提取预处理一个对数数组。$例如int(log(7)) = int(log(3)) + 1 = int(log(1)) + 1 + 1$

```python
log = [0] * (n + 1)
for i in range(2, n + 1):
    log[i] = log[i >> 1] + 1
```

模板

```python
def opt(a, b):
    return max(a, b)


lenj = math.ceil(math.__log(n, 2)) + 1
f = [[0] * lenj for _ in range(n)]
log = [0] * (n + 1)
for i in range(2, n + 1):
    log[i] = log[i >> 1] + 1
for i in range(n): f[i][0] = a[i]
for j in range(1, lenj):
    for i in range(n + 1 - (1 << j)):
        f[i][j] = opt(f[i][j - 1], f[i + (1 << (j - 1))][j - 1])


def qry(l, r):
    k = log[r - l + 1]
    return opt(f[l][k], f[r - (1 << k) + 1][k])
```

类模板

```python
class ST:
    def opt(self, a, b):
        return a & b

    def __init__(self, nums):
        n = len(nums)
        log = [0] * (n + 1)
        for i in range(2, n + 1):
            log[i] = log[i >> 1] + 1
        lenj = ceil(math.__log(n, 2)) + 1
        f = [[0] * lenj for _ in range(n)]
        for i in range(n): f[i][0] = nums[i]
        for j in range(1, lenj):
            for i in range(n + 1 - (1 << j)):
                f[i][j] = self.opt(f[i][j - 1], f[i + (1 << (j - 1))][j - 1])
        self.f = f
        self.log = log

    def qry(self, L, R):
        k = self.log[R - L + 1]
        return self.opt(self.f[L][k], self.f[R - (1 << k) + 1][k])
```



[2104. 子数组范围和 - 力扣（LeetCode）](https://leetcode.cn/problems/sum-of-subarray-ranges/?envType=featured-list&envId=ZZi8gf6w?envType=featured-list&envId=ZZi8gf6w)

```python
    def subArrayRanges(self, nums: List[int]) -> int:
    # f[i][j] 表示 [i, i + 2^j - 1] 的最值
    n = len(nums)
    lenj = ceil(math.__log(n, 2)) + 1
    log = [0] * (n + 1)
    for i in range(2, n + 1):
        log[i] = log[i // 2] + 1

    class ST:
        def __init__(self, n, flag):
            self.flag = flag
            f = [[inf * flag] * lenj for _ in range(n)]
            for i in range(n):
                f[i][0] = nums[i]
            for j in range(1, lenj):
                for i in range(n + 1 - (1 << j)):
                    f[i][j] = self.op(f[i][j - 1], f[i + (1 << (j - 1))][j - 1])
            self.f = f

        def op(self, a, b):
            if self.flag == 1: return min(a, b)
            return max(a, b)

        def query(self, l, r):
            k = log[(r - l + 1)]
            return self.op(self.f[l][k], self.f[r - (1 << k) + 1][k])

    n = len(nums)
    mxtr, mntr = ST(n, -1), ST(n, 1)
    res = 0
    for i in range(n):
        for j in range(i + 1, n):
            res += mxtr.query(i, j) - mntr.query(i, j)
    return res
```



# 图论

## 建图

邻接矩阵

```python
g = [[inf] * n for _ in range(n)]
for u, v, w in roads:
    g[u][v] = g[v][u] = w
    g[u][u] = g[v][v] = 0
```

邻接表

```python
e = [[] for _ in range(n)]
for u, v, w in roads:
    e[u].append((v, w))
    e[v].append((u, w))
```

去重边建图

[100244. 带权图里旅途的最小代价 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-cost-walk-in-weighted-graph/description/)

这道题需要在建图的时候取AND运算的最小值。

```python
        e = [defaultdict(lambda: -1) for _ in range(n)]
        for u, v, w in edges:
            e[v][u] = e[u][v] = e[u][v] & w
```

## Floyd

```python
    mp = [[inf] * n for _ in range(n)]
    for u, v, w in edges:
        mp[u][v] = mp[v][u] = w
        mp[u][u] = mp[v][v] = 0
    for k in range(n):
        for u in range(n):
            for v in range(n):
                mp[u][v] = min(mp[u][v], mp[u][k] + mp[k][v])
```

## Dijkstra

### 1. 朴素Dijkstra

适用于稠密图，时间复杂度：$O(n^2)$

```python
        g = [[inf] * n for _ in range(n)]
        for u, v, w in roads:
            g[u][v] = g[v][u] = w
            g[u][u] = g[v][v] = 0
        d = [inf] * n       # dist数组, d[i] 表示源点到i 的最短路径长度
        d[0] = 0
        v = [False] * n     # 节点访问标记
        for _ in range(n - 1): 
            x = -1
            for u in range(n):
                if not v[u] and (x < 0 or d[u] < d[x]):
                    x = u
            v[x] = True
            for u in range(n):
                d[u] = min(d[u], d[x] + g[u][x])
```

[1976. 到达目的地的方案数 - 力扣（LeetCode）](https://leetcode.cn/problems/number-of-ways-to-arrive-at-destination/description/?envType=daily-question&envId=2024-03-05)

最短路Dijkstra + 最短路Dp：求源点0到任意节点i 的最短路个数。



```python
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        g = [[inf] * n for _ in range(n)]
        moder = 10 ** 9 + 7
        for u, v, w in roads:
            g[u][v] = g[v][u] = w
            g[u][u] = g[v][v] = 0
        d = [inf] * n       # dist数组, d[i] 表示源点到i 的最短路径长度
        d[0] = 0
        v = [False] * n     # 节点访问标记
        mn, res = inf, 0
        f = [0] * n # f[i] 表示源点到i节点的最短路个数
        f[0] = 1
        for _ in range(n - 1): 
            x = -1
            for u in range(n):
                if not v[u] and (x < 0 or d[u] < d[x]):
                    x = u
            v[x] = True
            for u in range(n):
                a = d[x] + g[x][u]
                if a < d[u]:    # 到u的最短路个数 = 经过x到u的个数 = 到x的最短路的个数
                    d[u], f[u] = a, f[x]
                elif a == d[u] and u != x: # 路径一样短，追加
                    f[u] = (f[u] + f[x]) % moder
        return f[n - 1] 
     
```

[743. 网络延迟时间 - 力扣（LeetCode）](https://leetcode.cn/problems/network-delay-time/)

有向图 + 邻接矩阵最短路

```python
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g = [[inf] * (n + 1) for _ in range(n + 1)]
        for u, v, w in times:
            g[u][v] = w
            g[u][u] = g[v][v] = 0
        d = [inf] * (n + 1)
        d[k] = 0
        v = [False] * (n + 1)
        for _ in range(n - 1):
            x = -1
            for u in range(1, n + 1):
                if not v[u] and (x < 0 or d[u] < d[x]):
                    x = u
            v[x] = True
            for u in range(1, n + 1):
                d[u] = min(d[u], d[x] + g[x][u])
        res = max(d[1: ])
        return res if res != inf else -1
```

[2662. 前往目标的最小代价 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-cost-of-a-path-with-special-roads/solutions/?envType=featured-list&envId=QAPjw82k?envType=featured-list&envId=QAPjw82k)

将 有向图路径 转换为 节点。不需要建图，但是需要首先对 d 数组进行预处理。

```python
def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        # 把路径(a, b) -> (c, d) 简化成 (c, d)
        t, s = tuple(target), tuple(start)
        d, v = defaultdict(lambda: inf), set()
        d[s] = 0
        def g(p, q):
            return abs(p[0] - q[0]) + abs(p[1] - q[1])
        # 补充start 和 target 节点
        specialRoads.append([s[0], s[1], t[0], t[1], g(s, t)])
        specialRoads.append([s[0], s[1], s[0], s[1], 0])
        while True:
            x = None
            # 找到距离 start最近的 且 未计算过的节点
            for x1, y1, x2, y2, w in specialRoads:
                u = (x2, y2)
                if u not in v and (not x or d[u] < d[x]):
                    x = u 
            v.add(x)
            if x == t:
                return d[t]
            for x1, y1, x2, y2, w in specialRoads:
                u0, u = (x1, y1), (x2, y2)
                # 两种情况，1. start 经过 x 到达 u 
                # 2. start 经过 x 再到 u0 从路径到达 u
                d1 = d[x] + g(x, u)
                d2 = d[x] + g(x, u0) + w
                d[u] = min(d[u], d1, d2)

```



### 2.堆优化Dijkstra

适用于稀疏图（$点个数的平方 远大于 边的个数$），复杂度为$O(mlogm)$，$m表示边的个数$。

使用小根堆，存放未确定最短路点集对应的 (d[i], i)。对于同一个i 可能存放多组不同d[i] 的元组，因此堆中元素的个数最多是$m$ 个。

寻找最小值的过程可以用一个最小堆来快速完成。

```python
        e = [[] for _ in range(n)]
        for u, v, w in roads:
            e[u].append((v, w))
            e[v].append((u, w))

        d = [inf] * n
        d[0] = 0
        hq = [(0, 0)]   # 小根堆，存放未确定最短路点集对应的 (d[i], i)
        while hq:
            dx, x = heapq.heappop(hq)	
            if dx > d[x]: continue  # 跳过重复出堆，首次出堆一定是最短路
            for u, w in e[x]:
                a = d[x] + w
                if a < d[u]:
                    d[u] = a	# 同一个节点u 的最短路 d[u] 在出堆前会被反复更新
                    heapq.heappush(hq, (a, u))
```



[1976. 到达目的地的方案数 - 力扣（LeetCode）](https://leetcode.cn/problems/number-of-ways-to-arrive-at-destination/description/?envType=daily-question&envId=2024-03-05)

```python
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        e = [[] for _ in range(n)]
        for u, v, w in roads:
            e[u].append((v, w))
            e[v].append((u, w))

        moder = 10 ** 9 + 7
        f = [0] * n
        d = [inf] * n
        f[0], d[0] = 1, 0
        hq = [(0, 0)]   # 小根堆，存放未确定最短路点集对应的 (d[i], i)
        while hq:
            dx, x = heapq.heappop(hq)
            if dx > d[x]: continue  # 之前出堆过
            for u, w in e[x]:
                a = d[x] + w
                if a < d[u]:
                    d[u] = a
                    f[u] = f[x] 
                    heapq.heappush(hq, (a, u))
                elif a == d[u]:
                    f[u] = (f[u] + f[x]) % moder 
        return f[n - 1] 
```

[743. 网络延迟时间 - 力扣（LeetCode）](https://leetcode.cn/problems/network-delay-time/)

有向图 + 邻接矩阵最短路

```python
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        e = [[] * (n + 1) for _ in range(n + 1)]
        for u, v, w in times:
            e[u].append((v, w))
        d = [inf] * (n + 1)
        d[k] = 0
        hq = [(0, k)]
        while hq:
            dx, x = heapq.heappop(hq)
            if dx > d[x]: continue
            for u, w in e[x]:
                a = d[x] + w
                if a < d[u]:
                    d[u] = a 
                    heapq.heappush(hq, (a, u))	
        res = max(d[1: ])
        return res if res < inf else -1
```

[2045. 到达目的地的第二短时间 - 力扣（LeetCode）](https://leetcode.cn/problems/second-minimum-time-to-reach-destination/description/?envType=featured-list&envId=QAPjw82k?envType=featured-list&envId=QAPjw82k)

使用双列表d，存放最短和次短。将等红绿灯转换为松弛条件，通过t 来判断红灯还是绿灯。

```python
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # 将 节点 (u, t) 即 (节点，时间) 作为新的节点
        e = [[] for _ in range(n + 1)]
        for u, v in edges:
            e[u].append(v)
            e[v].append(u)
        hq = [(0, 1)]
        # (t // change) & 1 == 0 绿色
        # (x, t) -> (u, t + time)

        # (t // change) & 1 == 1 红色
        # 需要 change - t % change 时间进入下一个节点
        d, dd = [inf] * (n + 1), [inf] * (n + 1)
        d[1] = 0
        while hq:
            t, x = heapq.heappop(hq)
            if d[x] < t and dd[x] < t:    # 确认最小的和次小的
                continue
            for u in e[x]:
                nt = inf
                if (t // change) & 1 == 0:
                    nt = t + time
                else:
                    nt = t + change - t % change + time
                if nt < d[u]:
                    d[u] = nt
                    heapq.heappush(hq, (nt, u))
                elif dd[u] > nt > d[u] :
                    dd[u] = nt
                    heapq.heappush(hq, (nt, u))
        return dd[n]

```

### 3. 堆优化Dijkstra（字典写法）

转换建图 + 堆Dijkstra (字典写法 )

[LCP 35. 电动车游城市 - 力扣（LeetCode）](https://leetcode.cn/problems/DFPeFJ/description/?envType=featured-list&envId=QAPjw82k?envType=featured-list&envId=QAPjw82k)

```python
    def electricCarPlan(self, paths: List[List[int]], cnt: int, start: int, end: int, charge: List[int]) -> int:
        # 将(节点, 电量) 即 (u, c) 看成新的节点
        # 将充电等效转换成图
        # 则将节点i充电消耗时间charge[u] 看成从(u, c) 到 (u, c + 1) 有 w = 1
        n = len(charge)
        e = [[] for _ in range(n)]
        for u, v, w in paths:
            e[u].append((v, w))
            e[v].append((u, w))
        hq = [(0, start, 0)]
        d = {}
        while hq:
            dx, x, c = heapq.heappop(hq)
            if (x, c) in d: # 已经加入到寻找到最短路的集合中
                continue
            d[(x, c)] = dx
            for u, w in e[x]:
                if c >= w and (u, c - w) not in d:
                    heapq.heappush(hq, (w + dx, u, c - w))
            if c < cnt:
                heapq.heappush(hq, (charge[x] + dx, x, c + 1))
        return d[(end, 0)]
```

[743. 网络延迟时间 - 力扣（LeetCode）](https://leetcode.cn/problems/network-delay-time/description/)

```python
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        e = [[] * (n + 1) for _ in range(n + 1)]
        for u, v, w in times:
            e[u].append((v, w))
        d = {}
        hq = [(0, k)]
        while hq:
            dx, x = heapq.heappop(hq)
            if x in d: continue # 跳过非首次出堆
            d[x] = dx           # 首次出堆一定是最短路
            for u, w in e[x]:
                a = d[x] + w
                if u not in d:  # 未确定最短路
                    heapq.heappush(hq, (a, u))  # 入堆，同一个节点可能用多组
        for i in range(1, n + 1):
            if i != k and i not in d:
                return -1
        return max(d.values())
```

[2045. 到达目的地的第二短时间 - 力扣（LeetCode）](https://leetcode.cn/problems/second-minimum-time-to-reach-destination/?envType=featured-list&envId=QAPjw82k?envType=featured-list&envId=QAPjw82k)

求解严格次短路问题：两个d字典，一个存放最短，一个存放严格次短

```python
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        # 将 节点 (u, t) 即 (节点，时间) 作为新的节点
        # (t // change) & 1 == 0 绿色
        # (x, t) -> (u, t + time)

        # (t // change) & 1 == 1 红色
        # 需要 change - t % change 时间进入下一个节点
        # (x, t) -> (u, t + change - t % change + time)
        
        e = [[] for _ in range(n + 1)]
        for u, v in edges:
            e[u].append(v)
            e[v].append(u)
        hq = [(0, 1)]
        d, dd = {}, {}  # dd 是确认次短的字典
        while hq:
            t, x = heapq.heappop(hq)
            if x not in d:
                d[x] = t
            elif t > d[x] and x not in dd: 
                dd[x] = t
            else:
                continue
            for u in e[x]:
                if (t // change) & 1 == 0:
                    if u not in dd:
                        heapq.heappush(hq, (t + time, u))
                else:
                    if u not in dd:
                        heapq.heappush(hq, (t + change - t % change + time, u))
        return dd[n]        
```

转换建图问题：可折返图 转换成 到达时间的奇偶问题

[2577. 在网格图中访问一个格子的最少时间 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-time-to-visit-a-cell-in-a-grid/?envType=featured-list&envId=QAPjw82k?envType=featured-list&envId=QAPjw82k)

```python
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        # (w, x0, x1) 表示到达(x0, x1) 时刻至少为w
        if grid[0][1] > 1 and grid[1][0] > 1: return -1
        m, n = len(grid), len(grid[0])
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        target = (m - 1, n - 1)
        d = {}
        hq = [(0, (0, 0))]
        while hq:
            dx, x = heappop(hq)
            if x in d: continue
            d[x] = dx
            if x == target: return d[target]
            x0, x1 = x[0], x[1]
            for u0, u1 in [(x0 + dx, x1 + dy) for dx, dy in deltas]:
                if not (0 <= u0 < m and 0 <= u1 < n) or (u0, u1) in d: continue
                u, t = (u0, u1), grid[u0][u1]
                if dx + 1 >= t:
                    heappush(hq, (dx + 1, u))
                else:
                    # 例如 3 -> 6，折返一次变成5 后 + 1到达 6
                    du = (t - dx - 1) if (t - dx) & 1 else t - dx
                    heappush(hq, (dx + du + 1, u))
```



### 4.最短路与子序列 和/积 问题

求解一个数组的所有子序列的和 / 积中第k小 (大同理) 问题，其中子序列是原数组删去一些元素后剩余元素不改变相对位置的数组。

以和为例，可以转化为最短路问题：

将子序列看成节点 $(s, idx)$， $s$ 表示序列的和，$idx$ 表示下一个位置，则$idx - 1$ 表示序列最后一个元素的位置。

例如$[1, 2, 4, 4, 5, 9]$ 的其中一个子序列$[1,2]$，对应节点$(3, 2)$。如果从$idx-1$位置选或不选来看，可以转换为子序列$[1, 2, 4]$ 和 $[1, 4]$，则定义节点之间的边权是序列和之差，由于有序数组，边权一定非负。

可以将原问题看成从$[\space ]$ 为 源节点的，带正权的图。只需要不断求解到源节点的最短路节点，就可以得到所有子序列从小到大的和的值。

假设有$n$个节点，堆中元素个数不会超过$k$，时间复杂度是$O(klogk)$。

注意，如果采用二分答案方式求解，即想求出恰好有$k$个元素小于等于对应子序列之和$s$ 的算法，时间复杂度为$O(klogU), U = \sum{a_i}$

[2386. 找出数组的第 K 大和 - 力扣（LeetCode）](https://leetcode.cn/problems/find-the-k-sum-of-an-array/)

```python
    def kSum(self, nums: List[int], k: int) -> int:
        res = sum(x for x in nums if x > 0)
        nums = sorted([abs(x) for x in nums])
        # (s, idx) (子序列和, 当前下标)
        hq = [(0, 0)]
        while k > 1:
            # 每一次会将最小的子序列的和pop出去
            # pop k - 1次，堆顶就是答案
            s, idx = heappop(hq)
            # 选 idx - 1
            if idx < len(nums):
                heappush(hq, (s + nums[idx], idx + 1))
            # 不选 idx - 1
                if idx:
                    heappush(hq, (s + (nums[idx] - nums[idx - 1]), idx + 1))
            k -= 1
        return res - hq[0][0]      
```

### 5. 动态修改边权

[2699. 修改图中的边权 - 力扣（LeetCode）](https://leetcode.cn/problems/modify-graph-edge-weights/description/)

	1. 在邻接表数组中记录原矩阵中边的位置，方便修改
	1. 记$d_{signal, i}$ 表示第$signal$ 次得到的节点$i$ 到源点的最短路。跑两次 dijkstra算法
	1. .第二次修改边权时，对于特殊边尝试修改条件：

$$
d_{1,x} + nw + d_{0,dest} - d_{0, u} = target \\
解得nw = target - d_{1,x} + d_{0, u} -  d_{0,dest} \\
$$

当这个值大于1时，是一个合法的边权，进行修改。

![image.png](https://pic.leetcode.cn/1710550705-aHllZi-image.png)

```python
def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        e = [[] for _ in range(n)]
        # 存放边的位置，方便在原矩阵直接修改
        for pos, (u, v, w) in enumerate(edges):
            e[u].append([v, pos])
            e[v].append([u, pos])

        total_d = [[inf] * n for _ in range(2)]
        total_d[0][source] = total_d[1][source] = 0
        def dijkstra(signal):
            d = total_d[signal] # 第signal次的最短路数组
            v = set()
            for _ in range(n - 1):
                x = -1
                for u in range(n):
                    if u not in v and (x < 0 or d[u] < d[x]):
                        x = u
                v.add(x)
                for u, pos in e[x]:
                    w = edges[pos][2] 
                    w = 1 if w == -1 else w
                    # d[x] + nw +  total_d[0][destination] - total_d[0][u] = target
                    if signal == 1 and edges[pos][2] == -1:
                        nw = target - total_d[0][destination] + total_d[0][u] - d[x]
                        if nw > 1:  # 合法修改
                            w = edges[pos][2] = nw 
                    d[u] = min(d[u], d[x] + w)
            return d[destination]
        if dijkstra(0) > target: return []  # 全为1也会超过target
        if dijkstra(1) < target: return []  # 最短路无法变大
        for e in edges: 
            if e[2] == -1:
                e[2] = 1
        return edges

```

## 最小生成树

### Prim

```python
def solve():
    n, m = map(int, input().split())
    low_cost = [inf] * n 
    g = [[] for _ in range(n)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        u, v = u - 1, v - 1
        g[u].append((v, w))
        g[v].append((u, w))
        
    low_cost[0] = 0
    res = 0
    s = set()
    for _ in range(n):
        dx, x = inf, -1
        for i in range(n):
            if i not in s and (x < 0 or low_cost[i] < dx):
                dx, x = low_cost[i], i
        s.add(x)
        res += dx

        for i, w in g[x]:
            if i not in s:
                low_cost[i] = min(low_cost[i], w)

    if inf not in low_cost:
        print(res)
        return
    print('orz')
```



## 二分图

简单来说，如果图中点可以被分为两组，并且使得所有边都跨越组的边界，则这就是一个二分图。

[二分图的最大匹配、完美匹配和匈牙利算法_完美匹配图论-CSDN博客](https://blog.csdn.net/KYJL888/article/details/106055942)

定义：无向图$G(U,V,E)$中节点可以划分成互斥集合$U$, $V$，使得 $\forall (u, v) \in E$ 的两个端点分属于两个集合。

- 两个互斥点集中的任意两点之间都不存在边

- 任何一条边的两个端点分别来互斥的两个点集$U, V$

- 不存在奇数点的环（不存在奇数条边的环）

  ​	证明：因为走过一条边必然从一个集合走到另一个集合，要完成闭环必须走偶数条边（偶数个点）

- 可能存在孤点

  ![image.png](https://pic.leetcode.cn/1710725424-kbrwZc-image.png)

### 二分图判定

[785. 判断二分图 - 力扣（LeetCode）](https://leetcode.cn/problems/is-graph-bipartite/description/?envType=featured-list&envId=JMxeEVyu?envType=featured-list&envId=JMxeEVyu)

DFS染色：

```python
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0] * n    
        flag = True
        def dfs(u, c):
            nonlocal flag
            color[u] = c 
            for v in graph[u]:
                if color[v] == 0:
                    dfs(v, -c)
                elif color[v] == c:
                    flag = False
                    return 
        for i in range(n):
            if color[i] == 0: dfs(i, 1)
            if not flag: return False
        return True
```

Bfs染色：

```python
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        q = collections.deque()
        color = [0] * n
        for i in range(n):
            if not color[i]:
                q.append(i)
                color[i] = 1
            while q:
                u = q.popleft()
                c = color[u]
                for v in graph[u]:
                    if not color[v]:
                        color[v] = -c 
                        q.append(v)
                    elif color[v] == c:
                        return False
        return True
```

并查集做法：

维护两个并查集$U, V$ , 分别存储两个互斥点集。

对于每个节点$u$ 遍历其所有邻接节点$v $ 。如果遇到 $u$ , $v$ 在同一个并查集，说明不满足二分图。（同一点集中出现连接的边）

否则将所有邻接节点加到另一个并查集中。

```python
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        s = set()
        pa = list(range(n))
        def find(x):
            if pa[x] != x:
                pa[x] = find(pa[x])
            return pa[x]
        def union(u, v):
            if find(u) != find(v):
                pa[find(v)] = find(u)
        for u in range(n):
            if u not in s:
                s.add(u)
                p = None
                for v in graph[u]:
                    if find(u) == find(v):
                        return False
                    if p: union(p, v)
                    p = v
        return True
```

### 二分图最大匹配 / 匈牙利算法

**二分图的匹配**

给定一个二分图G，在G的一个子图M中， M的边集 $\{E\}$ 中的**任意两条边都没有公共顶点**，则称M是一**个匹配**。

**最大匹配**：匹配边数最大的匹配。

**完美匹配**：如果一个图的某个匹配中，所有的顶点都是匹配点，那么它就是一个完美匹配。图 4 是一个完美匹配。

- 完美匹配一定是最大匹配（完美匹配的任何一个点都已经匹配，添加一条新的匹配边一定会冲突）

- 但并非每个图都存在完美匹配。
- 完美匹配的边数 = 左 / 右部的点数

![image.png](https://pic.leetcode.cn/1713707756-oIAptI-image.png)

**二分图最大权完美匹配**：二分图边权和最大的完美匹配。

**交替路**：从一个未匹配点出发(右)，依次经过非匹配边、匹配边、非匹配边…形成的路径叫交替路。

![image.png](https://pic.leetcode.cn/1713708190-cjjZiZ-image.png)

**增广路**：从一个未匹配点出发(右)，走交替路，如果途径另一个未匹配点（出发的点不算），则这条交替路称为增广路（agumenting path）。例如，图 5 中的一条增广路如图 6 所示（图中的匹配点均用红色标出）

- 特点：**非匹配边比匹配边多一条**。因此，研究增广路的意义是改进匹配。只要把增广路中的匹配边和非匹配边的身份交换即可。由于中间的匹配节点不存在其他相连的匹配边，所以这样做不会破坏匹配的性质。交换后，图中的匹配边数目比原来多了 1 条。

![image.png](https://pic.leetcode.cn/1713708208-zxKiTw-image.png)

**增广路定理**

通过不停地找增广路来增加匹配中的匹配边和匹配点。找不到增广路时，达到最大匹配

[861. 二分图的最大匹配 - AcWing题库](https://www.acwing.com/problem/content/863/)

```python
    n1, n2, m = map(int, input().split())

    vis = set()
    match = {}
    e = defaultdict(list)

    def dfs(u) -> bool:
        for v in e[u]:
            if v in vis: continue 
            vis.add(v)
            if v not in match or dfs(match[v]):
                match[v] = u
                return True
        return False
    for _ in range(m):
        u, v = map(int, input().split())
        e[u].append(v)

    for u in range(1, n1 + 1):
        vis = set()
        dfs(u)

    print(len(match))
```



### 二分图最大权完美匹配  / KM算法

[1947. 最大兼容性评分和 - 力扣（LeetCode）](https://leetcode.cn/problems/maximum-compatibility-score-sum/description/?envType=featured-list&envId=ptud3zoQ?envType=featured-list&envId=ptud3zoQ)

暴力枚举时间复杂度：$O(m!)$，实际上是二分图的最大权完美匹配问题。复杂度：$O(m^3)$

```python
class KM:
    def __init__(self, n):
        self.maxn = 300 + 10
        self.INF = float('inf')
        self.wx = [0] * (self.maxn)
        self.wy = [0] * (self.maxn)
        self.cx = [-1] * (self.maxn)
        self.cy = [-1] * (self.maxn)
        self.visx = [0] * (self.maxn)
        self.visy = [0] * (self.maxn)
        self.cntx = n
        self.cnty = n
        self.Map = [[0] * (self.maxn) for _ in range(self.maxn)]
        self.slack = [0] * (self.maxn)

    def dfs(self, u):
        self.visx[u] = 1
        for v in range(1, self.cnty + 1):
            if not self.visy[v] and self.Map[u][v] != self.INF:
                t = self.wx[u] + self.wy[v] - self.Map[u][v]
                if t == 0:
                    self.visy[v] = 1
                    if self.cy[v] == -1 or self.dfs(self.cy[v]):
                        self.cx[u] = v
                        self.cy[v] = u
                        return True
                elif t > 0:
                    self.slack[v] = min(self.slack[v], t)
        return False

    def KM(self):
        for i in range(1, self.cntx + 1):
            for j in range(1, self.cnty + 1):
                if self.Map[i][j] == self.INF:
                    continue
                self.wx[i] = max(self.wx[i], self.Map[i][j])
        for i in range(1, self.cntx + 1):
            self.slack = [self.INF] * (self.maxn)
            while True:
                self.visx = [0] * (self.maxn)
                self.visy = [0] * (self.maxn)
                if self.dfs(i):
                    break
                minz = self.INF
                for j in range(1, self.cnty + 1):
                    if not self.visy[j] and minz > self.slack[j]:
                        minz = self.slack[j]
                for j in range(1, self.cntx + 1):
                    if self.visx[j]:
                        self.wx[j] -= minz
                for j in range(1, self.cnty + 1):
                    if self.visy[j]:
                        self.wy[j] += minz
                    else:
                        self.slack[j] -= minz

        ans = 0
        for i in range(1, self.cntx + 1):
            if self.cx[i] != -1:
                ans += self.Map[i][self.cx[i]]
        return ans

    def add_edge(self, u, v, w):
        self.Map[u + 1][v + 1] = w
```



## 连通块问题

[2867. 统计树中的合法路径数目 - 力扣（LeetCode）](https://leetcode.cn/problems/count-valid-paths-in-a-tree/description/?envType=featured-list&envId=4eH5fI7k?envType=featured-list&envId=4eH5fI7k)

**DFS + 字典维护节点所在连通块大小**

 `cc_siz` 用来记录连通块的大小。`vis`数组对质数节点进行记录，dfs的起始节点一定是质数节点的非质数子节点。

使用 `cc_node` 记录一次连通分量dfs得到的节点列表，更新对应 `cc_siz` 的值。这样后续在遍历到已经遍历过的非质数连通块时，可以直接得到结果。

```python
def countPaths(self, n: int, edges: List[List[int]]) -> int:
        primes = []
        N = n + 10
        is_prime = [True] * N
        is_prime[0] = is_prime[1] = False
        for i in range(2, N):
            if is_prime[i]:
                primes.append(i)
            for p in primes:
                if i * p >= N:
                    break
                is_prime[i * p] = False
                if i % p == 0:
                    break
        e = [[] for _ in range(n + 1)]
        for u, v in edges:
            e[u].append(v)
            e[v].append(u)
        vis = [False] * (n + 1)
        cc_siz = {}
        cc_node = []
        def dfs(u, fa):
            siz = 1
            cc_node.append(u)
            for v in e[u]:
                if v != fa and not is_prime[v]:
                    siz += dfs(v, u)
            return siz
        res = 0
        for u in range(1, n + 1):
            if not vis[u] and is_prime[u]:
                vis[u] = True
                cur_siz = 0
                for v in e[u]:
                    if is_prime[v]:
                        continue
                    # 对于每一个子连通分量
                    if v in cc_siz:
                        siz = cc_siz[v]
                    else:
                        cc_node.clear()
                        siz = dfs(v, u)
                        for node in cc_node:
                            cc_siz[node] = siz
                    res += siz + siz * cur_siz
                    cur_siz += siz
        return res

```

**DFS + 字典维护连通块的 AND 值 和 节点对应的连通块下标**

[100244. 带权图里旅途的最小代价 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-cost-walk-in-weighted-graph/description/)

通过字典中连通块下标，判断两个节点是否在同一连通块内。

```python
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        cc_and = {}     # 键为节点，值为 (cc_cnt, and_ans)，即对应的连通块编号 和 连通块的and值
        cc_cnt = 0      # 计数，记录当前统计到第几个连通块
        cc_node = []
        e = [{} for _ in range(n)]
        for u, v, w in edges:
            if v not in e[u]:
                e[v][u] = e[u][v] = w 
            else:
                 e[v][u] = e[u][v] = e[u][v] & w
        vis = [False] * n 
        
        def dfs(u):
            vis[u] = True 
            cc_node.append(u)
            and_ans = -1
            for v in e[u]:
                w = e[u][v]
                and_ans &= w
                if not vis[v]:
                    and_ans &= dfs(v)
            return and_ans
        for u in range(n):
            if not vis[u]:
                and_ans = dfs(u)
                for node in cc_node:
                    cc_and[node] = (cc_cnt, and_ans)
                cc_node.clear()
                cc_cnt += 1
        return [0 if u == v else (cc_and[u][1] if cc_and[u][0] == cc_and[v][0] else -1) 
                for u, v in query]
```

**并查集维护连通块属性**

[928. 尽量减少恶意软件的传播 II - 力扣（LeetCode）](https://leetcode.cn/problems/minimize-malware-spread-ii/description/?envType=daily-question&envId=2024-04-17)

题目问从 $bad$ 选一个节点，删除其和其邻接的边，能得到感染后的最小数量。暴力做法枚举删除的 $bad$ 点，需要 $O(n^3)$ 。

逆向思维：枚举所有的 $good$ 连通块，维护块大小 $siz$ ，及其邻接的 $bad$ 节点集合 $cc\_bad$。恰好只有一个邻接 $bad$ 的连通块，由于删除 $bad$ 后整个连通块不会被感染，所以其对该 $bad$ 节点的贡献为连通块大小。最后，返回所有 $bad$ 节点得到的贡献和（来自恰好仅邻接该节点的 $good$ 连通块）最大、序最小的节点。

```python
def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:
        n = len(graph[0])
        fa = list(range(n))
        siz = [1] * n
        cc_bad = defaultdict(set)
        def find(x):
            if fa[x] != x: fa[x] = find(fa[x])
            return fa[x]
        def union(u, v):
            if find(u) != find(v): 
                siz[find(u)] += siz[find(v)]
                cc_bad[find(u)] |= cc_bad[find(v)]
                fa[find(v)] = find(u)
        bad = set(initial)
        good = set(range(n)) - bad
        for u in good:
            for v, con in enumerate(graph[u]):
                if not con: continue 
                if v in bad: cc_bad[find(u)].add(v)
                else: union(u, v)
        pa = set(find(u) for u in good)
        bad_siz = Counter()
        for p in pa:
            if len(cc_bad[p]) == 1:
                bad_siz[list(cc_bad[p])[0]] += siz[p]
        mx, res = 0, min(bad)
        for u, sz in bad_siz.items():
            if sz > mx: mx, res = sz, u 
            if sz == mx: res = min(res, u)
        return res
```



## 最小费用最大流



# 树上问题

## 倍增LCA

$f[u][i] 表示 u 节点 向上跳2^i\space 的节点$，$dep[u] \space 表示深度$

```python
    MX = int(n.bit_length())
    f = [[0] * (MX + 1) for _ in range(n)]
    dep = [0] * n

    def dfs(u, fa):
        # father[u] = fa
        dep[u] = dep[fa] + 1    # 递归节点深度
        f[u][0] = fa
        for i in range(1, MX + 1):  # 倍增计算向上跳的位置
            f[u][i] = f[f[u][i - 1]][i - 1]
        for v in g[u]:
            if v != fa:
                dfs(v, u)

    # 假定0节点是树根
    dep[0] = 1
    for v in g[0]:
        dfs(v, 0)

    def lca(u, v):
        if dep[u] < dep[v]:
            u, v = v, u
        # u 跳到和v 同一层
        for i in range(MX, -1, -1):
            if dep[f[u][i]] >= dep[v]:
                u = f[u][i]
        if u == v:
            return u
        # 跳到lca的下一层
        for i in range(MX, -1, -1):
            if f[u][i] != f[v][i]:
                u, v = f[u][i], f[v][i]
        return f[u][0]
```



[P3379 【模板】最近公共祖先（LCA） - 洛谷 | 计算机科学教育新生态 (luogu.com.cn)](https://www.luogu.com.cn/problem/P3379)

```python
from math import log
import sys
input = lambda: sys.stdin.readline().strip()
n, m, s = map(int, input().split())

# f[n][mx]
mx = int(log(n, 2))
f = [[0] * (mx + 1) for _ in range(n + 10)]
e = [[] for _ in range(n + 10)]
dep = [0] * (n + 10)
dep[s] = 1


for _ in range(n - 1):
    u, v = map(int, input().split())
    e[u].append(v)
    e[v].append(u)
    


def dfs(u, fa):
    dep[u] = dep[fa] + 1
    f[u][0] = fa
    for i in range(1, mx + 1):
        f[u][i] = f[f[u][i - 1]][i - 1]
    for v in e[u]:
        if v != fa:
            dfs(v, u)
for v in e[s]:
    dfs(v, s)

def lca(u, v):
    # 让u 往上跳
    if dep[u] < dep[v]: u, v = v, u
    for i in range(mx, -1, -1):
        if dep[f[u][i]] >= dep[v]:
            u = f[u][i]
    if u == v: return u
    # 一定是在lca的下一层
    # 一起跳
    for i in range(mx, -1, -1):
        if f[u][i] != f[v][i]:
            u, v = f[u][i], f[v][i]
    return f[u][0]
for _ in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))

```



## 树上差分

点差分：解决多路径节点计数问题。

$u \rightarrow v 的路径转化为 u \rightarrow lca左孩子 + lca \rightarrow v$ 

```python
# 差分时左闭右开，无需考虑啊u = a的情况
for u, v in query:
    a = lca(u, v)
    diff[u] += 1
    diff[a] -= 1
    diff[v] += 1
    if father[a] != -1:
        diff[father[a]] -= 1
```

![image.png](https://pic.leetcode.cn/1701864888-CJnrkG-image.png)

## 树形DP(换根DP)

[834. 树中距离之和 - 力扣（LeetCode）](https://leetcode.cn/problems/sum-of-distances-in-tree/description/)

[题目详情 - Problem 4E. 最大社交深度和 - HydroOJ](https://hydro.ac/d/nnu_contest/p/17)

1，指定某个节点为根节点。

2，第一次搜索完成预处理（如子树大小等），同时得到该节点的解。

3，第二次搜索进行换根的动态规划，由已知解的节点推出相连节点的解。

```python
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        dep = [0] * n
        siz = [1] * n
        res = [0] * n
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def dfs1(u, fa):	# 预处理深度
            dep[u] = dep[fa] + 1 if fa != -1 else 0
            for v in g[u]:
                if v != fa:
                    dfs1(v, u)
                    siz[u] += siz[v]
        def dfs2(u, fa):	
            for v in g[u]:
                if v != fa:
                    res[v] = res[u] - siz[v] + (n - siz[v])
                    dfs2(v, u)
        dfs1(0, -1)
        res[0] = sum(dep)
        dfs2(0, -1)
        return res

```

$u$剔除v子树部分下降1，深度和增加 $n - siz[v]$

$v$子树部分上升1，深度和减少$siz[v]$

则状态转移方程$res[v] = res[u] - siz[v] + (n - siz[v])$

![image.png](https://pic.leetcode.cn/1709177362-feHrFp-image.png)

## 树上异或

性质1：对树上一条路径 $u \rightarrow x_0 \rightarrow x_1 \rightarrow \cdots \rightarrow v$ 进行相邻节点两两异或运算，等价于只对路径起始节点和终止节点异或。

因而树上相邻异或 等价于 树上任意两点进行异或

性质2：在树上任意相邻异或，总是有**偶数**个节点被异或。

[3068. 最大节点价值之和 - 力扣（LeetCode）](https://leetcode.cn/problems/find-the-maximum-sum-of-node-values/)

```python
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        res = sum(nums)
        delta = sorted([(x ^ k) - x for x in nums], reverse = True)
        for du, dv in zip(delta[::2], delta[1::2]):
            res = max(res, res + du + dv)
        return res 
```

## 树上直径

时间复杂度：$O(n)$

定义：**树上任意两节点之间最长的简单路径即为树的「直径」。**

定理：

- **对于无负边权的树，从树的任意节点出发寻找到距离最远的节点，一定是树直径的一个端点。** （反证）

方法一：两次dfs

```python
    def treeDiameter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        e = [[] for _ in range(n + 1)]
        for u, v in edges:
            e[u].append(v)
            e[v].append(u)
        def dfs(u, fa):
            res, mxv = 0, u
            for v in e[u]:
                if v == fa: continue
                a, b = dfs(v, u)
                if a + 1 > res:
                    res, mxv = a + 1, b 
            return res, mxv
        _, s = dfs(0, -1)
        res, _ = dfs(s, -1)
        return res
```

方法二：树形DP

返回每个节点 的最长路径fst 和 与最长路径没有公共边的次长路径 sec，取max(fst + sec) 

```python
    def treeDiameter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        e = [[] for _ in range(n + 1)]
        for u, v in edges:
            e[u].append(v)
            e[v].append(u)
        res = 0
        def dfs(u, fa):
            nonlocal res
            # 找出节点u 为子树的最长 / 次长路径
            fst = sec = -1 
            for v in e[u]:
                if v == fa: continue
                a, _ = dfs(v, u)
                if a >= fst:
                    fst, sec = a, fst
                else:
                    sec = max(a, sec)
            res = max(fst + sec + 2, res)        
            return fst + 1, sec + 1
        dfs(0, -1)
        return res
```

[310. 最小高度树 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-height-trees/description/?envType=daily-question&envId=2024-03-17)

树的直径问题，最小高度树的根一定在树的直径上。

```python
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
            e = [[] for _ in range(n)]
            for u, v in edges:
                e[u].append(v)
                e[v].append(u)
            # 确定以x 为根
            pa = [-1] * n
            def dfs(u, fa):
                pa[u] = fa
                res, mxv = 0, u
                for v in e[u]:
                    if v == fa:
                        continue
                    a, b = dfs(v, u)
                    if a + 1 > res:
                        res, mxv = a + 1, b
                return res, mxv
            _, x = dfs(0, -1)
            dis, y = dfs(x, -1)
            path = []
            while y != -1:
                path.append(y)
                y = pa[y]
            res = [path[dis // 2]]
            if dis & 1:
                res.append(path[dis // 2 + 1])
            return res
```

# 位运算

## 位运算与集合论

集合 $A, B$，最大二进制长度为 $N$

|           操作           | 位运算                    |
| :----------------------: | ------------------------- |
|           全集           | $(1 $<<$N)-1$             |
|           补集           | $\sim A$                  |
|         添加元素         | $A | (1$<<$i)$            |
|         删除元素         | $A \& \sim(1$<<$i)$       |
| 删除元素（一定在集合中） | $A \oplus(1$<<$i)$        |
|      属于 / 不属于       | $(A$>>$i) \& 1 = 1 / 0  $ |
|       删除最小元素       | $A\&(A-1)$                |
|           差集           | $A\& \sim B$              |
|  差集（子集） / 对称差   | $A\oplus B$               |
|      $A$ 包含于 $B$      | $A\&B=A$                  |

(1). 把b位置为1

通过 **或**  实现

```python
mask |= 1 << b 
```

(2). 把b位置清零

通过 **与非**实现

```python
mask &= ~(1 << b)
```

(3). 获得一个数从高到低的每一位的值

[1261. 在受污染的二叉树中查找元素 - 力扣（LeetCode）](https://leetcode.cn/problems/find-elements-in-a-contaminated-binary-tree/description/?envType=daily-question&envId=2024-03-12)

```python
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root

    def find(self, target: int) -> bool:
        target += 1
        node = self.root
        for b in range(target.bit_length() - 2, -1, -1):
            x = (target >> b) & 1
            node = node.right if x else node.left 
            if not node: return False 
        return True
```

**二维矩阵 压缩为一维二进制串**

```python
num = sum((ch == '.') << i for i, ch in enumerate(s))	# 010110
```

满足 $num >> x == s[i]$

```python
s = ["#", ".", ".", "#", ".", "#"]
num = sum((ch == '.') << i for i, ch in enumerate(s))	# 010110
print(bin(num))	# 0b 010110
```

**预处理所有子集的和**

时间复杂度：$O(n\cdot 2^n)$

```python
    sum_ = defaultdict(int)
    for i, x in enumerate(nums):
        for s in range(1 << i):
            sum_[(1 << i) | s] = sum_[s] + x
```

**从大到小枚举一个$s$ 的所有非空子集**

暴力做法是从 $s$ 出发，不断减1。但是中途需要规避不是 $s$ 子集的情况，相当于做 ”压缩版“ 的二进制减法：普通的二进制减法会把最低位的 1 变成 0，同时 1右边的 0 变成 1（例如 $101000 \rightarrow1 00111$）；”压缩版“ 的二进制减法只保留原集合中的的、右边的1，其余仍然是0。（例如 $101000 \rightarrow 100101，假设 s = 111101)$。保留的方法，就是 $\& s$。

```python
sub = s
while sub:
    # 处理 sub 的逻辑
    sub = (sub - 1) & s
```

**Gosper's Hack：枚举大小恰好为 $k$ 的子集**

例如当前为 $0100110$，下一个大小仍然为 $3$ 的集合是 $0101001$（$left = 0101000$，即 $sub + lowbit(sub)$；$right =000001$，即$left \oplus sub=0001111$，$right =left \oplus sub $ >> $2 / lowbit(sub)$。

时间复杂度：$O(n \cdot C(n,k))$，实际上优化不大

```python
    s = (1 << n) - 1
    sub = (1 << k) - 1
    def next_sub(x):
        lb = x & -x
        left = x + lb 
        right = ((left ^ x) >> 2) // lb
        return left | right 
    while sub <= s:
        # 处理 sub 逻辑
        sub = next_sub(sub)
```

**判断是否有两个连续（相邻）的1**

```python
(s & (s >> 1)) == 0	# 为True是表示没有两个连续的1
或者
(s & (s << 1)) == 0 
```

十进制长度

```python
m = int(log(n + 1, 10)) + 1
```

二进制长度	

```python
n = num.bit_lenght()
```

二进制中1的数量

```python
cnt = num.bit_count()
```

**十进制 int 转换 对应二进制的 int**

```python
def bin(x):
    res = 0
    i = 0
    while x:
        res = res + pow(10, i) * (x % 2)
        x >>= 1
        i += 1
    return res
```

**十进制转 $-2$ 进制**

[1017. 负二进制转换 - 力扣（LeetCode）](https://leetcode.cn/problems/convert-to-base-2/description/?envType=daily-question&envId=2024-04-28)

![image-20240428234840741](C:\Users\TsingPig\AppData\Roaming\Typora\typora-user-images\image-20240428234840741.png)

```python
    def baseNeg2(self, n: int) -> str:
        if n == 0: return '0'
        res = []
        while n:
            if n & 1: x = 1
            else: x = 0
            n = (n - x) // -2
            res.append(str(x))
        return ''.join(res[::-1])
```



**最大异或**

```python
def findMaximumXOR(self, nums: List[int]) -> int:
        n = max(nums).bit_length()
        res = mask = 0
        for i in range(n - 1, -1, -1):
            mask |= 1 << i 
            s, tmp = set(), res | (1 << i)
            for x in nums: # x ^ a = tmp -> a = tmp ^ x
                x &= mask
                if tmp ^ x in s:
                    res = tmp
                    break
                s.add(x)
        return res
```

## 拆位试填法

当发现题目要求所有元素按位运算得到的**最值**问题时，从高位开始考虑是否能为1/0 。

考虑过的状态记录在res中，不考虑的位用mask置为0表示。

```python
mask = res = 0
for b in range(n, -1, -1):
    mask |= 1 << b	# 蒙版
    for x in nums:
        x &= mask
    # 最大值 ...
    res |= 1 << b 		# 得到最大值
    mask &= ~(1 << b)	# 该位自由，不用考虑
```

3022 [给定操作次数内使剩余元素的或值最小](https://leetcode.cn/problems/minimize-or-of-remaining-elements-using-operations/)

https://leetcode.cn/problems/minimize-or-of-remaining-elements-using-operations/

```python
 		mask = res = 0
        for b in range(n, -1, -1):
            mask |= 1 << b
            ans_res = -1    # 初始值全是1
            cnt = 0
            for x in nums:
                ans_res &= x & mask 
                if ans_res > 0:
                    cnt += 1
                else:
                    ans_res = -1    # 重置初始值
            if cnt > k: # 说明这一位必然是1
                # mask这位蒙版就应置为0，表示后续都不考虑这位
                mask &= ~(1 << b)
                res |= 1 << b
        return res
```

# 动态规划

[划分型dp - 力扣（LeetCode）](https://leetcode.cn/problem-list/lfZOUTrA/)

[数位dp - 力扣（LeetCode）](https://leetcode.cn/problem-list/30QHpYGW/)

[状压dp - 力扣（LeetCode）](https://leetcode.cn/problem-list/ptud3zoQ/)

[线性dp / 背包 - 力扣（LeetCode）](https://leetcode.cn/problem-list/PAkZSAkX/)

[状态机dp - 力扣（LeetCode）](https://leetcode.cn/problem-list/oX87FqKK/)

[区间dp - 力扣（LeetCode）](https://leetcode.cn/problem-list/2UzczrXX/)

## 背包问题

$N$ 个物品，价值为$v_i$，重量为$w_i$，背包容量为$W$。挑选物品不超过背包容量下，总价值最大是多少。

- 0 - 1背包：每个物品用 0 或者 1 次。
- 完全背包：每个物品可以用 0 到 $+\infty$ 次。
- 多重背包：每个物品最多 $s_i$ 次。
- 分组背包：物品分为若干组，每一组里面选 0 或者1 次。

### 0 - 1 背包

状态表示：$f(i, j)$ 

- 集合 ：

  - 所有拿物品的选法
  - 条件：1. 只从前$i$ 个物品中选；2. 总重量 $\le j$ 

- 表示的属性（一般是$\max, \min, 个数$）：所有选法的总价值的最大值（$\max$ ）

  最终求解的问题 $f(N, W)$ 。

状态计算：

集合的划分问题：如何将集合$f(i,j)$ 划分成更小的可计算子集。

![image.png](https://pic.leetcode.cn/1710840104-YjZLqr-image.png)

```python
# f[i][j] 表示用前i 个物品，在总重量不超过j 的情况下，所有物品选法构成的集合中，总价值的最大值
# f[0][0] ~ f[N][0] = 0
# 考虑f[i][j] 对应集合的完备划分： 选i ，其子集的最大值是f[i - 1][j - w[i]] + v[i]，需要在 j - w[i] >= 0 满足
# 不选i， 其子集的最大值是 f[i - 1][j]。一定可以满足
for i in range(1, N + 1):
    for j in range(W + 1):
        f[i][j] = f[i - 1][j]
        if j - w[i] >= 0:
            f[i][j] = max(f[i][j], f[i - 1][j - w[i]] + v[i])
return f[N][W]
```

滚动数组优化为一维：逆序遍历

由于$f(i, j)$ 只和 $f(i-1, j)$ 有关。如果使用滚动数组$f(j)$ 优化，去掉第一维度，在同一个$i$ 下，如果正序遍历$j$ ，在恰好更新$f(j)$ 前所有$f(j'< j)$ 存放的是新值$f(i,j')$，所有$f(j''\geq j)$ 存放的是老值 $f(i-1,j'')$。

由于我们希望能够得到$f(i-1, j - w[i])$ ，所以我们必须逆序遍历$j$ ：在恰好更新$f(j)$ 前，$f(j'\leq j)$ 都是老值，表示$f(i-1, j')$。

所以$j$ 的枚举为$range(W, w[i]-1, -1)$

```python
f = [0] * (W + 1)
for i in range(1, N + 1):
    for j in range(W, w[i] - 1, -1):
        f[j] = max(f[j], f[j - w[i]] + v[i])
        # 此时f[j] 就代表 f[i - 1][j], f[j - w[i] 代表f[i - 1][j - w[i]]
return f[W]        
```

[题目详情 - LC2431. 最大限度地提高购买水果的口味 - HydroOJ](https://hydro.ac/d/nnu_contest/p/LC1)

增加限制条件：不超过k次使用折扣券。注意，k 的遍历方向也是逆序。

```python
    def maxTastiness(self, price: List[int], tastiness: List[int], maxAmount: int, maxCoupons: int) -> int:
        # f[i][j][k] 从前i 个物品，不超过容量j 的情况下，不超过k张券的最大价值
        # f[i][j][k] = max(f[i - 1][j][k], f[i - 1][j - w][k] + v, f[i - 1][j - w // 2][k - 1] + v)
        f = [[0] * (maxCoupons + 1) for _ in range(maxAmount + 1)]

        for w, v in zip(price, tastiness):
            for j in range(maxAmount, w // 2 - 1, -1):
                for k in range(maxCoupons, -1, -1):
                    if j - w >= 0:
                        f[j][k] = max(f[j][k], f[j - w][k] + v)
                    if k >= 1:
                        f[j][k] = max(f[j][k], f[j - w // 2][k - 1] + v)
        return f[maxAmount][maxCoupons]
```

**恰好装满型 0 - 1背包**

[2915. 和为目标值的最长子序列的长度 - 力扣（LeetCode）](https://leetcode.cn/problems/length-of-the-longest-subsequence-that-sums-to-target/description/?envType=featured-list&envId=OZhLbgFT?envType=featured-list&envId=OZhLbgFT)
$$
f[i][j] = max(f[i - 1][j], ~ f[i - 1][j - w] + v) ，第二个转移的条件是f[i - 1][j - w]> 0 或者  f[i - 1][j - w] =0 且 ~w =j
$$
可以通过初始值修改，将不合法的$f[i][j] 置为  -\infty$，合法的$f[i][j] \ge 0$。则初始值 $f[0][0] =0$ 

得到二维版本：

```python
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        # f[i][j] 表示从前i 个数中，和为j 的子序列的所有选法构成的集合中，子序列长度的最大值
        # f[n][target]
        # f[i][j] = max(f[i - 1][j], f[i - 1][j - w] + 1)
        n = len(nums)
        f = [[-inf] * (target + 1) for _ in range(n + 1)]
        f[0][0] = 0
        for i in range(1, n + 1):
            w = nums[i - 1]
            for j in range(target + 1):
                f[i][j] = f[i - 1][j]
                if j - w >= 0:
                    f[i][j] = max(f[i][j], f[i - 1][j - w] + 1)
        return f[n][target] if f[n][target] >= 0 else -1
```

优化：$j的上界可以优化为 \min(重量前缀, ~ target)$

```python
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        f = [0] + [-inf] * target
        pre = 0
        for w in nums:
            pre += w
            for j in range(min(pre, target), w - 1, -1):
                f[j] = max(f[j], f[j - w] + 1)
        return f[target] if f[target] >= 0 else -1
```

**分割等和子集问题**

给定一组数，判断是否可以分割成两个等和子集。

[416. 分割等和子集 - 力扣（LeetCode）](https://leetcode.cn/problems/partition-equal-subset-sum/description/)

```python
    def canPartition(self, nums: List[int]) -> bool:
        s, n = sum(nums), len(nums)
        if s & 1: return False 
        # f[i][j] 表示从前i个数中，分割成和为j是否可能。
        # f[n][s // 2]
        f = [1] + [0] * (s // 2)
        for x in nums:
            for j in range(s // 2, x - 1, -1):
                f[j] |= f[j - x]
        return f[s // 2] == 1
```



### 完全背包

**状态表示：$f(i, j)$ ** 同 0 - 1背包。

**状态计算：**对于集合的划分，按照第$i$ 个物品选几个（$0, 1, ... , $)  划分。

朴素做法：$O(N\cdot W^2)$

```python
for i in range(1, N + 1):
    for j in range(W + 1):
        for k in range(j // w[i] + 1):
            f[i][j] = max(f[i][j], f[i - 1][j - k * w[i]] + k * v[i])
return f[N][W]            
```

**冗余优化**：$O(N \cdot W)$

可以发现后面一坨的最大值等价于 $f(i, j - w)$
$$
\begin{align}
f[i,j]~ &=~Max(f[i-1,j],&  	&f[i-1,j-w]+v,&	&~f[i-1,j-2w]+2v,&	&~f[i-1,j-3w]+3v &,...)

\\

f[i,j-w]~ &= ~Max(	&		&f[i-1,j-w],&	&~f[i-1,j-2w]+v,&			&~f[i-1,j-3w]+2v,    &...)

\end{align} 
$$
所以 $f(i, j) = max \big(f(i - 1, j), f(i, j - w[i]) + v[i] \big)$， 

```python
for i in range(1, N + 1):
    for j in range(W + 1):
        f[i][j] = f[i - 1][j]
        if j - w[i] >= 0:
            f[i][j] = max(f[i][j], f[i][j - w[i]] + v[i])    
            # f[i][j - w[i]] 包含了 f[i - 1][j - k * w[i]] 的部分 （k >= 1）
return f[N][W]
```

**优化为一维**

```python
for i in range(1, N + 1):
    for j in range(w[i], W + 1):
        f[j] = max(f[j], f[j - w[i]] + v[i])
```

[518. 零钱兑换 II - 力扣（LeetCode）](https://leetcode.cn/problems/coin-change-ii/description/?envType=featured-list&envId=OZhLbgFT?envType=featured-list&envId=OZhLbgFT)

**完全背包求组合方案数**
$$
\begin{align}
f[i,j]~ &=~\sum (f[i-1,j],&  	&~f[i,j-c] )

\\

f[i,j-c]~ &= ~\sum(f[i-1,j-c],&	 &~f[i,j- 2 \cdot c])

\end{align}
$$

```python
    def change(self, amount: int, coins: List[int]) -> int:
        # f[i][j] 表示 前i 个硬币凑出 j 的方案数
        # 状态表示：从前i 个硬币中组合出j 的所有方案的集合
        # 属性：个数
        # 转移：对集合进行划分。
        # f[i][j] = f[i - 1][j] + f[i][j - c]
        n = len(coins)
        f = [[0] * (amount + 1) for _ in range(n + 1)]
        # f[i][0] = 1
        for i in range(n + 1): f[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                c = coins[i - 1]
                f[i][j] = f[i - 1][j]
                if j - c >= 0:
                    f[i][j] += f[i][j - c]
        return f[n][amount]
```

优化成一维：

```python
    def change(self, amount: int, coins: List[int]) -> int:
        # f[i][j] = f[i - 1][j] + f[i][j - c]
        n = len(coins)
        # 从前i 个中构成 j 的方案数
        f = [0] * (amount + 1)
        f[0] = 1
        for c in coins:
            for j in range(c, amount + 1):
                f[j] += f[j - c]
        return f[amount]
```



**求排列方案数：伪完全背包**

[377. 组合总和 Ⅳ - 力扣（LeetCode）](https://leetcode.cn/problems/combination-sum-iv/?envType=daily-question&envId=2024-04-22)

$f(i)$ 表示找出总和为 $i$ 的排列方案数，$f(i)=\sum f(i-w)$

```python
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        f = [0] * (target + 1)
        f[0] = 1
        for i in range(1, target + 1):
            for j in range(n):
                w = nums[j]
                if i - w >= 0:
                    f[i] += f[i - w]
        return f[target]
```





[1449. 数位成本和为目标值的最大数字 - 力扣（LeetCode）](https://leetcode.cn/problems/form-largest-integer-with-digits-that-add-up-to-target/description/?envType=featured-list&envId=OZhLbgFT?envType=featured-list&envId=OZhLbgFT)

每个数字有一个重量，可以无限选，问恰好重量为target的最大数字。（类似题目：长度最大的字典序最小串等）

先用完全背包模型求出最长长度，然后贪心的从9~1倒序遍历逆序构造。构造的条件是$f[target-w]+1 = f[target]$，即通过长度判断是否可以转移。

```python
    def largestNumber(self, cost: List[int], target: int) -> str:
        # 先求出能构成的最长数串
        # 每个物品重量W, 价值为1，
        # f[i][j] 表示从前i 个物品中选法中，能够构成的最大价值
        # f[i][j] = max(f[i][j], f[i][j - w])
        f = [0] + [-inf] * target
        for w in cost:
            for j in range(w, target + 1):
                f[j] = max(f[j], f[j - w] + 1)
        mxl = f[target]
        if mxl <= 0: return '0'
        res = ''
        # 贪心的构造，从高位到低位尽可能构造
        for x in range(9, -1, -1):
            w = cost[x - 1]
            while target - w >= 0 and f[target] == f[target - w] + 1:
                res += str(x)
                target -= w
        return res
```

### 多重背包

在完全背包的基础上，增加每个物品最多选择选择的次数限制 $s[i]$。

暴力做法：$O(N \cdot W ^2)$

```python
for i in range(1, n + 1):
    for j in range(W + 1):
        for k in range(min(c[i] + 1, j // w[i] + 1)):   
            f[i][j] = max(f[i][j], f[i - 1][j - k * w[i]] + k * v[i])
```

$$
f(i,j)=\max 	(f(i - 1,  j), 	&f(i-1,~ j-w)+v,& ~\cdots , &~ f(i-1,~ j - c \cdot w) + c \cdot v))&
\\
f(i, j - w)=\max(	&f(i-1,~ j-w),&	 ~\cdots , &~ f(i-1,~ j - c \cdot w) + (c-1) \cdot v),& ~f(i-1, j - (c + 1) \cdot w) + c \cdot v))
$$

可以发现无法借助完全背包的方法进行优化。

**二进制拆分重量为新的包裹**：$O(N \cdot W\cdot log(\sum W) \cdot )$

思路：将每一件最多能选 $c$ 个的物品拆分成若干个包裹，大小分别是$ 1, 2, \cdots, 2^k, c' $ ，例如 $c=500$, 拆分成$1, 2, \cdots, 128,245 $，可以证明这些数字可以枚举出$ 0 \sim 500$ 之间的所有数。将这些包裹看出是新的物品，有其对应的新的 重量 和 价值。

可以估算，总包裹的个数不超过 $ N \cdot log_2{(\sum W)}$ 。

```python
W, V = [], []
for _ in range(N):
    ow, ov, oc = map(int, input().split())
    k = 1
    while oc >= k:  # 例如10， 拆分成1，2，4和3
        W, V = W + [ow * k], V + [ov * k] 
        oc -= k
        k <<= 1
    if oc > 0:
        W, V = W + [ow * oc], V + [ov * oc]

f = [0] * (mxW + 1)
for w, v in zip(W, V):
    for j in range(mxW, w - 1, -1):
        f[j] = max(f[j], f[j - w] + v)
print(f[mxW])
```

### 分组背包

[9. 分组背包问题 - AcWing题库](https://www.acwing.com/problem/content/9/)

有$N$ 组物品，容量为$mxW$ 的背包，每组物品最多只能选其中一个。 例如，水果（苹果，香蕉，橘子）只能选一个或者不选。

$f(i, j)$ 从前$i$ 组选，总重量不超过 $j$  的所有选法方案的价值和的最大值。

状态转移：第$i$ 组物品一个都不选 $f(i-1,j)$，第$i$ 组物品选第$k$ 个 $f(i-1,j-w[i][k]) + v[i][k]$

```python
W, V = [[0] for _ in range(N + 1)], [[0] for _ in range(N + 1)]
for i in range(1, N + 1):
    K = int(input()) 
    for k in range(K):
        w, v = map(int, input().split())
        W[i], V[i] = W[i] + [w], V[i] + [v]
        
f = [0] * (mxW + 1) 
for i in range(1, N + 1):
    for j in range(mxW, -1, -1):
        for k in range(len(W[i])):
            if j - W[i][k] >= 0:
                f[j] = max(f[j], f[j - W[i][k]] + V[i][k])     
```

## 线性dp

### 最长上升子序列

$O(n^2)$ 做法，$f[i] 表示以nums[i] 结尾的所有上升子序列中最长的长度。$

```python
for i, x in enumerate(nums):
    for j in range(i):
        if nums[j] < x:
            f[i] = max(f[i], f[j] + 1)
```

$O(nlogn)$ 做法，$f[i] 表示长度为i的所有上升子序列中，子序列末尾的最小值$

正序遍历 $nums$ 中每一个数$x$， 二分找出$x$ 在$f$ 中的插入位置（恰好大于$ x$ 的位置）。

```python
# f[i] 表示长度为i 的子序列的末尾元素的最小值
f = []

# 找到恰好大于x的位置
def check(x, mid):
    return f[mid] >= x
for x in nums:
    lo, hi = 0, len(f)
    while lo < hi:
        mid = (lo + hi) >> 1
        if check(x, mid):
            hi = mid 
        else:
            lo = mid + 1
    if lo >= len(f):
        f.append(x)
    else:
        f[lo] = x
```



### 最长公共子序列

$ f[i][j] 表示从s[0: i] 和 s2[0: j] 中的最长公共子序列$

时间复杂度：$O(mn)$

可以证明：$f(i-1, j -1)+ 1 \ge \max(f(i-1,j), ~f(i,~j-1))$  

```python
#
# f[n][m] 
f = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s1[i - 1] == s2[j - 1]:
            f[i][j] = f[i - 1][j - 1] + 1
        else:
            f[i][j] = max(f[i - 1][j], f[i][j - 1])
```



### 编辑距离

```python
def getEditDist(s1, s2):
    m, n = len(s1), len(s2)
    f = [[inf] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1): f[i][0] = i
    for i in range(1, n + 1): f[0][i] = i
    f[0][0] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            a = f[i - 1][j] + 1
            b = f[i][j - 1] + 1
            c = f[i - 1][j - 1] + (1 if s1[i - 1] != s2[j - 1] else 0)
            f[i][j] = min(a, b, c)
    return f[m][n]
```



## 网格图dp

**最大 / 最小单趟路径和**

[LCR 166. 珠宝的最高价值 - 力扣（LeetCode）](https://leetcode.cn/problems/li-wu-de-zui-da-jie-zhi-lcof/description/)

求从左上角 $(0,0)$ 到右下角 $(m-1,~n-1)$ 能够获得的最大价值和。转移方程：$f(i,j)=g(i,j)+\max(f(i-1,j),~f(i,j-1))$。

```python
    def jewelleryValue(self, grid: List[List[int]]) -> int:
        # f(i, j) 表示到达 (i, j) 网格的最高价值
        m, n = len(grid), len(grid[0])
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                x = grid[i - 1][j - 1]
                f[i][j] = x + max(f[i - 1][j], f[i][j - 1])
        return f[m][n]
```

[64. 最小路径和 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-path-sum/)

巧妙设计初值：$f(1,0)=f(0,1)=0,其余为 inf$

```python
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        f = [[inf] * (n + 1) for _ in range(m + 1)]
        f[0][1] = f[1][0] = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                x = grid[i - 1][j - 1]
                f[i][j] = x + min(f[i - 1][j], f[i][j - 1])
        return f[m][n]
```

[120. 三角形最小路径和 - 力扣（LeetCode）](https://leetcode.cn/problems/triangle/description/)

将三角形转换成网格图：约束 $j \in [1,i]$。

```python
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = n = len(triangle)
        f = [[inf] * (n + 1) for _ in range(m + 1)]
        f[0][1] = 0
        for i in range(1, m + 1):
            for j in range(1, i + 1):
                x = triangle[i - 1][j - 1]
                f[i][j] = x + min(f[i - 1][j], f[i - 1][j - 1])
        return min(f[m][1: ])
```



[1289. 下降路径最小和 II - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-falling-path-sum-ii/description/?envType=featured-list&envId=DuoJVDZI?envType=featured-list&envId=DuoJVDZI)

求从上一层列下标不同位置处转移的路径最小和**。维护上一层的最小值、次小值**。时间复杂度从 $O(n^3)$ 优化到 $O(n^2)$。

```python
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        m = n = len(grid)
        if m == 1: return min(grid[0])
        f = [[inf] * (n + 1) for _ in range(m + 1)]
        mn = mn_2 = (0, -1)
        for i in range(1, m + 1):
            pmn, pmn_2 = mn, mn_2 
            mn = mn_2 = (inf, -1)
            for j in range(1, n + 1):
                x = grid[i - 1][j - 1]
                y = f[i][j] = x + pmn[0] if pmn[1] != j else x + pmn_2[0]
                if y < mn[0]: mn_2, mn = mn, (y, j)
                elif y == mn[0]: mn_2 = (y, j)
                elif y < mn_2[0]: mn_2 = (y, j)          
        return min(f[m])
```



**求路径方案数**

[63. 不同路径 II - 力扣（LeetCode）](https://leetcode.cn/problems/unique-paths-ii/description/)

巧妙设计初值，避免特殊边界讨论。

```python
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        f = [[0] * (n + 1) for _ in range(m + 1)]
        f[0][1] = 1
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                x = grid[i - 1][j - 1]
                f[i][j] = 0 if x else f[i - 1][j] + f[i][j - 1]
        return f[m][n]
```



### 多路线问题

[1463. 摘樱桃 II - 力扣（LeetCode）](https://leetcode.cn/problems/cherry-pickup-ii/description/?envType=featured-list&envId=DuoJVDZI?envType=featured-list&envId=DuoJVDZI)

双起点 + 双路线问题

$f(t,i,j)$ 表示共同来到第 $t$ 行，分别在 $(t,i)$ 和 $(t,j)$。为了表示出两个初始位置分别在 $(0,0)$ 和  $(0, n- 1)$，所有初始值设置为 $-inf$，同时将 $ f[0][0][n + 1] = 0$。

```python
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # f(t, i, j)
        res = 0
        f = [[[-inf] * (n + 2) for _ in range(n + 2)] for _ in range(m + 1)]
        f[0][0][n + 1] = 0
        for t in range(1, m + 1):
            for i in range(1, n + 1):
                x = grid[t - 1][i - 1]
                for j in range(1, n + 1):
                    y = 0 if i == j else grid[t - 1][j - 1]
                    mx = max(f[t - 1][i][j], f[t - 1][i - 1][j], f[t - 1][i + 1][j],\
                             f[t - 1][i][j - 1], f[t - 1][i - 1][j - 1], f[t - 1][i + 1][j - 1],\
                             f[t - 1][i][j + 1], f[t - 1][i - 1][j + 1], f[t - 1][i + 1][j + 1])
                    f[t][i][j] = x + y + mx 
                    if t == m: res = max(res, f[t][i][j])
        return res 
```



[741. 摘樱桃 - 力扣（LeetCode）](https://leetcode.cn/problems/cherry-pickup/description/?envType=featured-list&envId=DuoJVDZI?envType=featured-list&envId=DuoJVDZI)

同起点 + 双路线问题
$ f(t, i, j)  $ 表示 $A, B$ 共同走了 $t$ 步，分别到达 $(i, t - i), ~ (j, t - j) $。

为了区分没有采摘、不可达，初始值设定为 $-inf$；当 $i =j$时，表示当前 $A,B$ 在同一个位置，只能加一份价值 $grid[i][t-i]$，否则当前价值为 $grid[j][t - j] + grid[i][t-i]$ 。转移：$\max \{f(t-1,i,j),~f(t-1,i-1,j), ~f(t-1,i,j-1),~f(t-1,i-1,j-1)\}$。对于不可达的某个具体位置，检测到价值中有 $-1$ 时直接返回。

同时需要注意 $t$ 会对 $i$ 和 $j$ 的取值范围约束。最终答案：$f(2n-2,~n-1,~n-1)$

```python
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # f(t, i, j) 表示走了t 步， 分别到达 (i, t - i) 和 (j, t - j) 获得的最大得分
        n = len(grid)
        f = [[[-inf] * (n) for _ in range(n)] for _ in range(2 * n - 1)]
        f[0][0][0] = grid[0][0]
        for t in range(1, 2 * n - 1):
            for i in range(max(0, t - n + 1), min(n, t + 1)):
                x = grid[i][t - i]
                if x < 0: continue 
                for j in range(max(0, t - n + 1), min(n, t + 1)):
                    y = grid[j][t - j] if i != j else 0
                    if y < 0: continue 
                    mx = max(f[t - 1][i][j], f[t - 1][i - 1][j], f[t - 1][i][j - 1], f[t - 1][i - 1][j - 1])
                    f[t][i][j] = mx + x + y 
        res = f[2 * n - 2][n - 1][n - 1]
        return res if res != -inf else 0
```



## 区间dp

石子合并

[AcWing 282. 石子合并 - AcWing](https://www.acwing.com/activity/content/problem/content/1007/)

```python
s = [0] * (n + 1)
f = [[0] * n for _ in range(n)]
for i in range(n):
    s[i + 1] = s[i] + nums[i]
for l in range(2, n + 1):
    for i in range(n + 1 - l):
        j = i + l - 1   
        f[i][j] = inf
        for k in range(i, j):
            f[i][j] = min(f[i][j], f[i][k] + f[k + 1][j] + s[j + 1] - s[i])
```



[312. 戳气球 - 力扣（LeetCode）](https://leetcode.cn/problems/burst-balloons/description/?envType=featured-list&envId=PAkZSAkX?envType=featured-list&envId=PAkZSAkX)

长度统一处理：对于 length = 1, $f[i][i-1]$ 是0，$f[j + 1][j]$也是0。等价于没有

对于length = 2， $f[i][i+1] 其中一项 [i][i-1] + f[i+1][i+1]+...$  ，因此和长度大于等于3统一。

```python
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        f = [[0] * n for _ in range(n)]
        for l in range(1, n - 1):
            for i in range(1, n - l):
                j = i + l - 1
                for k in range(i, j + 1):  
                    f[i][j] = max(f[i][j], f[i][k - 1] + f[k + 1][j] + nums[k] * nums[i - 1] * nums[j + 1])
        return f[1][n - 2]
```

[375. 猜数字大小 II - 力扣（LeetCode）](https://leetcode.cn/problems/guess-number-higher-or-lower-ii/?envType=featured-list&envId=2UzczrXX?envType=featured-list&envId=2UzczrXX)

$ f[a, b] 表示从[a : b] 一定能获胜的最小金额$。一定制胜的策略是当前位置一定答错，同时选择左右两边较大区间

复杂度：$O(n^3)$

```python
    def getMoneyAmount(self, n: int) -> int:
        # f[a, b] 表示从[a : b] 一定能获胜的最小金额
        # 最多取到f[n + 1][n]
        f = [[0] * (n + 1) for _ in range(n + 2)]
        for l in range(2, n + 1):
            for i in range(1, n + 2 - l):
                j = i + l - 1
                f[i][j] = inf
                for k in range(i, j + 1):
                    f[i][j] = min(f[i][j], k + max(f[i][k - 1], f[k + 1][j]))
        return f[1][n]
```

[1039. 多边形三角剖分的最低得分 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-score-triangulation-of-polygon/description/?envType=featured-list&envId=2UzczrXX?envType=featured-list&envId=2UzczrXX)

![image.png](https://pic.leetcode.cn/1711619432-oDgIcO-image.png)

```python
    def minScoreTriangulation(self, values: List[int]) -> int:
        # f[i: j] 表示从[i: j] 的最小得分
        # f[0: n - 1]
        n = len(values)
        f = [[0] * (n + 1) for _ in range(n + 1)]
        for l in range(3, n + 1):
            for i in range(n + 1 - l):
                j = i + l - 1
                f[i][j] = inf
                for k in range(i + 1, j):
                    f[i][j] = min(f[i][j], f[i][k] + f[k][j] + values[i] * values[k] * values[j])
        return f[0][n - 1]
```

[95. 不同的二叉搜索树 II - 力扣（LeetCode）](https://leetcode.cn/problems/unique-binary-search-trees-ii/description/?envType=featured-list&envId=M60EuZ6w?envType=featured-list&envId=M60EuZ6w)

卡特兰数 + 区间dp，$f[i, j]$ 表示从 $i,i+1,~\cdots~, j$ 序列中构成的所有二叉搜索树的根节点（对应的列表）。

最终问题：$f(1,n)$，对于每个区间，枚举中间节点 $k \in [i,j]$，分别从左右子树对应的列表中（$f(i,k-1)$ 和 $f(k+1,j)$），利用乘法原理进行构造。

```python
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        # f[i, j] 表示用 1 .. j 构建的二叉搜索树的所有根节点列表
        # 枚举树根节点k in range(i, j + 1)
        # f[i, k - 1] 为所有左子树可能的根节点列表
        # f[k + 1, j] 为所有右子树可能的根节点列表
        f = [[[None] for _ in range(n + 2)] for _ in range(n + 2)]
        for l in range(1, n + 1):
            for i in range(1, n + 2 - l):
                j = i + l - 1
                f[i][j] = []
                for k in range(i, j + 1):
                    for left in f[i][k - 1]:
                        for right in f[k + 1][j]:
                            f[i][j].append(TreeNode(k, left, right))
        return f[1][n]
```

### 最长回文子序列

**求最长回文子序列长度问题**

$f[i: j]~ 表示s[i] \sim s[j] 中的最长回文子序列的长度$

[516. 最长回文子序列 - 力扣（LeetCode）](https://leetcode.cn/problems/longest-palindromic-subsequence/)

```python
    def mx_pal_subseq(self, s: str) -> int:
        # f(i, j) 表示 s[i] ~ s[j] 的最长回文子序列的长度
        n = len(s)
        f = [[0] * n for _ in range(n)]
        for i in range(n): f[i][i] = 1
        for l in range(2, n + 1):
            # i + l < n + 1
            for i in range(n + 1 - l):
                j = i + l - 1
                if s[i] == s[j]:
                    f[i][j] = f[i + 1][j - 1] + 2
                else:
                    f[i][j] = max(f[i + 1][j], f[i][j - 1])
        return f[0][n - 1]
```

推论：对于长度为 $n$ 的字符串，其最长回文子序列长度为 $L$， 则最少添加 $n - L$ 个字符可以使原串变成回文串。

[1312. 让字符串成为回文串的最少插入次数 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-insertion-steps-to-make-a-string-palindrome/?envType=featured-list&envId=PAkZSAkX?envType=featured-list&envId=PAkZSAkX)

[P1435 [IOI2000\] 回文字串 - 洛谷 | 计算机科学教育新生态 (luogu.com.cn)](https://www.luogu.com.cn/problem/P1435)

```python
    def minInsertions(self, s: str) -> int:
        # f[i: j] 表示从s[i] ~ s[j] 的 最长回文子序列
        n = len(s)
        f = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n):
            f[i][i] = 1
        for l in range(2, n + 1):
            for i in range(n + 1 - l):
                j = i + l - 1
                if s[i] == s[j]:
                    f[i][j] = f[i + 1][j -  1] + 2
                else:
                    f[i][j] = max(f[i + 1][j], f[i][j - 1])
        return n - f[0][n - 1]
```

[2002. 两个回文子序列长度的最大乘积 - 力扣（LeetCode）](https://leetcode.cn/problems/maximum-product-of-the-length-of-two-palindromic-subsequences/?envType=featured-list&envId=ptud3zoQ?envType=featured-list&envId=ptud3zoQ)

二进制枚举，将集合划分成互不相交的两部分。求各自最长回文子序列长度的乘积。$O(2^n\cdot n^2)$。

```python
    def maxProduct(self, s1: str) -> int:
        n, res = len(s1), 0
        s = (1 << n) - 2
        sub = s 
        def mx_pal_subseq(ss):
            m = len(ss)
            f = [[0] * m for _ in range(m)]
            for i in range(m): f[i][i] = 1 
            for l in range(2, m + 1):
                for i in range(m + 1 - l):
                    j = i + l - 1
                    if ss[i] == ss[j]:
                        f[i][j] = f[i + 1][j - 1] + 2 
                    else: 
                        f[i][j] = max(f[i + 1][j], f[i][j - 1])
            return f[0][m - 1]
        while sub:      
            s2 = ''.join([s1[j] for j in range(n) if (sub >> j) & 1])
            s3 = ''.join([s1[j] for j in range(n) if (sub >> j) & 1 == 0])
            cur = mx_pal_subseq(s2) * mx_pal_subseq(s3)
            if cur > res: res = cur 
            sub = (sub - 1) & s 
        return res 
```



### 最长回文子串

[5. 最长回文子串 - 力扣（LeetCode）](https://leetcode.cn/problems/longest-palindromic-substring/description/)

```python
    def longestPalindrome(self, s: str) -> str:
        # 定义f[i][j] 表示从 s[i] ~ s[j] 是否是回文字符串
        left = right = 0
        n = len(s)
        f = [[True] * (n + 1) for _ in range(n + 1)]
        for l in range(2, n + 1):
            for i in range(n + 1 - l):
                j = i + l - 1
                f[i][j] = s[i] == s[j] and f[i + 1][j - 1]
                if f[i][j]:
                    left, right = i, j
        return s[left: right + 1]
```



## 数位dp

**模板1：统计各位数字出现次数**

统计在 $[a, b]$ 区间各个数字出现的次数。

需要实现 $count(n, x)$  函数统计 $[1, n]  $  区间中数字 $x$ 出现的次数

```python
def count(n, x):
# 在 1 ~ n 中x数字出现的次数
# 上界 abcdefg
# yyyizzz , 考虑i位上x的出现次数
# 
# 1.1如果x不为0 yyy 为 000 ~ abc - 1, zzz 为 000 ~ 999
# 1.2x为0，yyy 为 001 ~ abc - 1， zzz 为 000 ~ 999
# 
# 2. yyy 为 abc, 
#     2.1 d < x时，0
#       2.2 d = x 时，zzz为 000 ~ efg
#       2.3 d > x 时，zzz为 000 ~ 999 
    s = str(n)
    res = 0
    n = len(s)
    for i in range(n):
        pre = 0 if i == 0 else int(s[:i])
        suf = s[i + 1:]
        if x == 0: res += (pre - 1) * pow(10, len(suf))
        else: res += pre * pow(10, len(suf))
        d = int(s[i])
        if d == x: res += (int(suf) if suf else 0) + 1 
        elif d > x: res += pow(10, len(suf))
    return res
def get(a, b):
    for i in range(10):
        print(count(b, i) - count(a - 1, i), end = ' ')
    print()
```

简化版：

```python
def count(n, x): # 统计 1 ~ n 中 数字 x 的出现次数
    res = 0
    s = str(n)
    m = len(s)
    for i in range(m):
        pre = 0 if i == 0 else int(s[: i])
        d = int(s[i])
        sufs = s[i + 1: ]
        if x == 0: pre -= 1
        if d > x: pre += 1
        if d == x: res += (int(sufs) if sufs else 0) + 1
        res += pre * pow(10, len(sufs))
    return res 
def get(a, b):
    for i in range(10):
        print(count(b, i) - count(a - 1, i), end = ' ')
    print()
```

[233. 数字 1 的个数 - 力扣（LeetCode）](https://leetcode.cn/problems/number-of-digit-one/description/?envType=featured-list&envId=30QHpYGW?envType=featured-list&envId=30QHpYGW)

```python
        def count(n, x): # 统计 1 ~ n 中 数字 x 的出现次数
            res = 0
            s = str(n)
            m = len(s)
            for i in range(m):
                pre = 0 if i == 0 else int(s[: i])
                d = int(s[i])
                sufs = s[i + 1: ]
                if x == 0: pre -= 1
                if d > x: pre += 1
                if d == x: res += (int(sufs) if sufs else 0) + 1
                res += pre * pow(10, len(sufs))
            return res 
        return count(n, 1)
```

**模板2：带限制数位dp 统计问题**

通用模板 v1.0：统计 $[1, ~n]$ 区间中，符合限制条件的数字个数。

$f(i,~mask,~is\_limit,~is\_num)$ 表示 前导数字集合为 $mask$，从第 $i$ 位开始往后填，能满足限制条件的数字个数。

其中， $is\_limit$ 表示前导是否恰好全都取到上界。为$True$ 时，$i$ 的上界 $hi = int(s[i])$ 否则 为9；

$is\_num$ 表示前导是否有数字。为 $True$ 时，$i$  的下界从$0$ 开始；否则可以继续不填数字，或者下界从 $1$ 开始。 

```python
        @lru_cache(maxsize = None)
        def f(i: int, mask: int, is_limit: bool, is_num: bool):
            if i == m: 
                if is_num: return 1
                return 0
            res = 0
            lo, hi = 0, 9
            if not is_num:
                lo = 1
                res += f(i + 1, mask, False, False)
            if is_limit:
                hi = int(s[i])
            for j in range(lo, hi + 1):
                # j 没有在mask 的集合中出现过
                if (mask >> j) & 1 == 0:
                    res += f(i + 1, mask | (1 << j), is_limit and j == hi, True)
            return res 
        return f(0, 0, True, False)
```

简化版本：

```python
        @lru_cache(None)
        def f(i, mask, is_limit, is_num):
            if i == len(s): return int(is_num)
            res = 0 if is_num else f(i + 1, mask, False, False)
            lo, hi = 0 if is_num else 1, int(s[i]) if is_limit else 9
            for j in range(lo, hi + 1):
                if (mask >> j) & 1 == 0:
                    res += f(i + 1, mask | (1 << j), is_limit and j == hi, True)
            return res 
```

时间复杂度：记$D = 10$，由于每个状态只会被计算一次，每个状态的复杂度是 $O(D)$；每一个 $(i, mask)$ 能够唯一确定 $(i,~mask,~is\_limit,~is\_num)$ 四元组（因此在记忆化的时候只需要$(i, mask)$ 维度），所以状态个数为 $m\cdot2^D$，其中 $m$ 表示 $n$ 的二进制长度。所以复杂度为： $O(D\cdot m \cdot 2^D)$

实际上某些问题中， $is\_num$ 可以 被简化掉，因为 $not(mask ==0)$  和 $is\_num$  是 等价的。



[2376. 统计特殊整数 - 力扣（LeetCode）](https://leetcode.cn/problems/count-special-integers/)

统计 $1 \sim n$  中各个数位都不相同的数字的个数。限制条件：$mask$ 前导中出现过的数字是不可以填的。

```python
    def countSpecialNumbers(self, n: int) -> int:
        s = str(n)
        @lru_cache(None)
        def f(i, mask, is_limit, is_num):
            if i == len(s): return int(is_num)
            res = 0 if is_num else f(i + 1, mask, False, False)
            lo, hi = 0 if is_num else 1, int(s[i]) if is_limit else 9
            for j in range(lo, hi + 1):
                if (mask >> j) & 1 == 0:
                    res += f(i + 1, mask | (1 << j), is_limit and j == hi, True)
            return res 
        return f(0, 0, True, False)
```

[788. 旋转数字 - 力扣（LeetCode）](https://leetcode.cn/problems/rotated-digits/description/?envType=featured-list&envId=30QHpYGW?envType=featured-list&envId=30QHpYGW)

统计区间：$1 \sim N$ 中的所有数字，每个数位都被旋转。

限制条件：旋转后不等于自身，且合法的数字。只需要在数字中包含至少 一个 $[2, 5, 6, 9]$ 且不包含 $[3, 4, 7]$。

```python
    def rotatedDigits(self, n: int) -> int:
        s = str(n)
        m = len(s)
        # 合法情况：包含至少一个 [2, 5, 6, 9] 且 不包含 [3, 4, 7]
        nums = [0, 0, 1, -1, -1, 1, 1, -1, 0, 1]
        @lru_cache(None)
        def f(i, has_mir, is_limit, is_num):
            if i == m: return int(has_mir and is_num)
            res = 0 if is_num else f(i + 1, has_mir, False, False)
            lo, hi = 0 if is_num else 1, int(s[i]) if is_limit else 9
            for j in range(lo, hi + 1):
                if nums[j] != -1:
                    res += f(i + 1, has_mir or nums[j] == 1, is_limit and j == hi, True)
            return res
        return f(0, False, True, False)
```

[902. 最大为 N 的数字组合 - 力扣（LeetCode）](https://leetcode.cn/problems/numbers-at-most-n-given-digit-set/description/?envType=featured-list&envId=30QHpYGW?envType=featured-list&envId=30QHpYGW)

```python
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s = str(n)
        ss = set([int(ch) for ch in digits])
        m = len(s)
        @lru_cache(None)
        def f(i, is_limit, is_num):
            if i == m: return int(is_num)
            res = 0 if is_num else f(i + 1, False, False)
            lo, hi = 0 if is_num else 1, int(s[i]) if is_limit else 9
            for j in range(lo, hi + 1):
                if j in ss:
                    res += f(i + 1, is_limit and j == hi, True)
            return res
        return f(0, True, False)
```

[2827. 范围中美丽整数的数目 - 力扣（LeetCode）](https://leetcode.cn/problems/number-of-beautiful-integers-in-the-range/description/)

运用模运算的性质：整个数字 模 $k$ 的结果，比如 $1234 \mod 17$ ，可以看成 $(1000 \mod 17) + (200 \mod 17)+(30 \mod 17 )+ (4 \mod 17)$，所以最后模数 的结果只需要等价成不断 $mod\_res \times 10 + j$ 即可。

```python
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        def cal(x):
            s = str(x)
            m = len(s)
            @lru_cache(None)
            def f(i, mod_res, odd_even_delta, is_limit, is_num):
                if i == m: return int(odd_even_delta == 0 and mod_res == 0 and is_num)
                res = 0 if is_num else f(i + 1, mod_res, odd_even_delta, False, False)
                lo, hi = 0 if is_num else 1, int(s[i]) if is_limit else 9
                for j in range(lo, hi + 1):
                    res += f(i + 1, (mod_res * 10 + j) % k, odd_even_delta + (1 if j & 1 else -1), is_limit and j == hi, True)
                return res
            return f(0, 0, 0, True, False)
        return cal(high) - cal(low - 1)
            
```

[600. 不含连续1的非负整数 - 力扣（LeetCode）](https://leetcode.cn/problems/non-negative-integers-without-consecutive-ones/description/?envType=featured-list&envId=30QHpYGW?envType=featured-list&envId=30QHpYGW)

二进制数位dp。上界改为1

```python
    def findIntegers(self, n: int) -> int:
        def get_bin(x):
            res = i = 0
            while x:
                res = res + pow(10, i) * (x % 2)
                i += 1
                x >>= 1
            return res
        n = get_bin(n)
        s = str(n)
        m = len(s)
        @lru_cache(None)
        def f(i, pre, is_limit, is_num):
            if i == m: return int(is_num)
            res = 0 if is_num else f(i + 1, None, False, False)
            lo, hi = 0 if is_num else 1, int(s[i]) if is_limit else 1
            for j in range(lo, hi + 1):
                if pre == None or (j == 1 and pre != 1) or j == 0:
                    res += f(i + 1, j, is_limit and j == hi, True)
            return res 
        return f(0, None, True, False) + 1
```



## 状态机dp

[3068. 最大节点价值之和 - 力扣（LeetCode）](https://leetcode.cn/problems/find-the-maximum-sum-of-node-values/)

0 表示当前异或偶数个k，1表示当前异或奇数个k

$0 \rightarrow 0 或者 1 \rightarrow 1$：$加上x$

$0 \rightarrow 1 或者 1 \rightarrow 0$： $ 加上x \oplus k$

```python
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        dp = [[0] * 2 for _ in range(n + 1)]
        dp[n][1] = -inf
        for i, x in enumerate(nums):
            dp[i][0] = max(dp[i - 1][0] + x, dp[i - 1][1] + (x ^ k))
            dp[i][1] = max(dp[i - 1][1] + x, dp[i - 1][0] + (x ^ k))
        return dp[n - 1][0]
```

## 状压dp / 状态压缩dp

[291. 蒙德里安的梦想 - AcWing题库](https://www.acwing.com/problem/content/293/)

竖方块摆放确定时，横方块摆放一定确定（合法或者恰好填充），所以只需要看竖方块的摆放情况。对于$N\times M $ 的方格，$f(i, j) 第~i~行形态为~j时，前~i~行合法切割方案数。$ $j$ 是用十进制记录$M$ 位二进制数，其每位数字为1 表示放竖方块上半部分，为0 表示其他情况。（竖方块下半部分 / 横方块）

$f(i,j)$ 能由 $f(i-1, k)$ 状态转移的充要条件：1. $j ~\&~ k =0$ ，保证同列上下两行不会同时放竖方块的上半部分。2. $j ~|~ k$ 的所有连续的 0 的个数必须是偶数。$j ~|~ k$ 为 0 当且仅当上下两行都是横方块，所以必须是偶数个。

初始状态对于$f(0)$ ，不能对第一行产生影响，所以只有$f(0,~0) = 1$ ，其余为0。最终目标：$f(N, 0)$ ，状态转移方程：$f(i,j) = \sum valid(f(i-1,k))$

对于所有$M$ 位二进制数，预处理其是否满足所有连续0的个数是否是偶数。

![image.png](https://pic.leetcode.cn/1712657543-VVJdTp-image.png)

```python
    N = M = 11
    f = [[0] * (1 << M + 1) for _ in range(N + 1)]
    def solve(n, m):
        # f[n][1 << m]
        # 预处理，判断 i 是否含有连续的奇数个0
        s = set()
        for i in range(1 << m):
            c = 0
            for j in range(m):
                if i >> j & 1:
                    if c & 1: break
                else: c += 1
            if c & 1: s.add(i)
        f[0][0] = 1
        for i in range(1, n + 1):
            for j in range(1 << m):
                f[i][j] = 0
                for k in range(1 << m):
                    if (j & k == 0 and (j | k not in s)):
                        f[i][j] += f[i - 1][k]
        return f[n][0]
```

**最短哈密顿回路 / 旅行商问题**

哈密顿回路：无向带权图中经过所有顶点的回路。朴素做法对于 $N$ 个顶点，时间复杂度为 $O(n!)$ ，是$NP-hard$ 问题（无法在多项式时间复杂度内求解）。

实际上，设已经访问过的点集 $S$，当前节点 $j$ ，设$f(S,j)$ 表示路径已经访问过点集$S$ 中的点且当前访问的$j$ 时 的最短路径。有状态转移：$f(S,j) = \min \{f(S-j, k) + w(k,~j) ~, \forall~k \in S-j \}$。可以用二进制来压缩已经访问的点集 $S$。最终问题 $f(2^N -1, N - 1 )$，初始值 $f(0, 0) = 0$。

```python
def solve():
    n = int(input())
    f = [[inf] * n for _ in range(1 << n)]
    w = []
    for _ in range(n):
        w.append(list(map(int, input().split())))
    f[1][0] = 0
    for S in range(1, 1 << n):
        for j in range(n):
            if (S >> j) & 1:    # j 在S 中，
                for k in range(n):
                    if ((S ^ (1 << j)) >> k) & 1:  # 且 k 在 S - j 中
                        f[S][j] = min(f[S ^ (1 << j)][k] + w[k][j], f[S][j])
    return f[(1 << n) - 1][n - 1]
```

### 全排列型状压

**朴素 - 全排列状压**

[1879. 两个数组最小的异或值之和 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-xor-sum-of-two-arrays/description/?envType=featured-list&envId=ptud3zoQ?envType=featured-list&envId=ptud3zoQ)

$O(n^2 \times 2^n )$ 做法：$f(i, s)$ 表示考虑完成 $nums[0: i]$ ，状态为 $s$ 之下，最小异或值之和。

```python
class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums2)
        f = [[inf] * (1 << n) for _ in range(n + 1)]
        for i in range(n + 1): f[i][0] = 0
        for i in range(1, n + 1):
            x = nums1[i - 1]
            for s in range(1, 1 << n):
                for j in range(n):
                    if (s >> j) & 1 == 0: continue 
                    f[i][s] = min(f[i][s], f[i - 1][s ^ (1 << j)] + (x ^ nums2[j]))
        return f[n][(1 << n) - 1]
```

优化：省略前一维度，这是因为 $i$ 的信息隐含在 $s$ 所含1的个数之中。时间复杂度 $O(n\times 2^n)$

```python
class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums2)
        f = [inf] * (1 << n) 
        f[0] = 0
        for s in range(1, 1 << n):
            x = nums1[s.bit_count() - 1]
            for j in range(n):
                if (s >> j) & 1 == 0: continue 
                f[s] = min(f[s], f[s ^ (1 << j)] + (x ^ nums2[j]))
        return f[(1 << n) - 1]

```



**约束型 - 全排列状压**

对于带有约束的全排列问题，$f[i][s]$ 表示考虑完全排列 $p[0: i]$ ，已经选择集合状态为 $s$ 情况下的合法方案数。一般转移方程：$f[i][s]=\sum f[i-1][s-\{j\}],~ \forall ~valid(j)$，初始化 $f[0][0]=1$。时间复杂度为 $O(n^2 \times 2^n)$。

优化思路：由于 $s$ 中包含了 $i$ 的信息，即  $bin(s).count('1')$  ，所以第一维度可以省略。时间复杂度 $O(n\times 2^n)$

[526. 优美的排列 - 力扣（LeetCode）](https://leetcode.cn/problems/beautiful-arrangement/description/?envType=featured-list&envId=ptud3zoQ?envType=featured-list&envId=ptud3zoQ)

时间复杂度为 $O(n^2 \times 2^n)$。

```python
class Solution:
    def countArrangement(self, n: int) -> int:
        res = 0
        # f[i][s]  考虑完perm[1] ~ perm[i]，已选择状态为s
        m = (1 << n) - 1
        f = [[0] * (m + 1) for _ in range(n + 1)]
        f[0][0] = 1
        for i in range(1, n + 1):
            for s in range(m + 1):
                for j in range(n):
                    if (s >> j) & 1 and ((j + 1) % i == 0 or i % (j + 1) == 0):
                        f[i][s] += f[i - 1][s ^ (1 << j)]
        return f[n][m]
```

优化：省略前一维度。时间复杂度 $O(n\times 2^n)$

```python
class Solution:
    def countArrangement(self, n: int) -> int:
        res = 0
        # f[i][s]  考虑完perm[1] ~ perm[i]，已选择状态为s
        m = (1 << n) - 1
        f = [1] + [0] * m
        for s in range(m + 1):
            i = bin(s).count('1')
            for j in range(n):
                if (s >> j) & 1 and ((j + 1) % i == 0 or i % (j + 1) == 0):
                    f[s] += f[s ^ (1 << j)]
        return f[m]
```



[2741. 特别的排列 - 力扣（LeetCode）](https://leetcode.cn/problems/special-permutations/description/?envType=featured-list&envId=ptud3zoQ?envType=featured-list&envId=ptud3zoQ)

$f(s,i)$ 表示当前选择的状态为 $s$ ，最后一个位置选择的元素为 $nums[i]$ 。对所有在 $s$ 中的 $i$ ，考虑其所有可能的前一个位置的值 $nums[j]$。$f(s,i)=\sum f(s\oplus j,~j),~\forall \text{valid}(j)$。复杂度：$O(n^2\cdot 2^n)$。

```python
moder = 10 ** 9 + 7 
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        f = [[0] * n for _ in range(1 << n)]
        f[0][0] = 1
        for s in range(1 << n):
            for i in range(n):
                if (s >> i) & 1 == 0: continue 
                if (s ^ (1 << i)) == 0:
                    f[s][i] = 1
                    continue 
                for j in range(n):
                    if i == j or (s >> j) & 1 == 0: continue 
                    x, y = nums[i], nums[j]
                    if x % y == 0 or y % x == 0:
                        f[s][i] = (f[s][i] + f[s ^ (1 << i)][j]) % moder   
        res = 0
        for i in range(n):
            res = (res + f[s][i]) % moder  
        return res 
```







### 划分成 $k$ 个子集的问题

$f(i,s)$ 表示划分到第 $i$ 个子集，划分的状态为 $s$ 情况下的某个值。$f(i,s)=F((f(i-1,s-sub),~G(sub) ))$。

时间复杂度： $O(n\cdot 3^n)$。由于元素个数为 $i$ 的集合个数有 $C(n,i)$个，其子集个数为$2^i$ ，根据二项式定理 $(a + b) ^n = \sum_{i=0}^n C_n^ia^ib^{n-i}$，所以$\sum_{i=0}^{n} C(n,i)\cdot 2^i = (2+1)^n=3^n$，每次需要 $O(n)$ 时间计算 $G$的情况下，时间复杂度为 $O(n\cdot 3^n)$

[2305. 公平分发饼干 - 力扣（LeetCode）](https://leetcode.cn/problems/fair-distribution-of-cookies/description/?envType=featured-list&envId=ptud3zoQ?envType=featured-list&envId=ptud3zoQ)

最小化 $k$ 个子集和中的最大值问题。$f(i,s)$ 表示划分到第 $i$ 个子集，划分的状态为 $s$ 情况下的 $i$ 个子集中和最大值的最小值。

考虑 $s$ 的所有子集$sub$ ，$f(i,s)=\min \{ \max(f(i-1,s-sub),~\sum sub)\}$。最终答案为 $f(k,1$<<$n-1)$，初始值 $f(0,0)=0$。

```python
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        # f[i][s] 表示当前划分状态为s,s为1表示已经分配
        # 划分完第i 个集合，所有集合的最大值 的最小值
        # f[i][s] = min(max(f[i - 1][s ^ sub], sum(sub)))
        # f[k][1 << n - 1]
        n = len(cookies)
        f = [[inf] * (1 << n) for _ in range(k + 1)]
        f[0][0] = 0
        for i in range(1, k + 1):
            for s in range(1, 1 << n):
                sub = s 
                while sub:
                    tot = sum(cookies[j] for j in range(n) if (sub >> j) & 1)
                    f[i][s] = min(f[i][s], max(f[i - 1][s ^ sub], tot))
                    sub = (sub - 1) & s
        return f[k][(1 << n) - 1]
```

[1723. 完成所有工作的最短时间 - 力扣（LeetCode）](https://leetcode.cn/problems/find-minimum-time-to-finish-all-jobs/description/)

此题是上一题的数据增强版，优化方法：预处理所有子集的和 + 一维滚动状压dp。复杂度：$O(3^n+ n\cdot 2^n)$

```python
    def minimumTimeRequired(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = [inf] * (1 << n) 
        f[0] = 0
        sum_ = defaultdict(int)
        for i, x in enumerate(nums):
            for s in range(1 << i):
                sum_[(1 << i) | s] = sum_[s] + x

        for _ in range(1, k + 1):
            for s in range((1 << n) - 1, 0, -1):
                sub = s
                while sub:
                    tot = sum_[sub]
                    if f[s ^ sub] > tot: tot = f[s ^ sub]
                    if f[s] > tot: f[s] = tot
                    sub = (sub - 1) & s
        return f[(1 << n) - 1]
```

**划分集合每个和不超过 $k$ 的最少划分数**

[1986. 完成任务的最少工作时间段 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-number-of-work-sessions-to-finish-the-tasks/description/?envType=featured-list&envId=ptud3zoQ?envType=featured-list&envId=ptud3zoQ)

$f(s)$ 表示到达这个状态需要的最少划分段数。枚举每个子集 $sub$ ，$f(s)=\min \{f(s-sub)+1\},~\forall \sum sub\le k$。时间复杂度：$O(3^n+n\cdot 2^n)$

```python
    def minSessions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = [inf] * (1 << n)
        f[0] = 0 
        # 预处理所有子集的和
        sum_ = defaultdict(int)
        for i, x in enumerate(nums):
            for sub in range(1 << i):
                sum_[sub | (1 << i)] = sum_[sub] + x 
        for s in range(1, 1 << n):
            sub = s
            while sub:
                if sum_[sub] <= k: 
                    f[s] = min(f[s], f[s ^ sub] + 1)
                sub = (sub - 1) & s 
        return f[(1 << n) - 1]
```



**集合是否能划分成 k 个相等子集**

[698. 划分为k个相等的子集 - 力扣（LeetCode）](https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/description/?envType=featured-list&envId=ptud3zoQ?envType=featured-list&envId=ptud3zoQ)

$f[s]$ 为在压缩状态 $s$ 下的余数。考察每一个在集合中的元素 $nums[j]$，对于删去其的集合 $ls=f[s \oplus(1$<<$j)]$，当且仅当 $ls+nums[j] \le siz$  的时候可以更新 $f[s]$，相当于枚举所有删去一个元素的子集向 $f[s]$ 转移，能否构造出整数倍的集合。

这种方法会有一定的重复，不妨反过来，对于 $f[s]$ ，考察其没有出现的每一个元素 $nums[j]$，更新 $f[s | nums[j]]$。这样可以大大减少重复。

> 时间复杂度：不超过 $O(n \cdot 2^n)$

```python
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        siz = sum(nums) // k
        if sum(nums) % k != 0 or any(x > siz for x in nums): return False
        # f[s] 表示 在选择状态为s的情况下，余数是多少
        n = len(nums)
        m = (1 << n) - 1
        f = [0] + [-inf] * m
        for s in range(m):
            if f[s] == -inf: continue
            for j in range(n):
                if (s >> j) & 1 == 0:
                    nx = s | (1 << j)
                    if f[nx] == 0: continue 
                    if f[s] + nums[j] <= siz:
                        f[nx] = (f[s] + nums[j]) % siz 
        return f[m] == 0
```

### 多重状压：记忆化搜索

当某些字符、数字可以使用 若干次时，传统的状压不方便表示使用状况。因此可以转用 $dfs$ 的记忆化搜索方式，配合 $Counter$ 计数器实现状压的代替品。

[691. 贴纸拼词 - 力扣（LeetCode）](https://leetcode.cn/problems/stickers-to-spell-word/description/?envType=featured-list&envId=ptud3zoQ?envType=featured-list&envId=ptud3zoQ)

其中剪枝部分，要求 $s[0]$ 一定在 $word$中出现。这是因为如果当前 $word$ 中存在能消除 $s[0]$ 的，那么最终解一定至少包含这些部分。否则，没有能消除 $s[0]$ 的，表示当前 $dfs(s)$ 的结果不合法，返回 $inf$。这样实际上约束了每次一定转移到最优的方案。

例如对于 $s=the$, 首先寻找所有包含 $t$ 的方案并向其转移。时间复杂度接近 $O(n\cdot m)$ ，$n$  为原始字符串大小，$m$  为可以考虑的字符串数量。

```python
    def minStickers(self, words: List[str], target: str) -> int:
        words = [Counter(word) for word in words]
        # dfs(s) 表示得到s 的最少数量
        @lru_cache(None)
        def dfs(s):
            if s == '': return 0
            cs = Counter(s)
            res = inf 
            for word in words:
                # 如果word压根无法消除s[0] 可以直接跳过
                # 因为再怎么使用也无法完全消除s
                # 应该首先考虑将s[0] 能消除的方案
                if s[0] not in word: continue 
                ns = s
                for k, v in word.items():
                    ns = ns.replace(k, '', v)
                res = min(res, dfs(ns) + 1)
            return res 
        res = dfs(target)
        return res if res < inf else -1
```

### $k$ 进制状压

 **$k$ 种颜色染色 $n \times m$ 网格（不允许出现空着的格子）问题**

[1931. 用三种不同颜色为网格涂色 - 力扣（LeetCode）](https://leetcode.cn/problems/painting-a-grid-with-three-different-colors/description/?envType=featured-list&envId=ptud3zoQ?envType=featured-list&envId=ptud3zoQ)

$k$ 进制预处理 + 合法状态预处理 + 枚举状压

每一行使用长度为 $m$ 的 $k$ 进制的串来表示。通过预处理的方式记录在 $color$ 中，键为 $k$ 进制的串对应的十进制数，值为对应的 $k$ 进制串的列表。相邻两行的约束，通过枚举来预处理。转移方程：$f(i,s)= \sum f(i-1, ~e[s])$

时间复杂度：$O(k^{2m}\times n)$

```python
moder = 10 ** 9 + 7
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        # 三进制表示每一行的颜色
        colors = {}
        for b in range(3 ** m):
            color = []
            x = b
            while x:
                color.append(x % 3)
                x //= 3
            color.extend([0] * (m - len(color)))
            if any(color[i] == color[i + 1] for i in range(len(color) - 1)):
                continue 
            colors[b] = color[::-1]
        
        e = defaultdict(list)
        # 预处理每一种状态可以邻接的状态
        for i, u in colors.items():
            for j, v in colors.items():
                flag = True 
                for b in range(m):
                    if u[b] == v[b]:
                        flag = False 
                        break 
                if flag: e[i].append(j)
                    
        # f[i][s] 表示i行为s的方案数
        f = [[0] * (3 ** m) for _ in range(n)]
        for b in colors.keys():
            f[0][b] = 1
        for i in range(1, n):
            for s in colors.keys():
                for ps in e[s]:
                    f[i][s] = (f[i - 1][ps] + f[i][s]) % moder 
        return (sum(f[n - 1])) % moder 
```



## 划分dp

### 约束划分个数

将数组分成 (恰好/至多) $k$ 个连续子数组，计算与这些子数组有关的最优值。

类型1： $f[i][j]$ 当前考虑完前缀 $a[:i]$，且$a[:i]$ 恰好划分成 $j$ 个连续子数组所得到的最优解。 枚举最后一个子数组的左端点 $L$, 从 $f[L][j-1]$ 转移到 $f[i][j]$，并考虑 $a[L:i]$ 对最优解的影响。 $f(i,j)=\min(f(L,j-1))$

类型2：$f(i,j, pre)$ 表示当前考虑到 $a[i]$， 且$a[:i]$ 的前缀中包含 $j$ 个连续子数组所得的最优解，其中 $pre$ 表示当前待划分的这段的状态。 考虑是否在 $i$ 处划分，并考虑前一段状态 $pre$ 是否允许划分。$f(i,j,pre)=\min \{~f(i+1,j,pre),~f(i+1,j+1,pre')~\}$ 

[3117. 划分数组得到最小的值之和 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-sum-of-values-by-dividing-array/description/)

$f(i, j, pre\_and):$ 表示当前考虑到$nums[i]$，且前缀中包含 $j$ 段，$pre\_and$ 表示当前待划分的这段的AND。

```python
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        n, m = len(nums), len(andValues)
        @lru_cache(None)
        def f(i, j, pre_and):
            # 表示当前考虑到nums[i]，且前缀中包含j 段，pre_and表示当前待划分的这段的AND
            if i == n and j == m: return 0
            if i < n and j == m: return inf 
            if i == n and j < m: return inf
            pre_and &= nums[i]
            # 在i处不划分，
            res = f(i + 1, j, pre_and)
            # 在i处划分，条件是这一段 pre_and == andValues[j]
            if pre_and == andValues[j]:
                res = min(res, f(i + 1, j + 1, -1) + nums[i])
            return res
        res = f(0, 0, -1)
        return res if res < inf else -1
```

时间复杂度：$O(mn\log U)$，由于 $ pre\_and$ 表示当前待划分这段的按位与。记 $\log U$ 表示最大数对应的二进制位数。对于一个确定的 $i$，向前 AND 每次不变或者减少比特1的个数。所以不同的$pre\_and$ 数不超过 $logU$。总共有 $mn \log U$ 个状态，每个状态是 $O(1)$ 。

### 不相交区间

[1235. 规划兼职工作 - 力扣（LeetCode）](https://leetcode.cn/problems/maximum-profit-in-job-scheduling/?envType=featured-list&envId=pjhpmdeh?envType=featured-list&envId=pjhpmdeh)

如果报酬等于区间长度（时间差），是一个贪心 + 排序问题：按照结束时间排序，结束早的优先考虑。本题的报酬与区间长度无关，因此需要 $dp$ 。

原始问题是考虑 $ 0 \sim \max (endTime)$ 时间段内，能够获得的最大报酬。考虑子问题 $0 \sim endTime[i]$ 时间段内的最大报酬。

$f[x]$  表示 $ 0 \sim endTime[x] $ 时间段内的最多报酬，一种转移是 $f[x-1]$，表示当前区间 $x$ 不考虑；另一种转移，考虑结束时间  $ \le startTime[x]$ 的最后一个位置 $idx$ ，有 $endTime[idx]\le startTime[x]$（可以发现 $f[x]$ 关于 $x$ 递增，最后一个位置一定是最大值），不妨同样按照结束时间从小到大排序，因此可以使用二分查找。

实现时，在数组前面增加一个 $(0,0,0)$ 用于统一查找。

时间复杂度：$O(n \log n)$ 

```python
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # f[x] 表示 0 ~ endTime[x] 时间段内的最多报酬
        n = len(startTime)
        nums = [(0, 0, 0)] + sorted([(s, e, p) for s, e, p in zip(startTime, endTime, profit)], key = lambda x: x[1])
        f = [0] * (n + 1)
        def bisect_left(lo, hi, k):
            while lo < hi:
                mid = (lo + hi) >> 1
                if nums[mid][1] > k:
                    hi = mid 
                else:
                    lo = mid + 1
            return lo - 1
        for i in range(1, n + 1):
            idx = bisect_left(0, i, nums[i][0])
            f[i] = max(f[i - 1], f[idx] + nums[i][2])
        return f[n]
```



# 贪心

## 排序贪心

[406. 根据身高重建队列 - 力扣（LeetCode）](https://leetcode.cn/problems/queue-reconstruction-by-height/description/)

贪心：先按照身高，从大到小排序；
同身高内，按照k从小到大排序
前缀性质：任何一个p的前面的所有的h一定比自己大

```python
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # [7, 0] [7, 1] [6, 1] [5, 0] [5, 2] [4, 4]
        people.sort(key = lambda x: -x[0] * 10 ** 5 + x[1])
        res = []
        for i, p in enumerate(people):
            h, k = p[0], p[1]
            if k == i:
                res.append(p)
            elif k < i:
                res.insert(k, p)
        return res
```

[857. 雇佣 K 名工人的最低成本 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-cost-to-hire-k-workers/description/?envType=daily-question&envId=2024-05-02)

排序贪心 + 堆维护 $k$ 个最小和。对任意一个员工子集，按照比例支付费用、且任意一个员工不少于阈值，等价于支付费用 = $\max(\frac{w_i}{q_i}) \times \sum_{i=1}^{k}q_i$。按照$\frac{w_i}{q_i}$ 从大到小排序，维护对应的 $k$ 个最小$q$ 的和。

```python
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        nums = sorted([(w / q, q) for w, q in zip(wage, quality)])
        hq, s = [], 0
        for i in range(k):
            heappush(hq, -nums[i][1])
            s += nums[i][1]
        res = nums[k - 1][0] * s 
        for i in range(k, n):
            mxw = -heappop(hq)
            s -= mxw 
            mxw = min(mxw, nums[i][1])
            heappush(hq, -mxw)
            s += mxw 
            res = min(res, nums[i][0] * s)
        return res
```

****

[2589. 完成所有任务的最少时间 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-time-to-complete-all-tasks/description/?envType=daily-question&envId=2024-05-15)

**区间选点问题：选点数量可能超过1 + 右端点排序贪心**

为什么不能按照左端点排序？

如果按照左端点排序：

- 当下一个区间比当前区间先结束时，选点会在当前区间中间；
- 当下一个区间前缀和当前区间后缀相交时，选点在当前区间的尾部。

两者无法统一。

考虑按照**右端点排序 / 结束时间排序：**

- 当下一个区间比当前区间先开始，选点可以在当前区间的尾部。
- 当下一个区间前缀和当前区间后缀相交时，选点也可以在区间的尾部。

因此二者是统一的。

从前向后考虑区间，当前区间，我们希望当前区间的后缀去匹配更多的后续区间的前缀，因此选点应该越靠后越好，即在当前区间的尾部。当相邻区间不相交时，选点是当前区间独占的。

因此，使用 $sel$ 维护选择的点，每次进入新区间，首先考察范围内已经选择的点的个数；剩余的点需要贪心的安排在尾部。

时间复杂度：$O(n \log n + n U)$, $U$ 为最大结束时间。

```python
    def findMinimumTime(self, nums: List[List[int]]) -> int:
        nums.sort(key = lambda x: x[1])
        n, m = len(nums), nums[-1][1]
        sel = [0] * (m + 1)
        for l, r, c in nums:
            c -= sum(sel[l: r + 1])
            if c > 0:
                for i in range(r, l - 1, -1):
                    if sel[i]: continue 
                    sel[i] = 1
                    c -= 1
                    if c == 0: break 
        return sum(sel)
```



## 反悔贪心

### 1.反悔堆

- 贪心：尽可能
- 反悔堆
- 反悔条件：不满足原条件

[630. 课程表 III - 力扣（LeetCode）](https://leetcode.cn/problems/course-schedule-iii/description/?envType=featured-list&envId=1DMi3d2m?envType=featured-list&envId=1DMi3d2m)

反悔贪心：按照截止日期排序，尽可能不跳过每一个课程。反悔条件（cur > y）满足时从反悔堆反悔用时最大的课程。

```python
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # 按照截至日期排序
        courses.sort(key = lambda x: x[1])
        hq = []
        res, cur = 0, 0 
        for x, y in courses:
            cur += x    # 贪心：尽可能不跳过每一个课程
            heapq.heappush(hq, -x)  # 反悔堆：存放所有课程耗时
            if cur > y: # 反悔条件：超过截止日期
                cur += heapq.heappop(hq)
            else:
                res += 1
        return res
```

[LCP 30. 魔塔游戏 - 力扣（LeetCode）](https://leetcode.cn/problems/p0NxJO/?envType=featured-list&envId=1DMi3d2m?envType=featured-list&envId=1DMi3d2m)

```python
    def magicTower(self, nums: List[int]) -> int:
        if sum(nums) + 1<= 0:
            return -1
        hq = []
        res, cur = 0, 1
        for x in nums:
            cur += x    # 贪心：尽可能不使用移动
            if x < 0:   # 反悔堆
                heapq.heappush(hq, x)   
            if cur <= 0:    # 反悔条件：血量不是正值
                res += 1    
                cur -= heapq.heappop(hq) # 从反悔堆中，贪心回复血量
        return res 
```

[1642. 可以到达的最远建筑 - 力扣（LeetCode）](https://leetcode.cn/problems/furthest-building-you-can-reach/?envType=featured-list&envId=1DMi3d2m?envType=featured-list&envId=1DMi3d2m)

```python
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        d = [max(0, heights[i] - heights[i - 1]) for i in range(1, n)]
        hq = []
        for res, x in enumerate(d):
            # ladders - len(hq) 代表剩余梯子数量
            heapq.heappush(hq, x)    # 贪心 + 反悔堆
            if ladders - len(hq) < 0: # 反悔条件：梯子不够了
                bricks -= heapq.heappop(hq) 
            if bricks < 0:
                return res
        return n - 1 
```

[871. 最低加油次数 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-number-of-refueling-stops/description/?envType=featured-list&envId=1DMi3d2m?envType=featured-list&envId=1DMi3d2m)

循环反悔贪心 + 反悔堆后置（需要贪心完成后才能加入当前值）

```python
def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target, 0])
        n = len(stations)
        pre = 0
        res, cur = 0, startFuel 
        hq = []
        for x, y in stations:
            cur -= x - pre #  贪心：尽可能耗油不加油
            pre = x
            while hq and cur < 0: # 反悔条件：剩余油不够了
                res += 1
                cur -= heapq.heappop(hq)
            if cur < 0 and not hq:
                return -1
            heapq.heappush(hq, -y)   # 反悔堆：保存没加的油
        return res
```

### 2. 尝试反悔 + 反悔栈

也是一个二维贪心问题。尽可能优先考虑利润维度。

[2813. 子序列最大优雅度 - 力扣（LeetCode）](https://leetcode.cn/problems/maximum-elegance-of-a-k-length-subsequence/?envType=featured-list&envId=1DMi3d2m?envType=featured-list&envId=1DMi3d2m)

```python
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        items.sort(reverse = True)
        s = set()   # 只出现一次的种类 c
        stk = []     # 反悔栈：出现两次以上的利润 p
        res = total_profit = 0
        for i, (p, c) in enumerate(items):
            if i < k:
                total_profit += p 
                if c not in s:      # 种类c首次出现, 对应p一定最大, 一定保留
                    s.add(c)	
                else:
                    stk.append(p)    # 反悔栈：存放第二次及以后出现的更小的p
            elif stk and c not in s:
                # 只有c没有出现在s中时，才尝试反悔一个出现两次及以上的p
                total_profit += p - stk.pop() 			
                s.add(c)		
                # 贪心：s的长度只增不减
            res = max(res, total_profit + len(s) ** 2)
        return res
```

## 消消乐贪心

配合哈希表 / 哈希集合，在 $O(n)$ 复杂度内，通过对乱序枚举到的每一个 $x$ ，贪心找出符合性质 / 限制的整组数据并且消除。

**最长连续子序列**

[最长连续序列](https://leetcode.cn/problems/longest-consecutive-sequence/)

给定一个未排序的整数数组 `nums` ，找出数字连续的最长子序列。

对于任何一个数 $x$ ，向两边贪心找到相邻的这一组数，将其消除。

```python
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for x in nums:
            if x not in s: continue
            cur = 1
            s.remove(x)
            y = x + 1
            while y in s:
                s.remove(y)
                cur, y = cur + 1, y + 1
            y = x - 1
            while y in s:
                s.remove(y)
                cur, y = cur + 1, y - 1
            res = max(res, cur)
        return res
```

[2007. 从双倍数组中还原原数组 - 力扣（LeetCode）](https://leetcode.cn/problems/find-original-array-from-doubled-array/description/)

对于任何一个数 $x$ ，如果是奇数则是最小出发数；否则向下贪心折半，直到得到最小出发数（奇数或者最小可达的偶数）。从最小出发数，出发，贪心删除整组数据。时间复杂度：$O(n)$

```python
def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n & 1: return []
        res = []
        cnt = Counter(changed)
        for i, x in enumerate(changed):
            if cnt[x] == 0: continue
            if x == 0:
                if cnt[0] & 1: return []
                res.extend(cnt[0] //2 * [0])
                cnt[0] = 0
                continue 
            while x & 1 == 0 and cnt[x // 2] > 0: x //= 2
            y = x 
            while cnt[y] > 0:
                if cnt[y * 2] < cnt[y]: return []
                res.extend(cnt[y] * [y])
                cnt[y * 2] -= cnt[y]
                cnt[y] = 0
                if cnt[y * 2]: y = 2 * y
                else: y = 4 * y
        return res
```

## 贪心集合划分

**划分集合和不超过 $k$ 的最少划分数：排序+回溯贪心**

[1986. 完成任务的最少工作时间段 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-number-of-work-sessions-to-finish-the-tasks/description/?envType=featured-list&envId=ptud3zoQ?envType=featured-list&envId=ptud3zoQ)

一种做法是$O(3^n+n\cdot 2^n)$ 的状压dp，实际上可以给出 最坏情况下 $O(2^n)$做法。

**首先按照从到大小排序。**对于$a[i]$，选择1：分配到新的组中；选择2：分配到已经存在的、不超载的组。最坏情况下不超过 $O(2^n)$，实际上由于剪枝操作，接近于线性复杂度。

```python
    def minSessions(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        n = len(nums)
        cnt = [0] * n 
        res = inf
        def dfs(i, cur):
            nonlocal res 
            if cur >= res: return 
            if i == n: 
                res = cur 
                return 
            x = nums[i]
            for j in range(cur):
                if cnt[j] + x <= k:
                    cnt[j] += x
                    dfs(i + 1, cur)
                    cnt[j] -= x
            cnt[cur] += x 
            dfs(i + 1, cur + 1)
            cnt[cur] -= x
        dfs(0, 0)
        return res
            
```

**划分集合和不超过 $k$ 的最少划分数：集合长度不超过2**

排序 + 双指针贪心。

[881. 救生艇 - 力扣（LeetCode）](https://leetcode.cn/problems/boats-to-save-people/description/)

```python
    def numRescueBoats(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        n = len(nums)
        i, j = 0, n - 1
        res = 0
        while i <= j:
            lft = k - nums[i]
            i += 1
            if lft >= nums[j]:
                j -= 1
            res += 1
        return res
```





# 贡献法

经典问题：**子数组的最小值之和，子数组的最大值之和，子数组的极差之和。**

1. 套娃式定义，如子数组的子数组，子序列的子序列
2. 求某些的和，可以考虑成子子问题对总问题的贡献

[2104. 子数组范围和 - 力扣（LeetCode）](https://leetcode.cn/problems/sum-of-subarray-ranges/description/?envType=featured-list&envId=ZZi8gf6w?envType=featured-list&envId=ZZi8gf6w)

考虑每个值对子数组最大值，最小值的贡献情况，用单调栈维护。

最大值用减小栈维护，贡献是$(i - t) \times (t - stk[-1]) \times nums[t]$

```python
    def subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        stk = [-1]
        total_mx = 0	# 贡献
        nums.append(inf)
        for i, x in enumerate(nums):
            # 单调减
            while len(stk) > 1 and x >= nums[stk[-1]]:
                t = stk.pop()
                total_mx += (i - t) * (t - stk[-1]) * nums[t]
            stk.append(i)
        stk = [-1]
        nums[-1] = -inf
        total_mn = 0
        for i, x in enumerate(nums):
            # 单调增
            while len(stk) > 1 and x <= nums[stk[-1]]:
                t = stk.pop()
                total_mn += (i - t) * (t - stk[-1]) * nums[t]
            stk.append(i)
        return total_mx - total_mn
```



# 计算几何

## 旋转与向量

将点 $(x, ~y)$ 顺时针旋转 $\alpha$ 后，新的点坐标为 $(x \cos \alpha+y\sin\alpha,~~~ y \cos \alpha~ - x\sin\alpha  )$

证明：
$$
点P(x, y) 表示为 半径为 r，极角为 \theta的坐标系下，
\begin{cases}
x = r \cos \theta
\\
y = r \sin \theta
\end{cases}
\\
顺时针旋转 \alpha 后，\begin{cases}
x' = r \cos (\theta - \alpha) = x \cos \alpha + y \sin \alpha
\\
y' = r \sin (\theta - \alpha) = y \cos \alpha - x \sin \alpha
\end{cases}
\\
$$


## 距离

$A(x_1, ~y_1),~ B(x_2, ~y_2)$

曼哈顿距离$ = |x_1 - x_2| + |y_1 - y_2|$

切比雪夫距离$ = \max(|x_1 - x_2| ,~ |y_1 - y_2|)$

### 曼哈顿距离转切比雪夫

即将所有点顺时针旋转45°后再乘 $\sqrt{2}$。
$$
将P(x,~y)映射到 ~ P'(x+y,~x-y)坐标系下，d_{M} = d'_Q \\
对于三维点 P(x,y,z) 映射到 P''(x+y+z, ~-x+y+z, ~x-y+z, ~x + y -z)坐标系下, d_M = d''_Q
$$


当需要求若干点之间的最大 $d_M$ 时，可以转换为
$$
\forall {i, j} \in P, \max(|x_i - x_j| + |y_i - y_j|) \iff \max(~\max(|x'_i - x'_j|, ~ |y'_i - y'_j|)~) \\
\iff \forall {i, j} \in P , ~ \max(\max(|x'_i - x'_j|), ~\max(|y'_i - y'_j|))
$$

[3102. 最小化曼哈顿距离 - 力扣（LeetCode）](https://leetcode.cn/problems/minimize-manhattan-distances/description/)

```python
from sortedcontainers import SortedList
class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        msx, msy = SortedList(), SortedList()
        for x, y in points:
            msx.add(x + y)
            msy.add(x - y)
        res = inf 
        for x, y in points:
            msx.remove(x + y)
            msy.remove(x - y)
            xmx = msx[-1] - msx[0]
            ymx = msy[-1] - msy[0]
            res = min(res, max(xmx, ymx))
            msx.add(x + y)
            msy.add(x - y)
        return res            
```



### 切比雪夫转曼哈顿距离

$$
将 P(x, y) 映射到 P'(\frac{x + y}{2}, \frac{x-y}{2}) 坐标系下， d_Q = d'_M
$$

切比雪夫距离在计算的时候需要取max，往往不是很好优化，对于一个点，计算其他点到该的距离的复杂度为O(n)

而曼哈顿距离只有求和以及取绝对值两种运算，我们把坐标排序后可以去掉绝对值的影响，进而用前缀和优化，可以把复杂度降为O(1)

[P3964 [TJOI2013\] 松鼠聚会 - 洛谷 | 计算机科学教育新生态 (luogu.com.cn)](https://www.luogu.com.cn/problem/P3964)

转换成切比雪夫距离。将x, y 分离，前缀和维护到各个xi 和 yi 的距离和，再相加

```python
def solve():
    n = int(input())
    points = []
    res = inf
    for _ in range(n):
        x, y = map(int, input().split())
        points.append(((x + y) / 2, (x - y) / 2))
    numsx = [p[0] for p in points]
    numsy = [p[1] for p in points]
    def g(nums):
        nums.sort()
        curx = nums[0]
        curd = sum(nums[i] - curx for i in range(1, n))
        dic = {nums[0]: curd}
        for i in range(1, n):
            x = nums[i]
            d = x - curx
            curd = curd + i * d - (n - i) * d
            dic[x] = curd
            curx = x
        return dic
    dicx, dicy = g(numsx), g(numsy)
    for x, y in points:
        ans = dicx[x] + dicy[y]
        res = min(res, ans)
    print(int(res))
```

# 杂项问题

**$ceil$ 精度处理**

同时存在除法和 $ceil$ 运算时， $ceil(a /b)$ 以及 $ceil(a/b +x)$ 操作会由于精度问题，导致偏差。

方法1：$ceil(x) = math.ceil(x - eps)$，其中 $eps $ 是小常量，如$10^{-8}$

方法2：所有数乘 $b$ ，其中 $b \times ceil(a,b) = ((a-1)//b + 1) \times b$ ，例如 $ ceil(4,3) \times3=2\times 3=6$。

[1883. 准时抵达会议现场的最小跳过休息次数 - 力扣（LeetCode）](https://leetcode.cn/problems/minimum-skips-to-arrive-at-meeting-on-time/description/?envType=daily-question&envId=2024-04-19)

$ f(i, j) =\min \{f(i - 1, j - 1) + d[i]/s,~ ceil(f(i - 1, j) + d[i]/s)\}$

方法1：

```python
    eps = 1e-8
    def ceil(x):
        return math.ceil(x - eps)
    
	def minSkips(self, d: List[int], s: int, hoursBefore: int) -> int:
        n = len(d)
        if sum(d) > s * hoursBefore: return -1
        if n == 1: return 0 if d[0] <= s * hoursBefore else -1
        mx = sum(d) + n
        f = [[mx] * (n + 1) for _ in range(n + 1)]
        
        d = [D / s for D in d]
        f[0][0] = ceil(d[0])
        f[0][1] = d[0] 
        for i in range(1, n - 1):
            for j in range(i + 2):
                f[i][j] = ceil(f[i - 1][j] + d[i])   # 不休息
                if j: f[i][j] = min(f[i][j], f[i - 1][j - 1] + d[i])    # 休息
        for k in range(n):
            if f[n - 2][k] + d[-1] <= hoursBefore:
                return k
```

方法2：

```python
    def ceil(a, b):
        return ((a - 1) // b + 1) * b

    def minSkips(self, d: List[int], s: int, hoursBefore: int) -> int:
        n = len(d)
        if sum(d) > s * hoursBefore: return -1
        if n == 1: return 0 if d[0] <= s * hoursBefore else -1
        mx = sum(d) + n
        f = [[mx] * (n + 1) for _ in range(n + 1)]
        
        f[0][0] = ceil(d[0], s)
        f[0][1] = d[0]
        for i in range(1, n - 1):
            for j in range(i + 2):
                f[i][j] = ceil(f[i - 1][j] + d[i], s)
                if j: f[i][j] = min(f[i][j], f[i - 1][j - 1] + d[i])
        for k in range(n):
            if f[n - 2][k] + d[-1] <= hoursBefore * s:
                return k
```







[灵茶の试炼 (qq.com)](https://docs.qq.com/sheet/DWGFoRGVZRmxNaXFz?tab=BB08J2)	
