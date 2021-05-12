from socket import *
import threading

BUFFSIZE = 1024
server_addr = ('localhost', 3333)

def recv_(sock):
    while True:

        msg = sock.recv(BUFFSIZE)
        print(msg.decode())

sock = socket()
sock.connect(server_addr)

my_id = input('id를 입력하세요: ')
sock.send(('[' + my_id + ']').encode())

while True:  

    th = threading.Thread(target=recv_, args=(sock,))
    th.daemon = True
    th.start()


    data = input()
    sock.send(data.encode())
    if 'quit' == data:
        break

sock.close()