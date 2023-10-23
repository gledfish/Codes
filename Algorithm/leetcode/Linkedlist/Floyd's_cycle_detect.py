'''
Author: gledfish
Date: 2023-10-22 16:33:05
LastEditTime: 2023-10-22 16:35:38
FilePath: \leetcode\Linkedlist\Floyd's_cycle_detect.py
Description: 
'''
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def hasCycle(head):
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True
if __name__ == "__main__":
    
    # 示例用法
    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node2  # 创建循环

    result = hasCycle(head)
    print(result)  # 输出: True