'''
Author: gledfish
Date: 2023-10-21 20:31:16
LastEditTime: 2023-10-21 22:13:10
FilePath: \leetcode\Hash_table\1\main.py
Description: 
给定一个整数数组 nums 和一个整数目标值 target，
请你在该数组中找出 和为目标值 target  的那 两个 整数，
并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
'''
# O(n^2)
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         """两数之和
#            哈希表O(n^2)
           
#         Args:
#             nums (list[int]): _description_
#             target (int): _description_

#         Returns:
#             list[int]: _description_
#         """
#         # 不如 set 
#         # my_dict = {}
#         # for i,v in enumerate(nums):
#         #     my_dict[i] = v
#         # for index,value in my_dict.items():
#         #     add_sum = target - value
#         #     for i,v in my_dict.items():
#         #         if v == add_sum and i != index:
#         #             return (index,i)
#         my_set = set()
#         for i,v in enumerate(nums):
#             my_set.add((i,v))
#         for index,value in my_set:
#             add_sum = target - value
#             for i,v in my_set:
#                 if v == add_sum and i != index:
#                     return (index,i)

# O(nlogn)            
# class Solution:
#     def twoSum(self, nums:list[int], target:int) -> list[int]:
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         # 遍历列表
#         for i in range(len(nums)):
#             # 计算需要找到的下一个目标数字
#             res = target-nums[i]
#                 # 遍历剩下的元素，查找是否存在该数字
#             if res in nums[i+1:]:
#                 # 若存在，返回答案。这里由于是两数之和，可采用.index()方法
#                 # 获得目标元素在nums[i+1:]这个子数组中的索引后，还需加上i+1才是该元素在nums中的索引
#                 return [i, nums[i+1:].index(res)+i+1]
     
     
     
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # 对输入列表进行排序
        nums_sorted = sorted(nums)
        
        # 使用双指针
        left = 0
        right = len(nums_sorted) - 1
        while left < right:
            current_sum = nums_sorted[left] + nums_sorted[right]
            if current_sum == target:
                # 如果和等于目标数，则返回两个数的下标
                left_index = nums.index(nums_sorted[left])
                right_index = nums.index(nums_sorted[right])
                if left_index == right_index:
                    right_index = nums[left_index+1:].index(nums_sorted[right]) + left_index + 1
                return [left_index, right_index]
            elif current_sum < target:
                # 如果总和小于目标，则将左侧指针向右移动
                left += 1
            else:
                # 如果总和大于目标值，则将右指针向左移动
                right -= 1     
# O(n)
# def twoSum(nums, target):
#     num_dict = {}  # 创建一个空字典，用于存储元素及其下标

#     for i, num in enumerate(nums):
#         complement = target - num  # 计算目标值与当前元素的差值

#         if complement in num_dict:  # 检查差值是否在字典中
#             return [num_dict[complement], i]  # 返回配对元素的下标

#         num_dict[num] = i  # 将当前元素及其下标添加到字典中

#     return []  # 如果不存在配对的元素，返回空列表

     
if __name__ == "__main__":
    # nums = [2,7,11,15]
    # target = 9
    
    # nums = [3,2,4]
    # target = 6 # [1,2]
    nums = [3,3] # 0,1
    target = 6
    
    solution = Solution()
    print(solution.twoSum(nums, target))