class GraphAdjMat:
    """基于邻接矩阵实现无向图类
    """
    # 顶点列表
    vertices: list[int] = []
    # 邻接矩阵，行列索引对应"顶点索引"
    adj_mat: list[list[int]] = []

    def __init__(self, vertices:list[int], edges:list[list[int]]):
        """构造方法

        Args:
            vertices (list[int]): 顶点
            edges (list[list[int]]): 边
        """
        # 添加顶点
        for val in vertices:
            self.add_vertex(val)
        # 添加边
        for e in edges:
            self.add_edge(e[0], e[1])
        
    def size(self) -> int:
        """获取顶点数量
        """
        return len(self.vertices)
    
    def add_vertex(self, val:int):
        """添加顶点

        Args:
            val (int): 顶点值
        """
        n = self.size()
        self.vertices.append(val)
        new_row = [0] * n
        self.adj_mat.append(new_row)
        for row in self.adj_mat:
            row.append(0)
    
    def remove_vertex(self, index: int):
        """删除顶点"""
        if index >= self.size():
            raise IndexError()
        # 在顶点列表中移除索引 index 的顶点
        self.vertices.pop(index)
        # 在邻接矩阵中删除索引 index 的行
        self.adj_mat.pop(index)
        # 在邻接矩阵中删除索引 index 的列
        for row in self.adj_mat:
            row.pop(index)
    

        

