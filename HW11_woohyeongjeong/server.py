from socket import *
import select
import threading
import time

c_list = []   
id_list = [] 

port = 3333
BUFFSIZE = 1024
       
s_sock = socket()
s_sock.bind(('', port))
s_sock.listen(5)

c_list.append(s_sock) 
print(str(port) + '대기')

while True:
    r_sock, w_sock, e_sock = select.select(c_list, [], [])

    for s in r_sock:
        if s == s_sock:
            c_sock, addr = s_sock.accept()
            print('Client ({}) connected'.format(addr))
            c_list.append(c_sock)

            id_msg = c_sock.recv(BUFFSIZE)
            if not id_msg:
                print('not id_msg')
                break
            print(time.asctime() + str(addr) + ' : ' + id_msg.decode())
            
             
            for i in range(1, len(c_list)):
                    if c_list[i] != c_sock:
                        c_list[i].send(id_msg)
            c_tupple = (c_sock, id_msg)
            id_list.append(c_tupple)

        else:
            data = s.recv(BUFFSIZE)
            if not data:
                s.close()
                c_list.remove(s)
                continue
           
            if 'quit' in data.decode():
                if s in c_list:
                    print(addr, 'exited')
                    c_list.remove(s)
                    break
            
            else:
                for i in range(len(id_list)):
                    if s == id_list[i][0]:
                        msg = id_list[i][1].decode() + ' ' + data.decode()
                        print(time.asctime() + str(addr) + ' :' , msg)
                      
                for i in range(1, len(c_list)):
                    if c_list[i] != s:
                        c_list[i].send(msg.encode())
                
