
from collections import deque

def popBoard (i, board):
    for j in range(H):
        if board[j][i] != 0:
            break
    dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    pops = deque([(j,i)])
    while pops:
        j,i = pops.popleft()
        k = board[j][i]
        if k == 1:
            board[j][i] = 0
            continue

        board[j][i] = 0
        for s in range(1,k):
            for dx, dy in dxy:
                x ,y = i + dx * s , j + dy * s
                if 0 <= x < H and 0 <= y < W and board[x][y] != 0:
                    pops.append((x,y))

    for i in range(W):
        for j in range(H-1, 0, -1):
            if board[j][i] == 0:
                board[j][i] , board[j-1][i] = board[j-1][i], board[j][i]

    for i in range(H):
        for j in range(W):
            print(board[i][j], end= ' ')
        print()
    return board


def dfs(n, board):
    global ans
    if n == N:
        cnt = 0
        for i in range(W):
            for j in range(H):
                if board[j][i] != 0 :
                    cnt += 1
        if ans >= cnt:
            ans = cnt
            print(ans)
        print()
        return

    for i in range(W):
        m_board = []
        for j in range(H):
            m_board.append(board[i])
        board = popBoard(i, board)
        dfs(n+1, board)
        board = m_board



T = int(input())
for _ in range(T):
    N, W, H = map(int, input().split())
    board = []
    for _ in range(H):
        board.append(list(map(int, input().split())))

    ans = 1000000000
    dfs(0, board)
    print(ans)