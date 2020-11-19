n,m = map(int, input().split())
house = []
for i in range(n) :
    house.append(int(input()))


house.sort()
# 최소
start = house[1] - house[0]
# 최대
end = house[-1] - house[0]

res =0
while(start<=end) :
    mid = (start+end)//2
    old = house[0]
    count = 1
    for i in range(1,len(house)) :
        if house[i]>= old+mid :
            count+=1
            old = house[i]
    if count>= m :
        start = mid+1
        res = mid
    else :
        end = mid-1

print(res)

