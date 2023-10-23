'''
Author: gledfish
Date: 2023-10-23 16:14:58
LastEditTime: 2023-10-23 16:26:22
FilePath: \leetcode\practices\2678\main.py
Description: 
给你一个下标从 0 开始的字符串 details 。
details 中每个元素都是一位乘客的信息，信息用长度为 15 的字符串表示，表示方式如下：

前十个字符是乘客的手机号码。
接下来的一个字符是乘客的性别。
接下来两个字符是乘客的年龄。
最后两个字符是乘客的座位号。
请你返回乘客中年龄 严格大于 60 岁 的人数。
'''
class Solution:
    def countSeniors(self, details: list[str]) -> int:
        """暴力求解O(n)

        Args:
            details (list[str]): 乘客信息字符串

        Returns:
            int: 个数
        """
        sum = 0
        for passenger in details:
            if passenger[11:13] > '60':
                sum += 1
        return sum

if __name__ == '__main__':
    details = ["7868190130M7522",
               "5303914400F9211",
               "9273338290F4010"]
    solution = Solution()
    print(solution.countSeniors(details))