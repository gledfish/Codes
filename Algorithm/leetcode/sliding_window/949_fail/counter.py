'''
Author: gledfish
Date: 2023-10-20 20:35:09
LastEditTime: 2023-10-20 20:36:50
FilePath: \leetcode\sliding_window\949_fail\counter.py
Description: 
'''
from collections import Counter

# 创建一个Counter对象
my_counter = Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])

# 获取元素的频率
print(my_counter['apple'])  # 输出：3
print(my_counter['banana'])  # 输出：2
print(my_counter['orange'])  # 输出：1

# 获取所有元素的频率统计
print(my_counter)  # 输出：Counter({'apple': 3, 'banana': 2, 'orange': 1})

# 获取出现次数最多的元素
most_common = my_counter.most_common(1)
print(most_common)  # 输出：[('apple', 3)]

# 更新计数器
my_counter.update(['apple', 'banana', 'kiwi'])
print(my_counter)  # 输出：Counter({'apple': 4, 'banana': 3, 'orange': 1,'kiwi': 1})

# 删除元素的计数
del my_counter['banana']
print(my_counter)  # 输出：Counter({'apple': 4, 'kiwi': 1})

# 清空计数器
my_counter.clear()
print(my_counter)  # 输出：Counter()