from socket import *
import random
import time

BUF_SIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 7777))
sock.listen(3)
print('Device1:')

while True:
    try:
        conn, addr = sock.accept()
        while True:
            msg = conn.recv(BUF_SIZE)
            if not msg:
                conn.close()
                continue

            elif msg == b'quit': 
                print('Client:', addr, msg.decode())
                conn.close()
                continue

            elif msg == b'Request':
                print('Client:', addr, msg.decode())
                conn.send(b'Success!')
                conn.send(time.ctime(time.time()).encode())

            else:
                print('Client:', addr, msg.decode())
                conn.send(b'Try again')
                continue
        
        
            temperature = random.randint(0, 40)  
            humidity = random.randint(0, 100)  
            illuminance = random.randint(70, 150) 
            msg = '{0} {1} {2}'.format(temperature, humidity, illuminance)
            conn.send(msg.encode())

    except:
        continue

    conn.close()
sock.close()