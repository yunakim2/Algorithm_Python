from collections import deque


def check_board(borad):
    queue = deque()
    tmp_board = [[0]*col for _ in range(row)]

    for i in range(row):
        for j in range(col):
            tmp_board[i][j] = borad[i][j]
            if borad[i][j] == 2:
                queue.append((i, j))

    dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < row and 0 <= ny < col and tmp_board[nx][ny] == 0:
                tmp_board[nx][ny] = 2
                queue.append((nx,ny))

    cnt = 0
    for i in tmp_board:
        cnt += i.count(0)

    return cnt


def bfs():
    global ans
    for i in range(row):
        for j in range(col):
            if board[i][j] != 0:
                continue
            for i2 in range(row):
                for j2 in range(col):
                    if board[i2][j2] != 0:
                        continue
                    for i3 in range(row):
                        for j3 in range(col):
                            if board[i3][j3] != 0:
                                continue
                            if i == i2 and j == j2:
                                continue
                            if i2 == i3 and j2 == j3:
                                continue
                            if i == i3 and j == j3:
                                continue

                            board[i][j] = 1
                            board[i2][j2] = 1
                            board[i3][j3] = 1
                            ans = max(ans, check_board(board))
                            board[i][j] = 0
                            board[i2][j2] = 0
                            board[i3][j3] = 0


if __name__ == '__main__':
    row, col = map(int, input().split())
    board = []
    for _ in range(row):
        board.append(list(map(int, input().split())))
    ans = 0
    bfs()
    print(ans)
