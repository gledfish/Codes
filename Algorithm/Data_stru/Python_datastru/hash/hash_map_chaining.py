class HashMapChaining:
    """链式地址哈希表
    """
    def __init__(self):
        self.size = 0
        self.capacity = 4
        self.load_thres = 2.0 / 3.0 #触发扩容的负载因子阈值
        self.extend_ratio = 2 # 扩容倍数
        self.buckets = [[] for _ in range(self.capacity)]
    
    def Pair(key:int, val:str) -> dict:
        print()

    def hash_func(self, key:int) -> int:
        """哈希函数

        Args:
            key (int): 输入

        Returns:
            int: 输出
        """
        return key % self.capacity
    def load_factor(self) -> float:
        """返回负载因子

        Returns:
            float: 负载因子
        """
        return self.size / self.capacity
    
    def get(self, key:int) -> str|None:
        """查询操作

        Args:
            key (int): 输入

        Returns:
            str|None: 输出查询到的值
        """
        index = self.hash_func(key)
        bucket = self.buckets[index]
        # 遍历桶
        for pair in bucket:
            if pair.key == key:
                return pair.val
        # 若没找到 key 则返回 None
        return None 
    def put(self, key:int, val:str):
        """添加操作

        Args:
            key (int): 哈希输入
            val (str): 值
        """
        # 当负载因子达到阈值，扩容
        if self.load_factor() > self.extend_ratio:
            self.extend()
        index = self.hash_func(key)
        bucket = self.buckets[index]
        for pair in bucket:
            if pair.key == key:
                pair.val == val
                return
        # 无 key 添加
        pair = Pair(key, val)
        bucket.append(pair)
        self.size += 1

    def remove(self, key:int):
        """删除操作

        Args:
            key (int): 哈希函数的输入
        """
        index = self.hash_func(key)
        bucket = self.buckets[index]
        # 遍历桶
        for pair in bucket:
            if pair.key == key:
                bucket.remove(pair)
                self.size -= 1
                break
        
    def extend(self):
        """扩容哈希表
        """
        # 暂存原哈希表
        old_buckets = self.buckets
        self.capacity *= self.extend_ratio
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        for bucket in old_buckets:
            for pair in bucket:
                self.put(pair.key, pair.val)
    
    def print(self):
        """打印哈希表
        """
        for bucket in self.buckets:
            res = []
            for pair in bucket:
                res.append(str(pair.key) + "->" + pair.val)
            print(res)
    