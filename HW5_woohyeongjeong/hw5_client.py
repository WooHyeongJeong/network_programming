from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 3333))

def changeStr(str_num):
    if '.' in str_num:
        return float(str_num)
    else:
        return int(str_num)

while True: 
    formula = input('Write Number(ex. 20 + 17): ')
    if formula == 'q': 
        break

    s.send(formula.encode())

    bytes_str_result = s.recv(1024)
    if not bytes_str_result:
        break

    str_result = bytes_str_result.decode()
    try:
        print('Total: ', changeStr(str_result)) 
    
    except:
        print('Try again: ', str_result) 

s.close()

