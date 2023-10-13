def fibonacci(n:int):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 30  # 要计算的斐波那契数列的索引

# 在 CPython 中计算执行时间
import time
# start_time = time.time()
# result_cpython = fibonacci(n)
# end_time = time.time()
# execution_time_cpython = end_time - start_time

# 在 PyPy 中计算执行时间
start_time = time.time()
result_pypy = fibonacci(n)
end_time = time.time()
execution_time_pypy = end_time - start_time

# # 打印结果
# print(f"CPython 结果: {result_cpython}")
# print(f"CPython 执行时间: {execution_time_cpython} 秒") # 0.13539648056030273
print(f"PyPy 结果: {result_pypy}")
print(f"PyPy 执行时间: {execution_time_pypy} 秒") # 0.03