
# ==================================================
# 语法进阶：列表推导器
# ==================================================

'''
列表推导器（List Comprehension）是Python中一种简洁且高效的方式，用于创建列表。
它的语法比传统的 for 循环更简洁，代码可读性更高，特别适合在算法竞赛中快速生成数据或进行数据转换。

基本语法：
[expression for item in iterable if condition]
- expression: 表达式，用于生成列表中的元素
- item: 可迭代对象中的每个元素
- iterable: 可迭代对象（如列表、字符串、range等）
- condition: 可选，用于过滤元素的条件
'''

# 示例 1：生成 1 到 10 的平方列表
squares = [i**2 for i in range(1, 11)]
# 输出：[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 示例 2：过滤出 1 到 20 中的偶数
evens = [i for i in range(1, 21) if i % 2 == 0]
# 输出：[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 示例 3：将输入的字符串列表转换为整数列表
# 假设输入为 "1 2 3 4 5"
input_data = list(map(int, input().split()))
# 使用列表推导器实现
input_data = [int(x) for x in input().split()]
# 输出：[1, 2, 3, 4, 5]

# 示例 4：生成一个 n x n 的零矩阵
n = 3
zero_matrix = [[0 for _ in range(n)] for _ in range(n)]
# 输出：[[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# 示例 5：快速生成一个长度为 n 的斐波那契数列
n = 10
fib = [0, 1]
[fib.append(fib[-1] + fib[-2]) for _ in range(n - 2)]
# 输出：[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# 示例 6：将二维列表展平为一维列表
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten = [x for row in matrix for x in row]
# 输出：[1, 2, 3, 4, 5, 6, 7, 8, 9]

# 示例 7：快速统计字符串中每个字符的出现次数
s = "algorithm"
char_count = {char: s.count(char) for char in set(s)}
# 输出：{'a': 1, 'l': 1, 'g': 1, 'o': 1, 'r': 1, 'i': 1, 't': 1, 'h': 1, 'm': 1}



# ==================================================
# 语法进阶：range 函数
# ==================================================

'''
range 是Python中用于生成整数序列的内置函数，在算法竞赛中非常常用。
它可以帮助我们快速生成一系列数字，用于循环、初始化数组等场景。

基本语法：
range(start, stop, step)
- start: 序列的起始值（包含），默认为 0
- stop: 序列的结束值（不包含）
- step: 步长，默认为 1

range 返回的是一个 range 对象，它是一个惰性序列，节省内存。
如果需要列表，可以用 list() 函数将其转换为列表。


注意：range 的 stop 参数是不包含的，因此实际生成的序列是 [start, stop - 1]。
'''

# 示例 1：生成 0 到 9 的序列（基础用法）
seq = range(10)
print(list(seq))  # 输出：[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 示例 2：生成 1 到 10 的奇数序列（步长控制）
seq = range(1, 11, 2)
print(list(seq))  # 输出：[1, 3, 5, 7, 9]

# 示例 3：生成倒序序列（步长为负数）
seq = range(10, 0, -1)
print(list(seq))  # 输出：[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# 示例 4：生成循环的索引（模运算结合）
n = 5
for i in range(n * 2):
    idx = i % n  # 索引循环 0→1→2→3→4→0→1→...
    print(idx, end=" ")  # 输出：0 1 2 3 4 0 1 2 3 4

# 示例 5：生成二维网格坐标（嵌套循环）
rows, cols = 2, 3
grid = [(i, j) for i in range(rows) for j in range(cols)]
print(grid)  # 输出：[(0,0), (0,1), (0,2), (1,0), (1,1), (1,2)]

