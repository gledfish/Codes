
list:list[int] = [1, 2, 3, 4, 5]
num:int = list[1]
print(num)

# class MyList:
#     """列表简易实现
#     """
#     def __init__(self):
#         self.__capacity:int = 10 #初始容量
#         self.__nums:list[int] = [0] * self.__capacity
#         self.__size:int = 0 # 列表长度
#         self.__extend_ratio:int = 2 # 每次列表扩容的倍数

#     def size(self) -> int:
#         """获取列表长度

#         Returns:
#             int: 列表长度
#         """ 
#         return self.__size
#     def capacity(self) -> int:
#         """获取列表容量

#         Returns:
#             int: 列表容量
#         """
#         return self.__capacity
#     def get(self, index:int) -> int:
#         """访问元素

#         Args:
#             index (int): 元素索引

#         Returns:
#             int: 元素值
#         """
#         if index < 0 or index >= self.__size:
#             raise IndexError("索引越界")
#         return self.__nums[index]
    
#     def set(self, num:int, index:int):
#         """更新索引处的元素

#         Args:
#             num (int): 元素值
#             index (int): 索引
#         """
#         if index < 0 or index >= self.__size:
#             raise IndexError("索引越界")
#         self.__nums[index] = num
#     def add(self, num:int):
#         """尾部添加元素


#         Args:
#             num (int): 元素值
#         """
#         if self.size() == self.capacity():
#             self.__extend_ratio()
#         self.__nums[self.__size] = num 
#         self.__size += 1
#     def insert(self, num:int, index:int):
#         if index < 0 or index >= self.__size:
#             raise IndexError("索引越界")
#         if self.size() == self.capacity():
#             self.__extend_ratio()
#         for j in range(self.__size - 1, index -1, -1):
#             self.__nums[j+1] = self.__nums[j]
#         self.__nums[index] = num
#         # 更新元素数量
#         self.size+1

#     def remove(self, index: int) -> int:
#         """删除元素

#         Args:
#             index (int): 元素索引

#         Returns:
#             int: 被删除的元素
#         """
#         if index < 0 or index >= self.__size:
#             raise IndexError("索引越界")
#         num = self.__nums[index]
#          # 索引 i 之后的元素都向前移动一位
#         for j in range(index, self.__size - 1):
#             self.__nums[j] = self.__nums[j + 1]
#         # 更新元素数量
#         self.__size -= 1
#         # 返回被删除元素
#         return num

#     def extend_capacity(self):
#         """列表扩容"""
#         # 新建一个长度为原数组 __extend_ratio 倍的新数组，并将原数组拷贝到新数组
#         self.__nums = self.__nums + [0] * self.capacity() * (self.__extend_ratio - 1)
#         # 更新列表容量
#         self.__capacity = len(self.__nums)

#     def to_array(self) -> list[int]:
#         """返回有效长度的列表"""
#         return self.__nums[: self.__size]
