a = list(map(int,input().split()))
mid = 0

if a[0]>=a[1] :
    if a[1]>=a[2] :
        mid = a[1]
    else :
        if a[0]>= a[2] :
            mid = a[2]
        else : mid = a[0]
else :
    if a[0]>=a[2] : mid = a[0]
    else :
        if a[1]>=a[2] :
            mid = a[2]
        else : mid = a[1]

print(mid)