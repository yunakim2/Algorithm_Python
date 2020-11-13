# L : 왼쪽으로 한칸
# R : 오른쪽으로 한칸
# U : 위로 한칸
# D : 아래로 한칸

n = int(input())

w = list(input().split())
num = [[1,1]]
for i in w :
    if i=='U' :
        num[0][0] -=1
        if num[0][0]>n or num[0][0]<1 : num[0][0] +=1
    if i=='D' :
        num[0][0] +=1
        if num[0][0]>n or num[0][0]<1 : num[0][0] -=1
    if i=='R' :
        num[0][1] +=1
        if num[0][1] > n or num[0][1]<1: num[0][1] -= 1
    if i=='L' :
        num[0][1] -=1
        if num[0][1] > n or num[0][1]<1: num[0][1] += 1


print(num[0][0],end=' ')
print(num[0][1])

