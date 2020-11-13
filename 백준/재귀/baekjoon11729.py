num = int(input())

def hanoi(n, froms, by, to, cnt) :
    if(n == 1) : print(str(froms)+" "+str(to))
    else:
        hanoi(n-1, froms,to,by, cnt)
        print(str(froms)+" "+str(to))
        hanoi(n-1,by,froms,to,cnt)


print(2**num-1)
hanoi(num,1,2,3,0)
