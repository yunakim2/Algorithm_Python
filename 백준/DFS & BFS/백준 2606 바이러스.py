from collections import deque


def bfs(n, v):
    l = deque()
    l.append(v)
    answer = 0
    checkbfs[v] = 1
    while l:
        answer += 1
        n1 = l.popleft()
        for i in range(n):
            if num[n1][i] == 1 and checkbfs[i] != 1:
                l.append(i)
                checkbfs[i] = 1
    return answer - 1


n = int(input())
m = int(input())
checkbfs = [0 for i in range(n)]
num = [[0 for col in range(n)] for row in range(n)]
for i in range(m):
    n1, m1 = map(int, input().split())
    num[n1 - 1][m1 - 1] = 1
    num[m1 - 1][n1 - 1] = 1

print(bfs(n, 0))
