# global 关键字在函数的

def globalTest():
    global eggs
    eggs = "global"
# eggs 为全局变量

eggs = "local"
#可以修改
print(eggs)
