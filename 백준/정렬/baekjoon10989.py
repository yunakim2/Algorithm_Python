import sys

n = int(sys.stdin.readline())
l = [0] * 10000

for i in range(n) :
    l[int(sys.stdin.readline())-1] +=1


for j in range(10000) :
    if l[j]!=0 :
        for k in range(l[j]) :
             print(j+1)



