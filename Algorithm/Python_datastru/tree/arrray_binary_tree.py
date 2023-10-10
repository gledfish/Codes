class ArrayBinaryTree:
    """数组表示下的二叉树
    """
    def __init__(self, arr:list[int| None]):
        """构造方法

        Args:
            arr (list[int |  None]): 数据
        """
        self.__tree = list(arr)
    
    def size(self):
        """
        节点数量
        """
        return len(self.__tree)
    
    def val(self, i:int) ->int:
        """获取索引为 i 节点的值

        Args:
            i (int): 索引

        Returns:
            int: 值
        """
        if i < 0 or i >= self.size():
            return None 
        return self.__tree[i]
    def left(self, i:int) ->int | None:
        """获取索引为i节点的左子节点的索引

        Args:
            i (int): 根索引   

        Returns:
            int | None: 左子树索引
        """
        return 2 * i + 1
    def right(self, i: int) -> int | None:
        """获取索引为 i 节点的右子节点的索引"""
        return 2 * i + 2
    def parent(self, i: int) -> int | None:
        """获取索引为 i 节点的父节点的索引"""
        return (i - 1) // 2
    
    def level_order(self) -> list[int]:
        """层序遍历"""
        self.res = []
        # 直接遍历数组
        for i in range(self.size()):
            if self.val(i) is not None:
                self.res.append(self.val(i))
        return self.res