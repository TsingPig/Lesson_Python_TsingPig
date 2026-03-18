'''
标识符

第一个字符必须是字母表中字母或下划线 _ 。
标识符的其他的部分由字母、数字和下划线组成。
标识符对大小写敏感。
在 Python 3 中，可以用中文作为变量名，非 ASCII 标识符也是允许的了。

'''

        # 常见变量命名
        # res/ans 答案、结果
        # cnt/tot 用于计数
        # i, idx 表示 索引
        # x, y, z... 表示元素遍历
        # a, b, c... 变量
        # s 字符串变量
        # nums 数组
        # q 队列， d字典， k,v 键值对变量
        # l, r = left, right





# python保留字
# 保留字即关键字，我们不能把它们用作任何标识符名称。
['False', 'None', 'True', 'and', 'as',
'assert', 'break', 'class', 'continue',
'def', 'del', 'elif', 'else',
'except', 'finally', 'for', 'from',
 'global', 'if', 'import',
 'in', 'is', 'lambda', 'nonlocal',
 'not', 'or', 'pass', 'raise',
 'return', 'try', 'while', 'with', 'yield']




# 字符串
'''
Python 中单引号 ' 和双引号 " 使用完全相同。
使用三引号可以指定一个多行字符串。
转义符 \。
反斜杠可以用来转义，使用 r 可以让反斜杠不发生转义。
如 r"this is a line with \n" 则 \n 会显示，并不是换行。

字符串可以用 + 运算符连接在一起，用 * 运算符重复。
Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
Python 中的字符串不能改变。
字符串切片 str[start:end]，其中 start（包含）是切片开始的索引，
end（不包含）是切片结束的索引。
字符串的切片可以加上步长参数 step，语法格式如下：str[start:end:step]
'''


s = '123456789'

print(s)  # 输出字符串
# 输出: 123456789
print(s[0:-1])  # 输出第一个到倒数第二个的所有字符
# 输出: 12345678
print(s[0])  # 输出字符串第一个字符
# 输出: 1
print(s[2:5])  # 输出从第三个开始到第六个的字符（不包含）
# 输出: 345
print(s[2:])  # 输出从第三个开始后的所有字符
# 输出: 3456789
print(s[1:5:2])  # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
# 输出: 24
print(s * 2)  # 输出字符串两次
# 输出: 123456789123456789
print(s + '你好')  # 连接字符串
# 输出: 123456789你好




# Python 模块导入 (import)
'''
在 Python 中，使用 `import` 或 `from...import` 语句可以导入模块或模块中的特定功能。

1. 导入整个模块：
   格式：`import somemodule`
   示例：`import math`

2. 为模块设置别名：
   格式：`import somemodule as alias`
   示例：`import numpy as np`

3. 从模块中导入某个函数：
   格式：`from somemodule import somefunction`
   示例：`from math import sqrt`

4. 从模块中导入多个函数：
   格式：`from somemodule import firstfunc, secondfunc, thirdfunc`
   示例：`from math import sqrt, sin, cos`

5. 导入模块中的所有函数：
   格式：`from somemodule import *`
   示例：`from math import *`
   注意：这种方式会导入模块中的所有内容，可能会导致命名冲突，不推荐在大型项目中使用。

6. 导入模块中的特定成员（如变量、函数等）：
   格式：`from somemodule import member1, member2`
   示例：`from sys import argv, path`
'''

# 示例代码
import sys

# 使用 sys.stdin 读取输入并去除换行符
input = lambda: sys.stdin.readline().strip()



