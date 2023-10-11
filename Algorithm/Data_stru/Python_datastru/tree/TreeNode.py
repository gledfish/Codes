class TreeNode:
    """二叉树
    """
    def __init__(self, val:int):
        self.val:int = val
        self.left:TreeNode | None = None 
        self.right:TreeNode | None = None 

def level_order(root:TreeNode | None) -> list[int]:
    """层序遍历

    Args:
        root (TreeNode | None): 根节点

    Returns:
        list[int]: 遍历结果
    """
    # 初始化队列，加入根节点
    queue:deque[TreeNode] = deque()
    queue.append(root)
    res = []
    while queue:
        node:TreeNode = queue.popleft() # 队列出队
        res.append(node.val)
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right) 
    return res