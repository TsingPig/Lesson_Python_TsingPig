from datetime import *

# 计算日期之差
t1 = date(year = 2025, month = 3, day= 1)
t2 = date(year = 2025, month = 3, day = 17)

print(t2 - t1) # 16 days, 0:00:00
print((t2 - t1).days) # 16

# 参数也可简化
t1 = date(2025, 1, 1)
t2 = date(2025, 3, 17)
print((t2 - t1).days) # 75

# 获取当前日期
print(date.today()) # 2025-03-17


t1 = date(2025, 3, 17)
print(t1 + timedelta(days = 2)) # 2025-03-19
print(t1 + timedelta(1)) # 2025-03-18
print(t1.weekday()) # 0，weekday()从0~6对应星期1~7
