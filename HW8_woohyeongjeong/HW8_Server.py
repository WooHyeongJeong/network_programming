from socket import *
from collections import defaultdict

BUFF_SIZE = 1024
port = 5555

s = socket(AF_INET, SOCK_DGRAM)  
s.bind(('', port)) 
print('Wait...')

dic = defaultdict(list)


while True:
    data, addr = s.recvfrom(BUFF_SIZE) 
    msg = data.decode()
    msg_list = msg.split(' ', maxsplit=2)

    if 'send' == msg_list[0]:
        dic[msg_list[1]].append(msg_list[2]) 
        print(dic) 
        s.sendto(b'OK', addr) 

    elif 'receive' == msg_list[0]: 
        try:
            recv_msg = dic[msg_list[1]][0] 
            s.sendto(recv_msg.encode(), addr)
            del dic[msg_list[1]][0]
            print(dic) 
        except:
            print('No messages')
            s.sendto(b'No messages', addr)


    elif 'quit' == msg_list[0]:
        print('quit')
        break

    else:
        print('It is wrong. Try again')
        s.sendto(b'Try again', addr)
