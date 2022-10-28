import socket

sockfd = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sockfd.bind(('0.0.0.0',12345))
sockfd.listen(5)

while True:

    print('waiting')
    try:
        connfd,addr = sockfd.accept()

        print('connect from',addr)
    except KeyboardInterrupt:
        print('exit')

    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print("收到：",data.decode())
        m = 'thank'

        n = connfd.send(m.encode())

        print('发送%d'%n)
    connfd.close()

sockfd.close()

