import collections
a,b,c = map(int,input().split())
n = int(input())

cable = []

for _ in range(n):
    cable.append(list(map(int,input().split())))

cable.sort(key= lambda k: k[0])
cable = collections.deque(cable)
price = 0
cnt = 0
while cable:
    p, type = cable.popleft()
    if type == 0:
        if a>0:
            a-=1
            price += p
            cnt += 1
        elif c>0:
            c-=1
            price += p
            cnt += 1
    else:
        if b>0:
            b-=1
            price += p
            cnt += 1
        elif c>0:
            c-=1
            price += p
            cnt += 1



print(cnt, price)





