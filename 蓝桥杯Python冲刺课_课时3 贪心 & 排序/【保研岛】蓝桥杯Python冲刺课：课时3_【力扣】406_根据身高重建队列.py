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