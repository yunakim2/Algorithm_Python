def selfnum(num) :
    sum = num
    while(True) :
        if(num==0) : break
        sum = sum+num%10
        num = num//10

    return sum

n = 10001
data = [False for i in range(n)]
for i in range(n) :
    cnt = selfnum(i)
    if (cnt<n) : data[cnt] = True

for i in range(n) :
    if not data[i]:
        print(i)





