n = int(input())
cnt = n
for i in range(0,n) :
    str = input()
    alpha = [0 for i in range(26)]
    j = 0
    flag = 0
    while j<len(str) :
        temp = ord(str[j])-97
        if(alpha[temp] == 0 ) :
            alpha[temp] = 1
            flag = temp
        else :
            if(flag!=temp) :
                cnt = cnt -1
                break

        j= j+1


print(cnt)