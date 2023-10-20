'''
Author: gledfish
Date: 2023-10-19 11:01:43
LastEditTime: 2023-10-19 13:20:35
FilePath: \leetcode\double_pointer\844\main.py
Description: 
给定 s 和 t 两个字符串，当它们分别被输入到空白的文本编辑器后，
如果两者相等，返回 true 。# 代表退格字符。
'''

# class Solution:
#     def backspaceCompare(self, s: str, t: str) -> bool:
#         """暴力求解

#         Args:
#             s (str): s 字符串
#             t (str): t 字符串

#         Returns:
#             bool: 返回是否相等
#         """
#         @staticmethod
#         def transfer_string(s:str) -> str:
#             """将字符串转换成字面量字符串

#             Args:
#                 s (str): 字符串

#             Returns:
#                 str: 转换后字符串
#             """
#             s = list(s)
#             s_index = 0
#             while s_index < len(s):
#                 if s_index == 0 and s[s_index] == '#':
#                     s.pop(s_index)# 删除 #
#                     s_index -= 1
#                 elif s[s_index] == '#':
#                     s.pop(s_index) # 删除 #
#                     s.pop(s_index - 1) # 删除 # 之前的元素
#                     s_index -= 2
#                 s_index += 1
#             return s
#         # 思路一：将字符串转换成字面量字符串，然后比较
#         s = transfer_string(s)
#         t = transfer_string(t)
#         # return (s,t)
#         return s == t

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """双指针

        Args:
            s (str): 给定字符串
            t (str): 给定字符串

        Returns:
            bool: 
        """
        def transfer_string(s:str) -> str:
            """将含有转义字符的字符串转换成字面量字符串
            """ 
            fixed_str = []
            for char in s:
                if char != '#':
                    fixed_str.append(char)
                elif fixed_str:
                    fixed_str.pop()
            return ''.join(fixed_str)
        return transfer_string(s) == transfer_string(t)       
        # return (transfer_string(s),transfer_string(t))
if __name__ == "__main__":
    # s = "ab#c"
    # t = "ad#c"
    
    # s = "ab##"
    # t = "c#d#"
    
    # s = "a#c"
    # t = "b"
    # s = "j##xfix"
    # t = "j##xfix"
    solution = Solution()
    print(solution.backspaceCompare(s,t))