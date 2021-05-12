from socket import *
import threading
import time

c_list = []  

port = 3333
BUFFSIZE = 1024


def chatting(sock, addr, id):

    while True:
        data = sock.recv(BUFFSIZE)

        if 'quit' in data.decode():
            if sock in c_list:
                print(addr, 'exited')
                c_list.remove(sock)
                break

        else:
            msg = id + ' ' + data.decode()
            for c_sock in c_list:
                if c_sock != sock:
                    c_sock.send(msg.encode())


s = socket()
s.bind(('', port))
s.listen(5)
print('Server Started')

while True:
    conn, addr = s.accept()
    print('new client', addr)


    if conn not in c_list:
        c_list.append(conn)

    id_msg = conn.recv(BUFFSIZE)
    if not id_msg:
        print('not id_msg')
        break

    for c_sock in c_list:
        if c_sock != conn:
            c_sock.send(id_msg)
    print(time.asctime() + str(addr) + ' : ' + id_msg.decode())


    th = threading.Thread(target=chatting, args=(conn, addr, id_msg.decode()))
    th.start()