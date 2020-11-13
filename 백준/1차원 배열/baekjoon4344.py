num = int(input())

for i in range(num) :
    data = list(map(int, input().split(' ')))
    cnt = data[0]
    del data[0]
    avg = sum(data) / cnt
    k = 0
    for j in range(cnt) :
        if(data[j]>avg) :
            k+=1

    print("%.3f"%round((k/cnt*100),3)+"%")