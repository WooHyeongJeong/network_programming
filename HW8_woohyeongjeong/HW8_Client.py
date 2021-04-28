from socket import *

BUFF_SIZE = 1024
port = 5555

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('Enter the message("send mboxID message" or "receive mboxID"): ')
    sock.sendto(msg.encode(), ('localhost', port))
    if msg == 'quit':
        break
    
    
    data, addr = sock.recvfrom(BUFF_SIZE)
    print('-> ', data.decode())
