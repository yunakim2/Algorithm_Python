a = int(input())

for b in range(a) :
    c,d = map(int,input().split())
    print("Case #%s: %s + %s = %s"%(b+1,c,d, c+d ))
