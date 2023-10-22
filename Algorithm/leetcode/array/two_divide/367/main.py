# 给你一个正整数 num 。如果 num 是一个完全平方数，则返回 true ，否则返回 false 。

# 完全平方数 是一个可以写成某个整数的平方的整数。换句话说，它可以写成某个整数和自身的乘积。

# 不能使用任何内置的库函数，如  sqrt

# class Solution:
#     def isPerfectSquare(self, num: int) -> bool:
#         """暴力

#         Args:
#             num (int): 正整数

#         Returns:
#             bool: 返回是否是完全平方数
#         """
#         for i in range(num + 1):
#             if i * i == num:
#                 return True
#         return False
    
# class Solution:
#     def isPerfectSquare(self, num: int) -> bool:
#         """二分法

#         Args:
#             num (int): 正整数

#         Returns:
#             bool: 返回是否是完全平方数
#         """
#         left = 0
#         right = num 
#         while left <= right:
#             middle = (left + right) // 2
#             result = middle * middle
#             if result == num:
#                 return True
#             elif result < num:
#                 left = middle + 1
#             elif result > num:
#                 right = middle - 1
#         return False

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """牛顿迭代法

        Args:
            num (int): 正整数

        Returns:
            bool: _description_
        """
        if num < 2:
            return True
        
        x = num // 2
        while x * x > num:
            x = (x + num // x) // 2
        
        return x * x == num

if __name__ == "__main__":
    # num = 16
    num = 14
    # num = 1
    # num = 2000105819 # 暴力求解  超时
    
    solution = Solution()
    print(solution.isPerfectSquare(num))