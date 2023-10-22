# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
# 如果目标值不存在于数组中，返回它将会被按顺序插入的位置(也就是索引)。
# 请必须使用时间复杂度为 O(log n) 的算法
# def searchInsert(nums: list[int], target: int) -> int:
#     """暴力解法

#     Args:
#         nums (list[int]): 给定数组
#         target (int): 数据
#     """
#     for i, v in enumerate(nums):
#         if v >= target:
#             return i
#     return len(nums)
def searchInsert(nums: list[int], target: int) -> int:
    """给定数组中搜索数据并返回索引，如果不存在，插入该数据

    Args:
        nums (List[int]): 给定数组
        target (int): 数据

    Returns:
        int: 索引
    """
    left = 0
    right = len(nums) - 1   
    while left <= right :
        middle = (right - left) >> 2 + left
        if nums[middle] > target :
            right = middle - 1
        elif nums[middle] < target :
            left = middle + 1
        else:
            return middle
    return left
   
   
        
            
            
    
        
if __name__ == "__main__":
    # nums = [1,3,5,6]
    # target = 5
    # nums = [1,3,5,6,9]
    # target = 2
    nums = [1,3,5,6]
    target = 7
    # nums = [1,3,5,6]
    # target = 0
    print(searchInsert(nums, target))