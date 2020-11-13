n = int(input())

cnt = 0
for i in range(n+1) :
    for j in range(60) :
        for k in range(60) :
            h = str(i)
            m = str(j)
            s = str(k)

            if h.find('3')!=-1 or m.find('3')!=-1 or s.find('3')!=-1:
                cnt +=1


print(cnt)