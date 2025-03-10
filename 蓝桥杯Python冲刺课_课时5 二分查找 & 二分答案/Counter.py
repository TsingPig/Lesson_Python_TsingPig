from collections import Counter

list1 = ["a", "a", "a", "b", "c", "c", "f", "g", "g", "g", "f"]
dic = Counter(list1)
print(dic)
#Counter({'a': 3, 'g': 3, 'c': 2, 'f': 2, 'b': 1})

list1 = ["a", "a", "a", "b", "c", "f", "g", "g", "c", "11", "g", "f", "10", "2"]
print(Counter(list1).most_common(3))
#结果：[('a', 3), ('g', 3), ('c', 2)]



list1 = ["a", "a", "a", "b", "c", "f", "g", "g", "c", "11", "g", "f", "10", "2"]
print(Counter(list1).most_common(1))
#结果：[('a', 3)]
