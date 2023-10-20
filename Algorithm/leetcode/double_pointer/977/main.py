'''
Author: gledfish
Date: 2023-10-19 13:35:58
LastEditTime: 2023-10-19 13:51:48
FilePath: \leetcode\double_pointer\977\main.py
Description: 
给你一个按 非递减顺序 排序的整数数组 nums，
返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
'''
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        """双指针

        Args:
            nums (list[int]): 给定数组

        Returns:
            list[int]: 平方，排序后数组
        """
        length = len(nums)
        result = [0] * length
        left = 0
        right = length - 1
        index = length -1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[index] = nums[left] * nums[left]
                left += 1
            else:
                result[index] = nums[right] * nums[right]
                right -= 1
            index -= 1
        return result 
                
if __name__ == "__main__":
    nums = [-4,-1,0,3,10]     # [16,1,0,9,100]
    
    
    solution = Solution()
    print(solution.sortedSquares(nums))