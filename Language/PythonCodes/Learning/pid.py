import os
import multiprocessing


# 获取进程的编号
def work():
    print("work的进程编号：", os.getpid())
    print("work父进程的编号：", os.getppid())

def work2():
    print("work的进程编号：", os.getpid())
    print("work父进程的编号：", os.getppid())

if __name__ == '__main__':

    print(os.getpid())
    work1_pro = multiprocessing.Process(target=work())

    work2_pro = multiprocessing.Process(target=work2())

    work1_pro.start()
    work2_pro.start()

