def graph_bfs(graph:GraphAdjList, start_vat:Vertex) -> list[Vertex]:
    """广度优先遍历

    Args:
        graph (GraphAdjList): 邻接表
        start_vat (Vertex): 开始顶点

    Returns:
        list[Vertex]: 访问序列
    """
    # 顶点访问序列
    res = []
    # 哈希表
    visited = set[Vertex]([start_vat])
    que = deque[Vertex]([start_vat])
    while len(que) > 0:
        vet = que.popleft() # 队首顶点出队
        res.append(vet) # 记录访问
        # 遍历该顶点的所有邻接顶点
        for adj_vet in graph.adj_list[vet]:
            if adj_vet in visited:
                continue
            que.append(adj_vet) # 只入队未访问的顶点
            visited.add(adj_vet)
    return res