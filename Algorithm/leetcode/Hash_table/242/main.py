'''
Author: gledfish
Date: 2023-10-21 19:47:33
LastEditTime: 2023-10-21 20:13:06
FilePath: \leetcode\Hash_table\242\main.py
Description: 
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词
'''
class Solution:
    @staticmethod
    def to_dict(s:str) -> {}:
        s_dict = {}
        for char in s:
            if char not in s_dict:
                s_dict[char] = 1
            else:
                s_dict[char] += 1
        return s_dict
    def isAnagram(self, s: str, t: str) -> bool:
        """判断是否是字母异味词

        Args:
            s (str): 源字符串
            t (str): 目标字符串

        Returns:
            bool: 
        """
        if len(s) != len(t):
            return False
        # 将 s 存入哈希表
        s_dict = Solution.to_dict(s)
        # 判断 t 是否在 哈希表中
        #  1. 新创建一个t_dict，判断两个dict是否相同
        # t_dict = Solution.to_dict(t)
        # if s_dict == t_dict:
        #     return True
        # else:
        #     return False
    #  2. 试图将s_dict 清空，如果len(s_dict) == 0 true， 否则 false
        for char in t:
            if char not in s_dict:
                return False
            else:
                s_dict[char] -= 1
                if s_dict[char] == 0:
                    del s_dict[char]
        return True if len(s_dict) == 0 else False 
if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    # s = "rat"
    # t = "car"
    
    solution = Solution()
    print(solution.isAnagram(s,t))