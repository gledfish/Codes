from functools import cache
'''
Author: gledfish
Date: 2023-10-24 10:28:14
LastEditTime: 2023-10-24 11:06:45
FilePath: \leetcode\practices\1155\main.py
Description: 
这里有 n 个一样的骰子，每个骰子上都有 k 个面，分别标号为 1 到 k 。

给定三个整数 n ,  k 和 target ，
返回可能的方式(从总共 kn 种方式中)滚动骰子的数量，
使正面朝上的数字之和等于 target 。

答案可能很大，你需要对 109 + 7 取模 。
'''

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """
        问题抽象：n个数，每个数取值范围为[1:k]，找和为target的组合的个数
        Args:
            n (int): 骰子的个数
            k (int): 骰子的面数
            target (int): 目标和

        Returns:
            int: 可能方式的个数
        """
        if not (n <= target <= n * k):
            return 0  # 无法组成 target
        MOD = 10 ** 9 + 7
        @cache
        def dfs(i: int, j: int) -> int:
            if i == 0:
                return int(j == 0)
            res = 0
            for x in range(min(k, j + 1)):  # 掷出了 x
                res += dfs(i - 1, j - x)
            return res % MOD
        return dfs(n, target - n)
    
if __name__ == "__main__":
    # n = 1
    # k = 6
    # target = 3
    
    n = 2
    k = 6
    target = 7
    solution = Solution()
    print(solution.numRollsToTarget(n,k,target))
                 
                
        

