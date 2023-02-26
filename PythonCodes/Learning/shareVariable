# 全局变量
import threading

g_num = 0

# 对g_sun进行加的操作
def sum_num():
    for i in range(100000000):
        global g_num
        g_num += 1
    print("g_num:", g_num)

def sum_num2():
    for i in range(100000000):
        global g_num
        g_num += 1
    print("g_num2:", g_num)

if __name__ == '__main__':

    # 创建子线程
    sum1_thread = threading.Thread(target=sum_num())
    sum2_thread = threading.Thread(target=sum_num2())

    # 启动进程
    sum1_thread.start()
    sum2_thread.start()


