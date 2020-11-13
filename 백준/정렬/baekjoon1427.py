import sys

n = str(sys.stdin.readline())
l = [i for i in n]
l.remove('\n')
l = sorted(l,reverse=True)

print(''.join(l))
