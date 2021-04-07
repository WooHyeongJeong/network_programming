from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 3333))
s.listen(5)
print('waiting...')

while True:
    client, addr = s.accept()
    print('connection from ', addr)
    while True:
        data = client.recv(1024)
        if not data:
            break

        formula = data.decode()
        f_list = formula.split(' ')

        try:
            if f_list[1] == '+':
                result = int(f_list[0]) + int(f_list[2])
            elif f_list[1] == '-':
                result = int(f_list[0]) - int(f_list[2])
            elif f_list[1] == '*':
                result = int(f_list[0]) * int(f_list[2])
            elif f_list[1] == '/':
                result = round(int(f_list[0]) / int(f_list[2]), 1)
        except:
            client.send(b'Try again') 
        else:
           
            bytes_str_result = str(result).encode()  
            client.send(bytes_str_result) 
    
    client.close()
s.close()
