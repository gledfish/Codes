'''
Author: gledfish
Date: 2023-10-19 14:18:11
LastEditTime: 2023-10-19 14:36:03
FilePath: \leetcode\sliding_window\209\main.py
Description: 
给定一个含有 n 个正整数的数组和一个正整数 target 。
找出该数组中满足其总和大于等于 target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，
并返回其长度。如果不存在符合条件的子数组，返回 0 。
'''
from sys import maxsize
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        """滑动窗口算法

        Args:
            target (int): 目标值
            nums (list[int]): 给定数组

        Returns:
            int: 连续子数组的长度
        """
        sub_len = maxsize # 滑动窗口长度
        i = 0 # 窗口起始位置
        num_sum = 0 # 记录子数组元素之和
        for j in range(len(nums)):
            num_sum += nums[j]
            while num_sum >= target:
                temp_len = j - i + 1
                sub_len = temp_len if temp_len < sub_len else sub_len
                num_sum -= nums[i]
                i += 1
        return sub_len if sub_len < maxsize else 0
                

if __name__ == "__main__":
    target = 7
    nums = [2,3,1,2,4,3]
    solution = Solution() # 2
    print(solution.minSubArrayLen(target, nums))
