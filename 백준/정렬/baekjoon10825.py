import sys
n = int(sys.stdin.readline())

arr = []
for i in range(n) :
    arr.append(sys.stdin.readline().split())

arr.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))


for j in range(n) :
    print(arr[j][0])