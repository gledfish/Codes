'''
Author: gledfish
Date: 2023-10-24 19:15:33
LastEditTime: 2023-10-24 20:51:14
FilePath: \leetcode\practices\2908\main.py
Description: 
给你一个下标从 0 开始的整数数组 nums 。

如果下标三元组 (i, j, k) 满足下述全部条件，则认为它是一个 山形三元组 ：

i < j < k
nums[i] < nums[j] 且 nums[k] < nums[j]
请你找出 nums 中 元素和最小 的山形三元组，并返回其 元素和 。如果不存在满足条件的三元组，返回 -1 。
'''

# 分治 O(n^2)
# class Solution:
#     def minimumSum(self, nums: list[int]) -> int:
#         n = len(nums)
#         min_sum = float('inf')

#         for j in range(1, n - 1):
#             left_min = min(nums[:j])
#             right_min = min(nums[j + 1:])
            
#             if nums[j] > left_min and nums[j] > right_min:
#                 min_sum = min(min_sum, nums[j] + left_min + right_min)

#         return min_sum if min_sum != float('inf') else -1 


# 动态规划 O(n)
# class Solution:
#     def minimumSum(self, nums: list[int]) -> int:
#         n = len(nums)
#         if n < 3: # 数组长度小于3，一定不存在
#             return -1
        
#         left_min = [float('inf')] * n
#         right_min = [float('inf')] * n

#         for i in range(1, n): # 确定左边每个 i 下的最小值（注意：下标为i时，求出的最小值是包括 i - 1 往左元素的最小值）
#             left_min[i] = min(left_min[i - 1], nums[i - 1])

#         for i in range(n - 2, -1, -1):# 确定右边每个 i 下的最小值
#             right_min[i] = min(right_min[i + 1], nums[i + 1])

#         min_sum = float('inf')

#         for j in range(1, n - 1): # 遍历数组寻找最小的和
#             if nums[j] > left_min[j] and nums[j] > right_min[j]:
#                 min_sum = min(min_sum, nums[j] + left_min[j] + right_min[j])

#         return min_sum if min_sum != float('inf') else -1
  


# 前后缀分解

if __name__ == "__main__":
    # nums = [8,6,1,5,3]
    nums = [5,4,8,7,10,2]
    solution = Solution()
    print(solution.minimumSum(nums))