'''
Author: gledfish
Date: 2023-10-18 21:39:39
LastEditTime: 2023-10-18 22:55:25
FilePath: \leetcode\double_pointer\283\main.py
Description: 
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。
'''

# 使用同向同速双指针，速度过慢，逻辑不复杂，但边界处理特别麻烦。
# 待优化：边界处理
# class Solution:
#     def moveZeroes(self, nums: list[int]) -> None:
#         """给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。
            
#         """
#         zero_index = 0 # 找 0
#         no_zero_index = 0  # 找非 0 值
#         while zero_index < len(nums) and no_zero_index < len(nums): 
#             while  zero_index < len(nums) and nums[zero_index] != 0 : # 找0
#                 zero_index += 1
#             while no_zero_index < len(nums) and nums[no_zero_index] == 0 :
#                 no_zero_index += 1
#             # 找到符合条件的 0 值和非 0 值进行交换
#             #  条件：no_zero_index > zero_index
#             if zero_index == len(nums) or no_zero_index == len(nums):
#                 return nums
#             if zero_index < no_zero_index:
#                 temp = nums[zero_index]
#                 nums[zero_index] = nums[no_zero_index]
#                 nums[no_zero_index] = temp
#                 # 交换完成，0 值索引增加1 ，非零值索引大于 0值索引
#                 zero_index += 1
#                 no_zero_index = zero_index + 1
#             # 如果不能交换，则非 0 值太小，寻找更大的非 0 值
#             elif zero_index > no_zero_index:
#                 no_zero_index += 1
#             # 如果超出范围，结束
#         return nums          
    
class Solution:
    # 同向快慢指针
    def moveZeroes(self, nums: list[int]) -> None:
        zero_index = 0  # 记录假设 0 元素的位置，在循环过程中逐渐后移
        for i in range(len(nums)):
            if nums[i] != 0:  # 遇到非零元素
                nums[i], nums[zero_index] = nums[zero_index], nums[i]  # 将非零元素与第一个0元素交换位置
                zero_index += 1  # 0元素位置后移

        return nums        
            
if __name__ == "__main__":
    # nums = [0,1,0,3,12]
    # nums = [1, 3, 0, 4, 0, 9]
    # nums = [0]
    # nums = [1,0,3,4]
    # nums = [1]
    # nums = [0,1]
    solution = Solution()
    print(solution.moveZeroes(nums))
