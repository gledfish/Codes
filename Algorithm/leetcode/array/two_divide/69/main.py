# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。

# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。

def karatsuba_multiply(x:int,y:int) -> int:
    # 将 x 和 y 转换为字符串
    x_str = str(x)
    y_str = str(y)

    # 将 x 和 y 填充为相同的长度
    max_len = max(len(x_str), len(y_str))
    x_str = x_str.zfill(max_len)
    y_str = y_str.zfill(max_len)

    # 基本情况：如果整数长度为 1，则直接计算乘积
    if len(x_str) == 1:
        return int(x_str) * int(y_str)

    # 拆分 x 和 y
    mid = len(x_str) // 2
    a, b = int(x_str[:mid]), int(x_str[mid:])
    c, d = int(y_str[:mid]), int(y_str[mid:])

    # 递归计算乘积
    ac = karatsuba_multiply(a, c)
    bd = karatsuba_multiply(b, d)
    ad_bc = karatsuba_multiply(a + b, c + d) - ac - bd

    # 计算最终乘积
    result = (ac * 10**(2 * (len(x_str) - mid))) + (ad_bc * 10**mid) + bd
    return result
# def mySqrt(x: int) -> int:
#     """暴力解法

#     Args:
#         x (int): 非负整数

#     Returns:
#         int: 算术平方根
#     """
#     for i in range(x + 1):
#         if  karatsuba_multiply(i,i) <= x and  karatsuba_multiply(i+1,i+1) > x: # 46999
#         # if i * i <= x and (i + 1) * (i + 1) > x: # 46339
#             return i 

# pass
# def mySqrt(x: int) -> int: 
#     """二分法(太慢了)

#     Args:
#         x (int): 非负整数

#     Returns:
#         int: 算术平方根
#     """
#     if x == 0:
#         return 0
#     if x == 1:
#         return 1
#     nums = [i for i in range(x + 1)]
#     left = 0
#     right = len(nums) - 1
#     while left <= right:
#         middle = (right + left) // 2
#         result_left = nums[middle] * nums[middle]
#         result_right = nums[middle + 1] * nums[middle + 1]
#         if result_left <= x and result_right > x:
#             return middle
#         if result_left <= x and result_right <= x:
#             left = middle + 1
#         if result_left > x :
#             right = middle - 1
            
# def mySqrt(x: int) -> int:
#     """二分法(修改版本)

#     Args:
#         x (int): 非负整数

#     Returns:
#         int: 算术平方根
#     """
#     left = 0
#     right = x
#     while left <= right:
#         middle = (left + right) // 2
#         result = middle * middle
#         if result == x:
#             return middle
#         elif result > x:
#             right = middle - 1
#         else:
#             left = middle + 1
#     return right

# 牛顿迭代法
def mySqrt(x: int) -> int:
    """牛顿迭代法求平方根

    Args:
        x (int): 非负整数

    Returns:
        int: 平方根
    """
    if x == 0:
        return 0

    sqrt = x
    while True:
        new_sqrt = (sqrt + x // sqrt) // 2
        if new_sqrt >= sqrt:
            return sqrt
        sqrt = new_sqrt
if __name__ == "__main__":
    # x = 1 # 1
    # x = 4 # 1
    # x = 8 # 2
    # x = 2147395599 #  46339
    # x = 0 # 0
    x = 10 # 2
    print(mySqrt(x)) 

    