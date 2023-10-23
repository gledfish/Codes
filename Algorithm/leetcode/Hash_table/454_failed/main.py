'''
Author: gledfish
Date: 2023-10-23 16:44:02
LastEditTime: 2023-10-23 17:09:26
FilePath: \leetcode\Hash_table\454\main.py
Description: 
给你四个整数数组 nums1、nums2、nums3 和 nums4 ，
数组长度都是 n ，请你计算有多少个元组 (i, j, k, l) 能满足：
0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
'''

# 不能只根据和计算


class Solution:
    def fourSumCount(self, num1: list[int], num2: list[int], 
                     num3: list[int], num4: list[int]) -> int:
        """暴力破解O(n^2)

        Args:
            nums1 (list[int]): _description_
            nums2 (list[int]): _description_
            nums3 (list[int]): _description_
            nums4 (list[int]): _description_

        Returns:
            int: _description_
        """
        sum_dict = dict()
        for num_1 in num1:
            for num_2 in num2:
                my_sum  = num_1 + num_2
                if my_sum in sum_dict:
                    sum_dict[my_sum] += 1
                else:
                    sum_dict[my_sum] = 1
                                  
        count = 0
        for num_3 in num3:
            for num_4 in num4:
                my_sum = -(num_3 + num_4)
                if my_sum in sum_dict:
                    count += sum_dict[my_sum]
        return count
        
if __name__ == "__main__":
    nums1 = [1,2]
    nums2 = [-2,-1]
    nums3 = [-1,2]
    nums4 = [0,2]
    # nums1 = [0]
    # nums2 = [0]
    # nums3 = [0]
    # nums4 = [0]
    solution = Solution()
    print(solution.fourSumCount(nums1,nums2,nums3,nums4))
    
    # 哈希表可能是集合（适用于无重复元素）
    # 也可能是键值对（适用于需要计出现次数的场合）