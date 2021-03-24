d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'}, {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'}, {'name':'Princess', 'phone':'555-3141', 'email':''}, {'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]

for i in d:
    j = list(i.values())
    if '8' in j[1]:
        print('전화번호가 8로 끝나는 사용자:', j[0])

for i in d:
    j = list(i.values())
    if '' == j[2]:
        print('이메일이 없는 사용자:', j[0])


name = input('사용자 이름을 입력하세요 : ')

names = []
d_list = []
for i in d:
    d_list.append(list(i.values()))
    a = list(i.values())
    names.append(a[0])

if name in names:
    print(d_list[names.index(name)])
else :
    print("이름이 없습니다.")

