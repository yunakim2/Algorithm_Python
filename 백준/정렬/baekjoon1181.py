import sys

n = int(sys.stdin.readline())
l = []

for i in range(n) :
    l.append(sys.stdin.readline().rstrip('\n'))

l = list(set(l))
l.sort(key = lambda  x : (len(x), x))

for j in  l :
    print(j)