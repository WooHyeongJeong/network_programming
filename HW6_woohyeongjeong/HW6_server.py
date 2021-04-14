from socket import *

s = socket()
s.bind(('', 80)) 
s.listen(10)
print('wait...')

while True:
    c, addr = s.accept() 

    data = c.recv(1024) 
    if not data:  
        break
    msg = data.decode() 
    req = msg.split('\r\n')  

    print('req[0] :', req[0])
    filename = req[0].split(' ')[1] 
    
    if '/' in filename:
        filename = filename.replace('/','') 

    print(filename)

    try:
        if filename == 'index.html':
            f = open(filename, 'r', encoding = 'utf-8')
            mimeType = 'text/html'

        elif filename == 'iot.png':
            f = open(filename, 'rb')
            mimeType = 'image/png' 

        elif filename == 'favicon.ico':
            f = open(filename, 'rb')
            mimeType = 'image/x-icon'

        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: ' + mimeType.encode() + b'\r\n')
        c.send(b'\r\n')
        data = f.read() 
        
        if filename == 'index.html':
            c.send(data.encode('utf-8')) 
        else:
            c.send(data)
        print(filename, 'send success!!')


    except:
        c.send(b'HTTP/1.1 404 Not Found\r\n')
        c.send(b'\r\n')
        c.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
        c.send(b'<BODY>Not Found</BODY></HTML>')
        print('Not Found')


    c.close()

s.close()