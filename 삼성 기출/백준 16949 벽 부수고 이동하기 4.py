from collections import deque

def bfs(x,y, group_number):
    queue = deque()
    queue.append((x,y))
    group_board[x][y] = group_number
    visited[x][y] = True
    cnt = 1
    while queue:
        x,y = queue.popleft()
        for dx,dy in dxy:
            nx,ny = dx+x, dy+y
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if board[nx][ny] == 0:
                    queue.append((nx,ny))
                    visited[nx][ny] = True
                    group_board[nx][ny] = group_number
                    cnt += 1

    return cnt


if __name__ == '__main__':
    N,M = map(int,input().split())
    board = []
    group_board = [[0]* M for _ in range(N)]
    group_size = {}
    group_number = 0
    dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    for _ in range(N):
        board.append(list(map(int,list(input()))))


    visited = [[False] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0 and not visited[i][j]:
                group_size[group_number] = bfs(i,j,group_number)
                group_number += 1

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                print(0, end='')
                continue
            else:
                tmp_group = set()
                size = 1
                for x,y in dxy:
                    nx,ny = x+i, y+j
                    if 0 <= nx < N and 0 <= ny < M:
                        if board[nx][ny] == 0:
                            tmp_group.add(group_board[nx][ny])
                for tmp in tmp_group:
                    size += group_size[tmp]
                print(size%10,end='')

        print()