# Python 输出 (print) - 算法竞赛专用
'''
在算法竞赛中，`print` 是常用的输出函数。以下是 `print` 的高效用法和技巧，帮助你在竞赛中快速输出结果。

1. 基本用法：
   格式：`print(value)`
   示例：`print("Hello, World!")`

2. 输出多个值：
   格式：`print(value1, value2, ...)`
   示例：`print("Name:", "Alice", "Age:", 25)`

3. 自定义分隔符：
   使用 `sep` 参数指定多个值之间的分隔符。
   格式：`print(value1, value2, ..., sep='separator')`
   示例：`print(2023, 10, 5, sep='-')`  # 输出：2023-10-05

4. 自定义结束符：
   使用 `end` 参数指定输出结束时的字符（默认为换行符 `\n`）。
   格式：`print(value, end='ending')`
   示例：`print("Hello", end=' ')`  # 输出后不换行，接一个空格

5. 格式化输出：
   - 使用 `f-string`（推荐）：
     格式：`print(f"{variable}")`
     示例：`name = "Alice"; print(f"Hello, {name}!")`  # 输出：Hello, Alice!
   - 使用 `format` 方法：
     格式：`print("{}".format(variable))`
     示例：`print("Hello, {}!".format("Alice"))`  # 输出：Hello, Alice!
   - 使用 `%` 格式化（旧版）：
     格式：`print("%s" % variable)`
     示例：`print("Hello, %s!" % "Alice")`  # 输出：Hello, Alice!

6. 高效输出：
   - 使用 `print(*list)` 快速输出列表内容：
     示例：`lst = [1, 2, 3]; print(*lst)`  # 输出：1 2 3
   - 使用 `sep` 和 `end` 控制输出格式：
     示例：`print(1, 2, 3, sep=',', end='!')`  # 输出：1,2,3!
'''

# 示例代码
# 基本用法
print("Hello, World!")

# 输出多个值
print("Name:", "Alice", "Age:", 25)

# 自定义分隔符
print(2023, 10, 5, sep='-')  # 输出：2023-10-05

# 自定义结束符
print("Hello", end=' ')
print("World!")  # 输出：Hello World!

# 格式化输出
name = "Alice"
print(f"Hello, {name}!")  # 输出：Hello, Alice!
print("Hello, {}!".format(name))  # 输出：Hello, Alice!
print("Hello, %s!" % name)  # 输出：Hello, Alice!

# 高效输出
lst = [1, 2, 3]
print(*lst)  # 输出：1 2 3
print(1, 2, 3, sep=',', end='!')  # 输出：1,2,3!



# Python 数据类型 - 算法竞赛专用
'''
Python 常用数据类型及其特性：
1. 整数 (int)：支持大整数运算，如 `a = 10**100`
2. 浮点数 (float)：注意精度问题，如 `b = 3.14`
3. 字符串 (str)：不可变序列，支持切片和格式化，如 `s = "Hello"`
4. 列表 (list)：可变序列，支持增删改查，如 `lst = [1, 2, 3]`
5. 元组 (tuple)：不可变序列，如 `tup = (1, 2, 3)`
6. 集合 (set)：无序不重复，支持集合运算，如 `s = {1, 2, 3}`
7. 字典 (dict)：键值对映射，如 `d = {"key": "value"}`
'''

# 示例代码


# 字符串
s = "Hello"
print(s[1:3])  # 切片：输出 "el"
print(f"{s}, World!")  # 格式化输出

# 列表
lst = [1, 2, 3]
lst.append(4)  # 添加元素
print(lst)  # 输出：[1, 2, 3, 4]

# 元组
tup = (1, 2, 3)
print(tup[0])  # 输出：1

# 集合
s = {1, 2, 3}
s.add(4)  # 添加元素
print(s)  # 输出：{1, 2, 3, 4}

# 字典
d = {"key": "value"}
d["new_key"] = "new_value"  # 添加键值对
print(d)  # 输出：{"key": "value", "new_key": "new_value"}

# Python 函数 - 算法竞赛专用
'''
Python 函数定义与使用：
1. 定义函数：`def func_name(args):`
2. 返回值：`return value`
3. 默认参数：`def func(a, b=10):`
4. 可变参数：`def func(*args):` 或 `def func(**kwargs):`
5. Lambda 函数：`lambda args: expression`
'''

