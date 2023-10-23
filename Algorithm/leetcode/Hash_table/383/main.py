'''
Author: gledfish
Date: 2023-10-23 20:37:21
LastEditTime: 2023-10-23 20:43:40
FilePath: \leetcode\Hash_table\383\main.py
Description: 
'''

# class Solution:
#     def canConstruct(self, ransomNote: str, magazine: str) -> bool:
#         """哈希表O(n^2)

#         Args:
#             ransomNote (str): _description_
#             magazine (str): _description_

#         Returns:
#             bool: _description_
#         """
#         # 将magazine加入字典
#         mag_dict = {}
#         for char in magazine:
#             if char in mag_dict:
#                 mag_dict[char] += 1
#             else:
#                 mag_dict[char] = 1
#         # 查看ransomNote是否在magazine
#         for char in ransomNote:
#             if char in mag_dict:
#                 mag_dict[char] -= 1
#                 if mag_dict[char] == 0:
#                     del mag_dict[char]
#             else:
#                 return False 
#         return True 
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = [0] * 26
        magazine_count = [0] * 26
        for c in ransomNote:
            ransom_count[ord(c) - ord('a')] += 1
        for c in magazine:
            magazine_count[ord(c) - ord('a')] += 1
        return all(ransom_count[i] <= magazine_count[i] for i in range(26))

if __name__ == "__main__":
    # ransomNote = "a"
    # magazine = "b"
    
    ransomNote = "aa"
    magazine = "ab"
    
    ransomNote = "aa"
    magazine = "aab"
    solution = Solution()
    print(solution.canConstruct(ransomNote,magazine))
    
    
# all函数是Python内置函数之一，用于判断可迭代对象中的所有元素是否都为真（即非零、非空、非None等）。

# 函数签名：

# python
# Copy
# all(iterable)
# 参数：

# iterable：要检查的可迭代对象，可以是列表、元组、集合、字典等。
# 返回值：

# 如果可迭代对象中的所有元素都为真，则返回True。
# 如果可迭代对象中存在至少一个元素为假，则返回False。
# all函数的工作方式如下：

# 对于空的可迭代对象，例如空列表或空元组，它会直接返回True。
# 对于非空的可迭代对象，它会依次遍历对象中的元素，并在遇到第一个为假的元素时立即返回False。
# 如果遍历完整个可迭代对象，没有遇到任何为假的元素，则返回True。
# 以下是一些示例，演示了all函数的使用：

# python
# Copy
# # 列表中的所有元素都为真
# print(all([True, True, True]))  # 输出: True

# # 列表中存在一个为假的元素
# print(all([True, False, True]))  # 输出: False

# # 空列表
# print(all([]))  # 输出: True

# # 元组中的所有元素都为真
# print(all((1, 2, 3)))  # 输出: True

# # 字典的键默认判断为真
# print(all({'a': 1, 'b': 2}))  # 输出: True

# # 字典的值存在一个为假的情况
# print(all({'a': 1, 'b': 0}))  # 输出: False
# 总结起来，all函数用于判断可迭代对象中的所有元素是否都为真，提供了一种方便的方式来进行条件判断。