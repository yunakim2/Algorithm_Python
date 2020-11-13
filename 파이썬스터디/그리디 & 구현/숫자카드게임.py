import time
start_time = time.time() # 측정 시작

n,m = map(int, input().split(' '))

cards = [[0]*m ]*n

for i in range(0,n) :
    temp = list(map(int,input().split(' ')))
    cards[i] = temp

min_list = [0]*n
for i in range(0, n) :
    min_list[i] = min(cards[i])

print(max(min_list))

end_time = time.time() # 측정 종료
print("time:", end_time - start_time) # 수행 시간 출력
