num = int(input())

for i in range(num) :
    list = input()
    sum = 0
    cnt = 0
    for j in range(len(list)) :
        if list[j] =='O' :
            cnt+=1
            sum+=cnt
        else :
            cnt = 0

    print(sum)