s = input()
s = list(s)
cnt =0
for i in s :
    if cnt ==0 :
        cnt = int(i)
    else :
        temp1 = cnt * int(i)
        temp2 = cnt + int(i)
        if temp1>temp2 :
            cnt = temp1
        else :
            cnt = temp2

print(cnt)