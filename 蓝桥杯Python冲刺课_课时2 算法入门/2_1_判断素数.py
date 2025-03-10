from math import sqrt
# sqrt(x) 返回x的开平方的浮点值
# int(sqrt(x))  sqrt(11) = 3
def is_prime(n):
    if n < 2: return False
    # 24
    # 2 * 12
    # 3 * 8
    # ...
    # 8 * 3
    for i in range(2, int(sqrt(n)) + 1):  # [2, int(sqrt(n)) ]
        if n % i == 0: 
            return False
    return True

print(is_prime(2))  # True 1, 2 最小的素数
print(is_prime(11)) # True 1, 11
print(is_prime(91)) # False   13 * 7

    
