'''
Author: gledfish
Date: 2023-10-23 21:08:12
LastEditTime: 2023-10-23 21:49:16
FilePath: \leetcode\Hash_table\15\main.py
Description: 
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，
同时还满足 nums[i] + nums[j] + nums[k] == 0 。
请你返回所有和为 0 且不重复的三元组。
'''
# 双指针
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 存储结果的列表
        result = []
        # 对输入列表进行排序
        nums.sort()

        # 遍历排序后的列表，固定一个数作为第一个数
        for i in range(len(nums) - 2):
            # 跳过重复的固定数
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 使用双指针在剩余部分寻找另外两个数
            left = i + 1
            right = len(nums) - 1
            while left < right:
                # 计算当前三个数的和
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    # 和小于0，左指针右移
                    left += 1
                elif total > 0:
                    # 和大于0，右指针左移
                    right -= 1
                else:
                    # 找到一组解
                    result.append([nums[i], nums[left], nums[right]])

                    # 跳过重复的左指针和右指针
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # 移动指针继续寻找下一组解
                    left += 1
                    right -= 1

        return result
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i in range(len(nums) - 2):
            # 跳过重复的固定数
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            num_map = {}

            for j in range(i + 1, len(nums)):
                complement = target - nums[j]

                if complement in num_map and num_map[complement] > 0:
                    result.append([nums[i], complement, nums[j]])
                    num_map[complement] -= 1

                num_map[nums[j]] = num_map.get(nums[j], 0) + 1

        return result
