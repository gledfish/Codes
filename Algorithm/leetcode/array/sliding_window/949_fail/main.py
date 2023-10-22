'''
Author: gledfish
Date: 2023-10-20 16:51:06
LastEditTime: 2023-10-20 20:41:18
FilePath: \leetcode\sliding_window\949_fail\main.py
Description: 
你正在探访一家农场，农场从左到右种植了一排果树。这些树用一个整数数组 fruits 表示，其中 fruits[i] 是第 i 棵树上的水果 种类 。

你想要尽可能多地收集水果。然而，农场的主人设定了一些严格的规矩，你必须按照要求采摘水果：

你只有 两个 篮子，并且每个篮子只能装 单一类型 的水果。每个篮子能够装的水果总量没有限制。
你可以选择任意一棵树开始采摘，你必须从 每棵 树（包括开始采摘的树）上 恰好摘一个水果 。采摘的水果应当符合篮子中的水果类型。每采摘一次，你将会向右移动到下一棵树，并继续采摘。
一旦你走到某棵树前，但水果不符合篮子的水果类型，那么就必须停止采摘。

'''

# from collections import Counter
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        """滑动窗口
        Args:
            fruits (List[int]): 果树数组，下标代表果树i，fruits[i] 表示该果树的水果种类

        Returns:
            int: _description_
        """
        left = max_fruits = 0
        # selected_fruits = Counter() # 挑选的水果
        selected_fruits = {} # 保存已经选择的水果种类：数量
        for index, value in enumerate(fruits):
            if value not in selected_fruits:
                selected_fruits[value] = 0
            selected_fruits[value] += 1
            while len(selected_fruits) > 2:
                selected_fruits[fruits[left]] -= 1
                if selected_fruits[fruits[left]] == 0:
                    del selected_fruits[fruits[left]]
                left += 1
            max_fruits= max(max_fruits, index - left + 1)
        return max_fruits   
                
if __name__ == "__main__":
    # fruits = [1,2,1] # 3
    # fruits = [0,1,2,2] # 3
    # fruits = [1,2,3,2,2] # 4
    fruits = [3,3,3,1,2,1,1,2,3,3,4] # 5
    solution = Solution()
    print(solution.totalFruit(fruits))