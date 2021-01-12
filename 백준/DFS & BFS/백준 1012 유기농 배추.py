import sys
from collections import deque


def bfs(x, y):
    dxy = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    queue = deque([(x, y)])
    while queue:
        item = queue.popleft()
        for xy in dxy:
            new_x = int(item[0] + xy[0])
            new_y = int(item[1] + xy[1])
            if 0 <= new_x < m and 0 <= new_y < n and check[new_x][new_y] != 1:
                if maps[new_x][new_y] == maps[item[0]][item[1]]:
                    queue.append((new_x, new_y))
                    check[new_x][new_y] = 1

    return 1


number = int(input())
for _ in range(number):
    m, n, k = map(int, sys.stdin.readline().split())
    maps = [[0 for _ in range(n)] for _ in range(m)]
    check = [[0 for _ in range(n)] for _ in range(m)]
    answer = 0
    for _ in range(k):
        i, j = map(int,sys.stdin.readline().split())
        maps[i][j] = 1

    for i in range(m):
        for j in range(n):
            if maps[i][j] != 0:
                if check[i][j] != 1:
                    answer += bfs(i, j)

    print(answer)
