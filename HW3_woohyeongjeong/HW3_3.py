str = input('문자열을 입력하세요: ')
str_dict = {}

str_list = str.split('&')
for i in str_list:
    str_dict[i.split("=")[0]] = i.split("=")[1]  
print(str_dict)