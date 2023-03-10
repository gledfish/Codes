
import multiprocessing
import time

# 定义全局变量

def write_list():
    for i in range(3):
        my_list.append(i)
        print("add:", i)
    print("write_data", my_list)

def read_list():
    print("read_data", my_list)

if __name__ == '__main__':

    my_list = list()
# 创建写入进程
    write_process = multiprocessing.Process(target=write_list())
# 创建读取进程
    read_process = multiprocessing.Process(target=read_list())

# 进程执行
    write_process.start()
    time.sleep(1)
    read_process.start()