import numba
import numpy as np 

print(numba.__version__)
# x = np.arange(100).reshape(10,10)

# @jit(nopython=True) # 最好性能模式
# #@njit
# def go_fast(a): # 当函数第一次被调用时将被编译成机器码
#     trace = 0.0
#     for i in range(a.shape[0]): # 循环
#         trace += np.tanh(a[i,i])# Numpy函数
#     return a + trace # Numpy广播 都是jit的用武之地

# # jit 不适用于复杂的数据类型
# print(go_fast(x))