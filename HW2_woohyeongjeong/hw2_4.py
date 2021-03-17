num = range(1, 1001)

for i in range(1, 1001):
    sum = 0
    s = str(i)
    
    for j in s:
        sum += int(j)
    
    print(i, ' Sum: ' , sum)