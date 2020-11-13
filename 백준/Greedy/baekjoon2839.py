n = int(input())
n2 = n
cnt = 0
cnt2 =0
while n>=3 :
    # print(f"n1 = {n} cnt ={cnt}")
    if n % 5 == 0  or n >5:
        n = n - 5
        cnt +=1

    else:
        n = n-3
        cnt +=1

while n2>=3 :
    # print(f"n2 = {n2} cnt2 ={cnt2}")
    if n2%3 == 0 or n2>3  :
        if n2%5 == 0 :
            n2 = n2 - 5
            cnt2 +=1
        else :
            n2 = n2 - 3
            cnt2 +=1
    else :
        n2 = n2-5
        cnt2 +=1

# print(f"n2 = {n2} cnt2 ={cnt2}")
if n == 0 or n2 == 0:
    if n==0 and n2 ==0 :
        print(min(cnt,cnt2))
    elif n==0 :
        print(cnt)
    else :
        print(cnt2)
else : print("-1")