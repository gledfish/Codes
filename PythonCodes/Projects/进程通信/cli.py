# import os
# import threading
# from multiprocessing import Process, Pipe


# def receive_message(conn, role):
#     while True:
#         msg = conn.recv()
#         if msg:
#             print(role + ":" + msg)


# def parent(child_conn):
#     threading.Thread(target=receive_message, args=(child_conn, parent)).start()
#     while True:
#         msg = input("请输入消息：")
#         if msg:
#             child_conn.send(msg)


# def child(parent_conn):
#     threading.Thread(target=receive_message, args=(parent_conn, child)).start()
#     while True:
#         msg = input("请输入消息：")
#         if msg:
#             parent_conn.send(msg)


# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()
#     p = Process(target=child, args=(parent_conn, ))
#     p.start()
#     parent(child_conn)
import os
import time
import multiprocessing as mp


def child_process(child_pipe, parent_pipe):
    # 子进程循环读取管道中的数据并输出
    while True:
        # 接收来自父进程的消息
        if parent_pipe.poll():
            message = parent_pipe.recv()
            if message == "exit":
                break
            print("[Child Process] Received message from parent:", message)
        # 接收来自子进程的消息
        elif child_pipe.poll():
            message = child_pipe.recv()
            if message == "exit":
                break
            print("[Child Process] Received message from child:", message)
            # 将消息发送给父进程
            parent_pipe.send(message)


def main():
    # 创建父进程管道对象和子进程管道对象
    parent_pipe, child_pipe = mp.Pipe()

    # 创建子进程并将管道对象传递给子进程
    child_proc = mp.Process(target=child_process,
                            args=(child_pipe, parent_pipe))
    child_proc.start()

    # 父进程循环输入消息并发送给子进程
    while True:
        message = input(
            "[Parent Process] Please enter a message (type 'exit' to quit): ")
        parent_pipe.send(message)
        if message == "exit":
            break
        # 接收来自子进程的消息
        if parent_pipe.poll():
            message = parent_pipe.recv()
            if message == "exit":
                break
            print("[Parent Process] Received message from child:", message)

    # 等待子进程结束
    child_proc.join()

    # 关闭管道对象
    parent_pipe.close()
    child_pipe.close()


if __name__ == '__main__':
    main()
