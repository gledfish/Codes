def search(self, num:int) -> TreeNode | None:
    
    cur = self.__root
    # 循环查找
    while cur is not None:
        if cur.val < num:
            cur = cur.right
        elif cur.val > num:
            cur = cur.left
        # 找到目标节点，跳出循环
        else:
            break
    return cur