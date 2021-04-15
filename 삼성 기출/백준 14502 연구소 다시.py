from collections import deque

def check_board(borad):
    visited_board = [[False for _ in range(col)] for _ in range(row)]
    dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for i in range(row):
        for j in range(col):
            if borad[i][j] == 2:
                for dx, dy in dxy:
                    nx, ny = i+dx, j+dy
                    if 0<= nx <col and 0<= ny < col and not visited_board[nx][ny]:
                        borad[dx][dy] = 2
                        visited_board[dx][dy] = True
            else:
                visited_board[i][j] = True
    cnt = 0
    for i in range(row):
        if visited_board[i] in False:
            return 0
        cnt += borad[i].count(0)
    return cnt

def bfs(x,y):
    global ans
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True

    while queue:
        x,y = queue.popleft()
        for _ in range(2):
            for i in range(row):
                for j in range(col):
                    nx,ny = x+i, y+j
                    if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny]:
                        if board[nx][ny] == 1 or board[nx][ny] == 2:
                            visited[nx][ny] = True
                            continue
                        queue.popleft((nx,ny))
                        board[nx][ny] = 1
                        visited[nx][ny] = True
        ans = max(ans,check_board(board))




if __name__ == '__main__':
    row, col = map(int, input().split())
    board = []
    visited = [[False for _ in range(col)] for _ in range(row)]
    print(visited)
    for _ in range(row):
        board.append(list(map(int, input().split())))
    ans = 0
    bfs(0,0)
    print(ans)