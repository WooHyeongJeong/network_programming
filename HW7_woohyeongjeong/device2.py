from socket import *
import random
import time

BUF_SIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 7778))
sock.listen(3)
print('Device2:')

while True:
    try:
        conn, addr = sock.accept()
        while True:
            msg = conn.recv(BUF_SIZE)  
        
            if not msg:
                conn.close()
                continue

            elif msg == b'quit': 
                print('client:', addr, msg.decode())
                conn.close()
                continue

            elif msg == b'Request':
                print('client:', addr, msg.decode())
                conn.send(b'Successful Request!')
                conn.send(time.ctime(time.time()).encode())


            else:
                print('client:', addr, msg.decode())
                conn.send(b'Try again')
                continue
        
        
            heart_rate = random.randint(40, 140)        
            walking = random.randint(2000, 6000)         
            calorie = random.randint(1000, 4000) 
            msg = '{0} {1} {2}'.format(heart_rate, walking, calorie)
            conn.send(msg.encode())

    except:
        continue

    conn.close()
sock.close()
