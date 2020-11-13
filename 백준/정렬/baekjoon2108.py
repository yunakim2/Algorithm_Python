# 통계학
import sys
from collections import Counter

n = int(sys.stdin.readline())
l = []
for i in range(n) :
    l.append(int(sys.stdin.readline()))

print(int(round(sum(l)/len(l),0)))
l.sort()
print(l[n//2])
if n == 1 :
    print(l[0])
else :
    mode = Counter(l).most_common(n=2)
    if(mode[0][1] == mode[1][1]) :
        print(mode[1][0])
    else :
        print(mode[0][0])

print(l[-1] -l[0])