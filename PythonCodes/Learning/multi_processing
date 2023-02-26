import multiprocessing
# 导入进程包

def func1():
    print("func1")


def func2():
    print("func2")

def func3(num):
    print(num)
if __name__ == '__main__':
# 创建进程
    func1_pro = multiprocessing.Process(target=func1())
    func2_pro = multiprocessing.Process(target=func2())
    func3_pro = multiprocessing.Process(target=func3(3))

# 启动进程
    func1_pro.start()
    func2_pro.start()
    func3_pro.start()

