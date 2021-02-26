import itertools

n = int(input())
a = list(map(int,input().split()))
cnt = 0
for i in range(1,n+1):
    temp_combi = list(map(sum,itertools.combinations(a,i)))
    cnt += temp_combi.count(0)

print(cnt)