# 示例代码
# 定义函数
def add(a, b):
    return a + b
print(add(1, 2))  # 输出：3

# 默认参数
def power(x, n=2):
    return x**n
print(power(3))  # 输出：9

# 可变参数
def sum_all(*args):
    return sum(args)
print(sum_all(1, 2, 3))  # 输出：6

# 关键字参数
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Alice", age=25)  # 输出：name: Alice, age: 25

'''
Lambda表达式是一种匿名函数，也称为内联函数。
它是一种Python的小型匿名函数，可以接受任意数量的参数，
但只能有一个表达式。Lambda函数不能包含多个语句。
用于编写简短的函数，而不需要定义函数名称。
基本语法：
lambda 参数: 表达式
'''
x = lambda a: a + 10
print(x(5))  # 输出: 15
'''
这里，lambda是Python的关键字，用于定义Lambda函数。参数是参数列表，
可以包含零个或多个参数，但必须在冒号（:）前指定。
表达式是一个用于计算并返回函数结果的表达式。
例如，创建一个Lambda函数，它接受一个参数并返回该参数加10的结果：
'''

# 获得中位数
get_mid = lambda nums: nums[len(nums) // 2]
print(get_mid([1, 4, 5]))

'''
【保研岛】蓝桥杯Python辅导课：课时1_Sort排序
'''

'''
sorted() 函数
Python内置的 sorted() 函数可以对任何可迭代对象进行排序，返回一个新的排序后的列表。
基本语法：
sorted(iterable, key=None, reverse=False)
iterable：需要排序的可迭代对象
key：排序规则，可以传入一个函数，指定排序依据（如按元素的某个属性排序）
reverse：是否反向排序，默认为 False，表示升序排序
'''

# 按照默认升序排序
nums = [5, 3, 8, 6, 7]
print(sorted(nums))  # 输出: [3, 5, 6, 7, 8]

# 降序排序
print(sorted(nums, reverse = True))  # 输出: [8, 7, 6, 5, 3]

# 按照字符串长度排序
words = ["apple", "banana", "kiwi", "cherry"]
print(sorted(words, key = len))  # 输出: ['kiwi', 'apple', 'cherry', 'banana']

'''
列表的 sort() 方法
sort() 是列表对象的一个方法，它会原地修改列表，直接排序，不返回新的列表。
list.sort(key=None, reverse=False)
key：排序规则，类似 sorted() 的 key
reverse：是否反向排序，默认为 False
'''
nums = [5, 3, 8, 6, 7]
nums.sort()  # 原地升序排序
print(nums)  # 输出: [3, 5, 6, 7, 8]

words = ["apple", "banana", "kiwi", "cherry"]
words.sort(key = len)  # 按照字符串长度排序
print(words)  # 输出: ['kiwi', 'apple', 'cherry', 'banana']

'''
使用 Lambda 表达式与排序
有时我们需要更加灵活的排序方式，可以使用 lambda 表达式作为 key 参数来指定排序规则。
'''
# 按照第二个字符排序
words = ["apple", "banana", "kiwi", "cherry"]
sorted_words = sorted(words, key = lambda x: x[1])
print(sorted_words)  # 输出: ['banana', 'cherry', 'kiwi', 'apple']

# 5. 处理常见输入格式
# 示例 1：单行多个整数
a, b, c = map(int, input().split())  # 输入：1 2 3
print(a, b, c)  # 输出：1 2 3

# 示例 2：多行多个整数
n = int(input())  # 输入行数
lst = [int(input()) for _ in range(n)]  # 读取 n 行整数
print(lst)

# 示例 3：矩阵输入
n, m = map(int, input().split())  # 输入矩阵大小
matrix = [list(map(int, input().split())) for _ in range(n)]  # 读取 n 行 m 列的矩阵
print(matrix)
