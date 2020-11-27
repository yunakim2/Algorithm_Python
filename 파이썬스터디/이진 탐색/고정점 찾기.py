n = int(input())

list_n = list(map(int, input().split()))
cnt = 0
for i in range(len(list_n)):
    if list_n[i] == i:
        print(i)
        cnt = 1
        break

if cnt ==0 :
    print(-1)


