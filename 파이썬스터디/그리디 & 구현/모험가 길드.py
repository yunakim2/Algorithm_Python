n = int(input())
s = list(map(int, input().split()))
s = sorted(s)

cnt =0
group = 0
for i in s :
    group +=1
    if group >= i :
        cnt += 1
        group = 0

print(cnt)