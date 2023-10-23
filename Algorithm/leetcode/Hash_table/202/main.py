'''
Author: gledfish
Date: 2023-10-22 16:12:29
LastEditTime: 2023-10-22 16:23:40
FilePath: \leetcode\Hash_table\202\main.py
Description: 
'''
# class Solution:
#     def isHappy(self, n: int) -> bool:
#         """使用哈希表
#            缺点:何时出现循环未知，可能导致空间复杂度极大

#         Args:
#             n (int): _description_

#         Returns:
#             bool: _description_
#         """
#         record = set() # 存储和
#         while True:
#             n = self.get_sum(n)
#             if n == 1:
#                 return True
#         # 如果中间结果重复出现，说明陷入死循环了，该数不是快乐数
#             if n in record:
#                 return False
#             else:
#                 record.add(n)
#     def get_sum(self,n: int) -> int: 
#         new_num = 0
#         while n:
#             n, r = divmod(n, 10)
#             new_num += r ** 2
#         return new_num

class Solution:
    def isHappy(self, n: int) -> bool:
        """双指针

        Args:
            n (int): _description_

        Returns:
            bool: _description_
        """
        slow = quick = n
        while True:
            slow = self.get_sum(slow)
            quick = self.get_sum(quick)
            quick =self.get_sum(quick)
            if slow != quick:
                continue
            else:
                break
        return slow == 1
    def get_sum(self,n: int) -> int: 
        new_num = 0
        while n:
            n, r = divmod(n, 10)
            new_num += r ** 2
        return new_num
if __name__ == "__main__":
    # n = 19
    n = 2
    solution = Solution()
    print(solution.isHappy(n))