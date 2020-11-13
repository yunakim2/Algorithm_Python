import sys

n = int(sys.stdin.readline())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))

l = list(set(l))
l.sort()

for j in l :
    print(j)