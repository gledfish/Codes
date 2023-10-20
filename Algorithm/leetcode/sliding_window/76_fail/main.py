# 待重做

'''
Author: gledfish
Date: 2023-10-19 20:12:14
LastEditTime: 2023-10-19 21:22:23
FilePath: \leetcode\sliding_window\76\main.py
Description: 
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。
如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。
1. 子串 包括 t 中所有元素
2. 子串元素的数量不小于t中对应的元素的数量
3. len >1
4. 如果存在，便是唯一答案
'''


class Solution:
    def minWindow(self, source: str, target: str) -> str:
        """暴力破解:双循环：外层循环迭代子串长度（>= len(target)），内层循环迭代首尾字符，并判断字符是否存在。O(n^3)
        Args:
            source (str): 源字符串  
            target (str): 目标字符串    

        Returns:
            str: 返回包含所有字母的最小子串
        """
        
# class Solution:
#     @staticmethod
#     def is_contain(source:str,target:str) -> bool:
#         """判断target 所有字符是否在source中，只能覆盖target 无重复元素，且 len > 1

#         Args:
#             source (str): 源字符串
#             target (str): 目的字符串

#         Returns:
#             bool: 
#         """
#         for char in target:
#             if char not in source: 
#                 return False
#         return True
#     def minWindow(self, source: str, target: str) -> str:
#         """（未优化）滑动窗口（
#         Args:
#             source (str): 源字符串  
#             target (str): 目标字符串    

#         Returns:
#             str: 返回包含所有字母的最小子串
#         """
#         flag = 0
#         left = 0
#         right = len(target) - 1
#         result_str = source[left:right+1]
#         out_str = source
#         result_len = len(out_str)
#         while right < len(source):
#             contain = self.is_contain(result_str,target)# 判断 temp 是否包含 target 所有字母
#             if contain:
#                 # 如果包含
#                 flag = 1
#                 out_str = result_str if len(result_str) < result_len else out_str
#                 result_len = len(out_str)
#                 left += 1
#                 result_str = source[left:right+1]
#             elif not contain and flag == 0:  # 如果不包含 并且 flag == 0（一直不包含）
#                 right += 1 # 扩大字符串
#                 result_str = source[left:right+1]
#             if not contain and flag == 1: # 如果不包含 并且 flag == 1（之前包含，现在不包含的邻界情况） 
#                 # return source[left - 1:right+1]
#                 flag = 0
            
#         return out_str if result_len < len(source) else ""

class Solution:
    def is_contain(self, window_count, target_count):
        for char in target_count:
            if window_count[char] < target_count[char]:
                return False
        return True

    def minWindow(self, source: str, target: str) -> str:
        target_count = {}  # 目标字符串中每个字符的出现次数
        window_count = {}  # 窗口中每个字符的出现次数
        for char in target:
            target_count[char] = target_count.get(char, 0) + 1

        left, right = 0, 0  # 窗口的左右边界
        formed = 0  # 窗口中已经涵盖的目标字符数量
        min_len = float('inf')  # 最小子串的长度
        min_window_start = 0  # 最小子串的起始索引

        while right < len(source):
            # 扩大窗口，将右边界对应字符的出现次数加一
            char = source[right]
            window_count[char] = window_count.get(char, 0) + 1

            # 检查窗口中的字符是否涵盖了目标字符串的字符
            if char in target_count and window_count[char] == target_count[char]:
                formed += 1

            # 尝试缩小窗口
            while formed == len(target_count):
                # 更新最小子串信息
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window_start = left

                # 缩小窗口，将左边界对应字符的出现次数减一
                char = source[left]
                window_count[char] -= 1

                # 检查窗口是否不再涵盖目标字符串的字符
                if char in target_count and window_count[char] < target_count[char]:
                    formed -= 1

                left += 1

            right += 1

        if min_len == float('inf'):
            return ""
        else:
            return source[min_window_start:min_window_start + min_len]
        
        
if __name__ == "__main__":
    # s = "ADOBECODEBANC"
    # t = "ABC"
    
    s = "a"
    t = "a"
    solution = Solution()
    print(solution.minWindow(s,t))