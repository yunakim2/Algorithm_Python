n, k = map(int, input().split())
q = [i for i in range(1,n+1)]
print("<",end='')
i = 0
while len(q) > 1:
    if len(q) >= i+k-1:
        i = i+k-1
        if i<0:
            i +=1
    else:
        i = ((i+k) % len(q)) -1
        if i < 0:
            i+=k

    print(str(q.pop(i)), end=", ")

print("{}>".format(str(q.pop())))