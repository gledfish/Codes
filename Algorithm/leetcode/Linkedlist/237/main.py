'''
Author: gledfish
Date: 2023-10-24 14:55:31
LastEditTime: 2023-10-24 15:30:00
FilePath: \leetcode\Linkedlist\237\main.py
Description: 
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        current.val = current.next.val
        current.next = current.next.next
                 
if __name__ == "__main__":
    node_0 = ListNode(4)
    node_1 = ListNode(5)
    node_2 = ListNode(1)
    node_3 = ListNode(9)
    
    node_0.next = node_1
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = None
    
    solution = Solution()
    solution.deleteNode(node_1)
    print(node_0.val)# 4
    print(node_0.next.val)# 1
    print(node_1.val) # 1
    print(node_1.next.val) # 9
    print(node_2.val)# 1
    print(node_3.val) # 9
    