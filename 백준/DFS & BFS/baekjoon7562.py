# 나이트의 이동
from collections import deque


def bfs(init_x, init_y , res_x, res_y):
    dx = [-2, -1, +1, +2, -2, -1, +1, +2]
    dy = [-1, -2, -2, -1, +1, +2, +2, +1]

    queue = deque()
    queue.append((init_x, init_y))
    graph[init_x][init_y] = 1
    while queue:
        x, y = queue.popleft()
        if x == res_x and y == res_y:
            return graph[x][y] -1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            else :
                if graph[nx][ny] == 0 :
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx, ny))




case = int(input())
for i in range(case) :
    # 체스판 크기
    n = int(input())
    init_x , init_y = map(int,input().split())
    res_x , res_y = map(int,input().split())
    graph = [[0 for _ in range(n)] for _ in range(n)]
    if init_x == res_x and init_y == res_y :
        print(0)
    else :
        print(bfs(init_x,init_y,res_x,res_y))







