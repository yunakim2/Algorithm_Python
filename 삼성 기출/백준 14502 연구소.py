from collections import deque
import copy
import sys

def bfs():
    global ans
    dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    check = [[False for _ in range(col)] for _ in range(row)]
    check_board = copy.deepcopy(board)
    queue = deque()
    for i in range(row):
        for j in range(col):
            if check_board[i][j] == 2:
                queue.append([i, j])
    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < row and 0 <= ny < col:
                if check_board[nx][ny] == 0 and not check[nx][ny]:
                    check_board[nx][ny] = 2
                    check[nx][ny] = True
                    queue.append([nx, ny])
    total = 0
    for i in check_board:
        total += i.count(0)
    ans = max(ans, total)


def dfs(cnt):
    if cnt == 3:
        bfs()
        return
    for i in range(row):
        for j in range(col):
            if board[i][j] == 0:
                board[i][j] = 1
                dfs(cnt + 1)
                board[i][j] = 0

if __name__ == '__main__':
    row, col = map(int, sys.stdin.readline().split())
    board = []
    for _ in range(row):
        board.append(list(map(int, sys.stdin.readline().split())))
    ans = 0
    dfs(0)
    print(ans)
