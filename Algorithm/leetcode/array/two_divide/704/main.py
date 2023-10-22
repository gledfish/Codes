""" 
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ,
写一个函数搜索 nums 中的 target,如果目标值存在返回下标，否则返回 -1。
"""

# 一般方法
def get_target(num_tuple:tuple[int], target:int) ->int:
    """在数组中查找目标值,返回下标或 -1

    Args:
        num_tuple (tuple(int)): 数组
        target (int): 目标值

    Returns:
        int: 下标
    """
    for index,num in enumerate(num_tuple):
        if(num == target):
            return index
    return -1

# 二分法
# 1. 将数组排序
# 2.找到数组中间的值
# 3.通过比较middle与target值的大小，缩小范围
def two_divide(num_tuple:tuple[int], target:int) ->int:
    """在数组中查找目标值
        循环实现

    Args:
        num_tuple (tuple[int]): 数组
        target (int): 目标值

    Returns:
        int: 下标
    """
    left = 0
    right = len(num_tuple) - 1
    middle = (right + left) // 2

    while left <= right:
        if num_tuple[middle] == target:
            return middle 
        elif num_tuple[middle] > target:
            right = middle - 1
            middle = (right + left) // 2
        elif num_tuple[middle] < target:
            left = middle + 1
            middle = (right + left) // 2
    return -1
    
def two_divide_recursive(num_tuple: tuple[int], target: int, left: int = 0, right: int = 5) -> int:
    """在数组中查找目标值
    递归实现

    Args:
        num_tuple (tuple[int]): 数组
        target (int): 目标值
        left (int): 左边界
        right (int): 右边界

    Returns:
        int: 下标
    """
    if left > right:
        return -1

    middle = (left + right) // 2

    if num_tuple[middle] == target:
        return middle
    elif num_tuple[middle] > target:
        return two_divide_recursive(num_tuple, target, left, middle - 1)
    else:
        return two_divide_recursive(num_tuple, target, middle + 1, right)



if __name__ == "__main__":
    num_tuple = [-1,0,3,5,9,12]
    target = 2
    # print(get_target(num_tuple, target)) # -1
    # print(two_divide(num_tuple, target))
    print(two_divide_recursive(num_tuple, target))