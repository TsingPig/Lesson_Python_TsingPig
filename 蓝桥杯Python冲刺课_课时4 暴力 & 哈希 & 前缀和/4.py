n = 10 ** 10
lst = [i ** 2 for i in range(n)]

lst.pop(0) # O(n)  
lst.pop()
from collections import deque
q = deque(lst)
q.popleft() # O(1) 
