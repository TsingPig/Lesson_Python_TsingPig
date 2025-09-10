# from collections import Counter
#
# list1 = ["a", "a", "a", "b", "c", "c", "f", "g", "g", "g", "f"]
# dic = Counter(list1)
# print(dic)
# #Counter({'a': 3, 'g': 3, 'c': 2, 'f': 2, 'b': 1})
#
# list1 = ["a", "a", "a", "b", "c", "f", "g", "g", "c", "11", "g", "f", "10", "2"]
# print(Counter(list1).most_common(3))
# #结果：[('a', 3), ('g', 3), ('c', 2)]
#
#
#
# list1 = ["a", "a", "a", "b", "c", "f", "g", "g", "c", "11", "g", "f", "10", "2"]
# print(Counter(list1).most_common(1))
# #结果：[('a', 3)]
#


s = [1, 2, 3, 4, 5]
# 位运算
sbit = 0
for i in s:
    sbit |= 1 << i
print(sbit, bin(sbit))
for i in range(1, 1 << len(s)):
    if (sbit >> i) & 1:
        print(i)




n = int(input())
lst = [int(input()) for _ in range(n)]
print(lst)