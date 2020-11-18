n,m = map(int,input().split())

list_n = list(map(int, input().split()))

cnt = list_n.count(m)
if cnt == 0 : 
    print(-1)
else :
    print(cnt)