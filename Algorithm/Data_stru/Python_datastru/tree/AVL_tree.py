class TreeNode:
    """AVL树节点类
    """
    def __init__(self, val:int):
        self.val: int = val # 节点值
        self.height:int = 0 # 节点高度
        self.left:TreeNode | None = None # 左子节点引用
        self.right:TreeNode | None = None # 右子节点引用

    
    def height(self, node:TreeNode | None) -> int:
        """获取节点高度

        Args:
            node (TreeNode | None): 节点

        Returns:
            int: 高度
        """
        if node is not None:
            return node.height
        return -1
    
def __update_height(self, node:TreeNode | None):
    """更新节点高度

    Args:
        node (TreeNode | None): 节点    
    """
    node.height = max([self.height(node.left), self.height(node.right)]) + 1

def balance_factor(self, node:TreeNode | None) -> int:
    """获取平衡因子

    Args:
        node (TreeNode | None): 节点

    Returns:
        int: 平衡因子
    """
    if node is None:
        return 0
    return self.height(node.left) - self.height(node.right)

def __right_rotate(self, node:TreeNode | None) -> TreeNode|None:
    """右旋操作

    Args:
        node (TreeNode | None): 右旋节点

    Returns:
        TreeNode|None: 右旋后的节点
    """
    child = node.left
    grand_child = child.right
    # 以child为原点，将 node 向右旋转
    child.right = node
    node.left = grand_child
    # 更新节点高度
    self.__update_height(node)
    self.__update_height(child)
    # 返回旋转后子树的根节点
    return child

def __left_rotate(self, node: TreeNode | None) -> TreeNode | None:
    """左旋操作"""
    child = node.right
    grand_child = child.left
    # 以 child 为原点，将 node 向左旋转
    child.left = node
    node.right = grand_child
    # 更新节点高度
    self.__update_height(node)
    self.__update_height(child)
    # 返回旋转后子树的根节点
    return child

def __rotate(self, node: TreeNode | None) -> TreeNode | None:
    """执行旋转操作，使该子树重新恢复平衡"""
    # 获取节点 node 的平衡因子
    balance_factor = self.balance_factor(node)
    # 左偏树
    if balance_factor > 1:
        if self.balance_factor(node.left) >= 0:
            # 右旋
            return self.__right_rotate(node)
        else:
            # 先左旋后右旋
            node.left = self.__left_rotate(node.left)
            return self.__right_rotate(node)
    # 右偏树
    elif balance_factor < -1:
        if self.balance_factor(node.right) <= 0:
            # 左旋
            return self.__left_rotate(node)
        else:
            # 先右旋后左旋
            node.right = self.__right_rotate(node.right)
            return self.__left_rotate(node)
    # 平衡树，无须旋转，直接返回
    return node

