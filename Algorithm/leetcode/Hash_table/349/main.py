'''
Author: gledfish
Date: 2023-10-22 15:11:34
LastEditTime: 2023-10-22 15:43:05
FilePath: \leetcode\Hash_table\349\main.py
Description: 
给定两个数组 nums1 和 nums2 ，返回 它们的交集 。
输出结果中的每个元素一定是 唯一 的。我
们可以 不考虑输出结果的顺序 。
'''
# 方法一： 暴力破解：O(n^2)

# 方法二：哈希表
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return self.set_intersection(set1, set2)

    def set_intersection(self, set1, set2):
        if len(set1) > len(set2):
            return self.set_intersection(set2, set1)
        return [x for x in set1 if x in set2]


        
if __name__ == "__main__":
    # nums1 = [1,2,2,1]
    # nums2 = [2,2]
    
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    solution = Solution()
    print(solution.intersection(nums1, nums2))