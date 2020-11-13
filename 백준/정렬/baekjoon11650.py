import sys

n = int(sys.stdin.readline())
l = []
for i in range(n) :
    l.append(list(map(int,sys.stdin.readline().split())))


l.sort(key = lambda  x : (int(x[0]), int(x[1])))

for j in range(n) :
    print(l[j][0], l[j][1])