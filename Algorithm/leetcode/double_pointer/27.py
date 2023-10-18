'''
Author: gledfish
Date: 2023-10-17 20:01:49
LastEditTime: 2023-10-18 09:07:59
FilePath: \leetcode\27.py
Description: 
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，
并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
'''




# class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:
#         """暴力解法
#         思路:遍历列表:当元素等于 val 时,使用 remove 删除该元素,同时更新索引
#                      当元素不等于 val 时,更新索引.

#         Args:
#             nums (List[int]): 给定数组
#             val (int): 目标元素

#         Returns:
#             int: 返回修改后数组长度
#         """
#         index = 0
#         while index < len(nums):
#             if nums[index] == val:
#                 nums.remove(nums[index])
#             else:
#                 index += 1
#         return len(nums)

# class Solution:
#     def removeElement(self, nums: list[int], val: int) -> int:
#         """双指针（同向指针）
#         特点：两个指针，一快一慢，一个用于遍历，一个用于记录
#             元素位置改变，但相对位置不改变。
        

#         Args:
#             nums (list[int]): 给定数组
#             val (int): 目标元素

#         Returns:
#             int: 返回修改后数组的长度
#         """
#         slow_index = 0
#         quick_index = 0
#         while quick_index < len(nums):
#             if nums[quick_index] != val:
#                 nums[slow_index] = nums[quick_index]
#                 slow_index += 1
#             quick_index += 1
#         return slow_index

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """问题：
        给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，
        并返回移除后数组的新长度。

        不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

        元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
        方法：
        双向指针（相向指针）
        将左边向右相等的元素与右边向左不相等的元素进行交换

        Args:
            nums (list[int]): 给定数组
            val (int): 目标值

        Returns:
            int: 修改数组后的长度
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            while left <= right and nums[left] != val:
                left += 1
            while left <= right and nums[right] == val:
                right -= 1
            if left < right:
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp 
                left += 1
                right -= 1
        return left
            
if __name__ == "__main__":
    # 下一步：修改逻辑，测试更多实例
    # nums = [3,2,2,3] 
    # val = 3 # 2
    # nums = []
    # val = 2 # 0
    nums = [2]
    val = 3 # 0
    # nums = [3,3]
    # val = 5
    # nums = [0,1,2,2,3,0,4,2]
    # val = 2 # 5
    solution = Solution()
    print("length:{}".format(solution.removeElement(nums,val)))
    print(nums)