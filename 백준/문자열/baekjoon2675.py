num = int(input())

for i in range(num) :
    size , lists = input().split()
    lists = list(lists)

    for k in range(0, len(lists)) :
        for j in range(int(size)) :
            print(lists[k], end='')

    print("")
