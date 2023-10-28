'''
Author: gledfish
Date: 2023-10-26 15:57:53
LastEditTime: 2023-10-26 16:12:15
FilePath: \leetcode\practices\2520\main.py
Description: 
'''
# 给你一个整数 num ，返回 num 中能整除 num 的数位的数目。

# 如果满足 nums % val == 0 ，则认为整数 val 可以整除 nums 。


# class Solution:
#     def countDigits(self, num: int) -> int:
#         """转为字符串

#         Args:
#             num (int): _description_

#         Returns:
#             int: _description_
#         """
#         my_sum = 0
#         num_str = str(num)
#         for char in num_str:
#             if num % int(char) == 0:
#                 my_sum += 1
#         return my_sum

class Solution:
    def countDigits(self, num: int) -> int:
        my_sum = 0
        my_num = num 
        while num > 0:
            temp = num % 10
            num = num // 10
            if my_num % temp == 0:
                 my_sum += 1
                 
        return my_sum 
if __name__ == "__main__":
    # num = 7
    # num = 121
    num = 1248
    
    solution = Solution()
    print(solution.countDigits(num))