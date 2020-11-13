import sys

n = int(sys.stdin.readline())
l = []

for i in range(n) :
   l.append(list(sys.stdin.readline().split()))
   l[i][0] = int(l[i][0])


l.sort(key = lambda  x : (x[0]))

for j in l :
    print(j[0],j[1])