from collections import deque
from sys import stdin


def bfs(x, y):
    dxy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = deque([(x, y)])
    while queue:
        item = queue.popleft()
        for xy in dxy:
            new_x = int(xy[0] + item[0])
            new_y = int(xy[1] + item[1])
            if 0 <= new_x < n and 0 <= new_y < m and check[new_x][new_y] != 1 and maps[new_x][new_y] == '1':
                queue.append((new_x, new_y))
                maps[new_x][new_y] = int(maps[item[0]][item[1]]) + 1
                check[new_x][new_y] = 1


n, m = map(int, stdin.readline().split())
check = [[0 for _ in range(m)] for _ in range(n)]
maps = []

for _ in range(n):
    tmp_map = list(stdin.readline())
    tmp_map.remove('\n')
    maps.append(tmp_map)

bfs(0, 0)
print(maps[n - 1][m - 1])
