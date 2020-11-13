n = int(input())
time = list(map(int,input().split()))
time.sort()
times = []
cnt =0

for i in time :
    cnt = i+cnt
    times.append(cnt)

print(sum(times))