# 示例 6：生成素数序列（筛选法）
n = 20
is_prime = [True] * (n + 1)
is_prime[0], is_prime[1] = False, False
for i in range(2, int(n**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, n+1, i):
            is_prime[j] = False
primes = [i for i in range(n+1) if is_prime[i]]
print(primes)  # 输出：[2, 3, 5, 7, 11, 13, 17, 19]

# 示例 7：生成前缀和数组（高效初始化）
arr = [3, 1, 4, 1, 5]
prefix = [0] * (len(arr) + 1)
for i in range(len(arr)):
    prefix[i+1] = prefix[i] + arr[i]
print(prefix)  # 输出：[0, 3, 4, 8, 9, 14]

# 示例 8：生成螺旋矩阵（复杂索引控制）
n = 3
matrix = [[0] * n for _ in range(n)]
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
x, y, num, d = 0, 0, 1, 0
for step in range(n, 0, -2):
    for _ in range(4 if step > 1 else 1):
        dx, dy = directions[d]
        for _ in range(step - 1):
            matrix[x][y] = num
            num += 1
            x += dx
            y += dy
        d = (d + 1) % 4
print(matrix)  # 输出：[[1, 2, 3], [8, 9, 4], [7, 6, 5]]

# 课后练习：
# 1. 使用 range 生成一个长度为 n 的杨辉三角（每个元素为组合数）。
# 2. 使用 range 生成一个回文数列表（例如 1 到 100 中的回文数）。



# ==================================================
# 数据结构实战：队列（Queue）与栈（Stack）
# ==================================================

'''
核心语法与操作：
1. 队列（先进先出）：
   - 标准库双端队列（实际使用）：
     from collections import deque
     q = deque()          # 初始化
     q.append(x)          # 从右侧入队
     q.appendleft(x)      # 从左侧入队（特殊场景用）
     x = q.popleft()      # 从左侧出队（时间复杂度 O(1)）
     len(q)               # 获取队列长度

2. 栈（后进先出）：
   - 直接用列表模拟（Pythonic写法）：
     stack = []
     stack.append(x)      # 入栈
     x = stack.pop()      # 出栈（默认弹出最后一个元素，O(1)时间复杂度）
     stack[-1]            # 获取栈顶元素不移除

3. 实用技巧：
   - 快速判断空队列/栈：if not q:  # 判空
   - 栈的翻转：stack[::-1]        # 用切片获取逆序
   - 队列转列表：list(q)          # 将 deque 转换为普通列表
   - 一次性初始化：deque([1,2,3]) # 用迭代器初始化队列

竞赛应用场景：
- 队列：BFS层序遍历、滑动窗口等等
- 栈：DFS路径回溯、括号匹配、单调栈优化
'''
from collections import deque

q = deque()  # 初始化
q.append(x)  # 从右侧入队
q.appendleft(x)  # 从左侧入队（特殊场景用）
x = q.popleft()  # 从左侧出队（时间复杂度 O(1)）
len(q)  # 获取队列长度

stk = []
stk.append(x)  # 入栈
x = stk.pop()  # 出栈（默认弹出最后一个元素，O(1)时间复杂度）
stk[-1]  # 获取栈顶元素不移除


# ==================== 队列实战示例 ====================





# ==================== 栈实战示例 ====================

def eval_rpn(tokens: list[str]) -> int:
    stack = []
    ops = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: int(a / b)  # 关键！向零取整（而非Python默认的向下取整）
    }

    for t in tokens:
        if t in ops:
            b = stack.pop()
            a = stack.pop()
            stack.append(ops[t](a, b))  # 注意操作数顺序：a在前，b在后
        else:
            stack.append(int(t))
    return stack[0]


# ------------------ 测试用例 -------------------
print(eval_rpn(["2", "1", "+", "3", "*"]))  # 输出: 9 → (2+1)*3
print(eval_rpn(["4", "13", "5", "/", "+"]))  # 输出: 6 → 4 + (13/5)
print(eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*"]))  # 输出: -20

# 示例4：嵌套列表解析（栈结构应用）
def decode_string(s):
    stack = []
    num = 0
    res = ""
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == "[":
            stack.append((res, num))  # 同时压入字符串和重复次数
            res, num = "", 0
        elif c == "]":
            prev_str, repeat = stack.pop()
            res = prev_str + repeat * res  # 字符串连接
        else:
            res += c
    return res


# 课后练习：
# 1. 用队列实现栈的 push（入栈）和 pop（出栈）操作
# 2. 设计一个支持 getMin() 的栈，要求所有操作时间复杂度为 O(1)