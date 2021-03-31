import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())

sock.send(b'HYEONGJEONG WOO')
bytes_num = sock.recv(1024)
num = int.from_bytes(bytes_num, 'big')
print(num)

sock.close()