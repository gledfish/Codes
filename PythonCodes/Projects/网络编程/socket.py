import socket

# 1. 创建客户端socket对象
# 2. 和服务端socket建立连接
# 3. 发送数据
# 4. 接受数据
# 5. 关闭客户端socket


if __name__ == '__main__':
    # 创建客户端socket
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_client_socket.connect()