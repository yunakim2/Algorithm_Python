import sys

a = int(input())

for b in range(a) :
    c,d = map(int,sys.stdin.readline().split())
    print(c+d)