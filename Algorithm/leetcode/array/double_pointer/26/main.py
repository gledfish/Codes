'''
Author: gledfish
Date: 2023-10-18 15:51:06
LastEditTime: 2023-10-18 17:39:48
FilePath: \leetcode\double_pointer\26\main.py
Description: 
给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。

考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：

更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。
返回 k 。
'''
# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         """暴力解法
#         思路:遍历列表:当出现重复元素时删除该元素

#         Args:
#             nums (List[int]): 给定数组

#         Returns:
#             int: 返回修改后数组长度
#         """
#         index = 0
#         while index < len(nums) - 1:
#             pointer = index + 1
#             # 遍历每一个元素
#             while pointer < len(nums):
#                 # 如果 nums[pointer] == nums[index] 则删除该元素。同时下标左移一位
#                 if nums[pointer] == nums[index]:
#                     nums.pop(pointer)
#                     pointer -= 1
#                 pointer += 1
#             index += 1   
#         return len(nums)

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """双指针（同向指针）
        Args:
            nums (list[int]): 给定数组

        Returns:
            int: 数组长度
        """
        # 定义两个指针，一个指向待验证元素，一个遍历数组
        slow_index = 0
        quick_index = 1
        while quick_index < len(nums):  
            # 如果元素相等，更新快指针
            if nums[quick_index] <= nums[slow_index]:
                quick_index += 1
            elif nums[quick_index] > nums[slow_index]:
                # 不相等,且大于该元素，将元素加到慢指针之后
                slow_index += 1
                nums[slow_index] = nums[quick_index]
                if quick_index == len(nums) - 1:
                    return slow_index + 1
                quick_index = slow_index + 1
        # 如果因为超出列表长度退出循环，返回 slow_index + 1
        return slow_index + 1



class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """反向指针

        Args:
            nums (list[int]): 给定数组

        Returns:
            int: 返回修改后数组长度
        """
if __name__ == "__main__":
    # nums = [1,1,2,2,3] # 3
    # nums = [1] # 1
    # nums = [0,0,1,1,1,2,2,3,3,4]
    nums = [1,1,1] # 1
    # nums = [1,2,2]
    solution = Solution()
    print(solution.removeDuplicates(nums))
    print(nums)
    