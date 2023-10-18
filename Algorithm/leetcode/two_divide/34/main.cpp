/*
 * @Author: gledfish
 * @Date: 2023-10-18 12:28:49
 * @LastEditTime: 2023-10-18 12:32:53
 * @FilePath: \leetcode\two_divide\34\main.cpp
 * @Description: 
给你一个按照非递减顺序排列的整数数组 nums，
和一个目标值 target。
请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。
 */

// def search_range(nums: list[int], target: int) -> list[int]:
//     # 给你一个按照非递减顺序排列的整数数组 nums，
// # 和一个目标值 target。
// # 请你找出给定目标值在数组中的开始位置和结束位置。

// # 如果数组中不存在目标值 target，返回 [-1, -1]。
//     """二分法

//     Args:
//         nums (list[int]): 整数数组
//         target (int): 目标值

//     Returns:
//         list[int]: 索引列表
//     """
//     if len(nums) == 0:
//         return [-1,-1]
//     left = 0
//     right = len(nums) - 1
//     while left <= right:
//         middle = (right - left) // 2 + left
//         if nums[middle] < target:
//             left = middle + 1
//         elif nums[middle] > target:
//             right = middle -1
//         elif nums[middle] == target:
//             start = end = middle
//             # 寻找开始位置的索引
//             while start > 0 and nums[start - 1] == target:
//                 start -= 1
            
//             # 寻找结束位置的索引
//             while end < len(nums) - 1 and nums[end + 1] == target:
//                 end += 1
            
//             return [start, end]
//     return [-1,-1]

#include <iostream>
#include <vector>

using namespace std;

int main(){
    return 0;
}
