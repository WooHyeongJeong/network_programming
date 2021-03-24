days = {'January': 31, 'February': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}

m = input('월을 입력하세요: ')
print(days[m])

print(sorted(days))

for key, value in days.items():
    if value == 31:
        print(key, ":", value)


print(sorted(days.items(), key = lambda t: t[1]))

n = input('월의 알파벳 앞 3자리만 입력하세요 : ')
for key in days.keys():
    if n in key:
        print(days[key])