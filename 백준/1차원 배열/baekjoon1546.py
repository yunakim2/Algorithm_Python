num = int(input())
list = list(map(int,input().split()))

max = max(list)
sum =0

for i in range(num) :
    list[i] = list[i]/max*100
    sum += list[i]

print(sum/num)


