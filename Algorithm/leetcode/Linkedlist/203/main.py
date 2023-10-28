# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """设置一个虚拟节点删除指定节点

        Args:
            head (Optional[ListNode]): _description_
            val (int): _description_

        Returns:
            Optional[ListNode]: _description_
        """
        fake_head = ListNode(next = head)
        current_node = fake_head
        while current_node.next:
            if current_node.next.val == val:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        return fake_head.next
                
                
        