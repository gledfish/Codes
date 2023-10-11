class ListNode:
    """
    链表节点类
    """
    def __init__(self, val:int):
        self.val:int = val 
        self.next:ListNode | None = None 

def insert(n0:ListNode, p:ListNode):
    """在节点n后插入p节点

    Args:
        n0 (ListNode): 前置节点
        p (ListNode): 待插入节点
    """
    n1 = n0.next
    n0.next = p
    p.next = n1 

def remove(n0:ListNode):
    """删除n0后的首个节点

    Args:
        n0 (ListNode): 前置节点
    """ 
    n1 = n0.next
    n0.next = n1.next

def access(head:ListNode, index:int) -> ListNode | head:
    """访问链表中的节点

    Args:
        head (ListNode): 链表的表头
        index (int): 待访问节点的索引

    Returns:
        ListNode | head: 待访问节点
    """
    for _ in range(index):
        if not head:
            return None
        head = head.next 
    return head

def find(head:ListNode, target:int) -> int:
    """在链表中查找值为target的首个节点

    Args:
        head (ListNode): 待查找链表
        target (int): 目标节点

    Returns:
        int: 节点索引
    """ 
    index = 0
    while head:
        if head.val == target:
            return index 
        head = head.next
        index += 1
    return -1
    
    
if __name__ == "__main__":
    n0 = ListNode(1)
    n1 = ListNode(2)
    n0.next = n1
    

