from collections import deque

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int,input().split())))


queue = deque([(N-1,0),(N-1,1), (N-2,1), (N-2,0)])
moving = {1: (0,-1), 2: (-1,-1), 3: (-1,0), 4: (-1,1), 5: (0,1), 6:(1,1), 7:(1,0), 8:(1,-1)}
side = [(-1,-1), (1,1), (-1,1), (1,-1)]

for _ in range(M):
    m,k = map(int, input().split())
    dx, dy = moving[m]
    check = set([])
    while queue:
        x, y = queue.popleft()
        x = (N + x + dx * k) % N
        y = (N + y + dy * k) % N
        board[x][y] += 1
        check.add((x, y))

    for x,y in check:
        cnt = 0
        for cx, cy in side:
            rx, ry = x + cx, y + cy
            if 0 <= rx < N and 0 <= ry < N:
                if board[rx][ry] > 0:
                    cnt += 1
        board[x][y] += cnt

    for i in range(N):
        for j in range(N):
            if (i,j) in check:
                continue
            if board[i][j] >= 2:
                board[i][j] -= 2
                queue.append((i,j))

ans = 0
for i in range(N):
    ans += sum (board[i])

print(ans)