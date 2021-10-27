from collections import deque
import heapq

N, M, S = map(int, input().split())
board = []

for _ in range(N):
    board.append(list(map(int, input().split())))

cx, cy = map(int, input().split())
cx -= 1
cy -= 1

person = deque([])
item = deque([])

for _ in range(M):
    x, y, dx, dy = map(int, input().split())
    person.append([x - 1, y - 1, dx - 1, dy - 1])
    item.append((x-1,y-1))
    board[x-1][y-1] = 2

dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def checking(cx, cy, person):
    ans = []
    que = deque([(cx,cy,0)])
    visited = [[False for _ in range(N)] for _ in range(N)]
    while que:
        x,y,m = que.popleft()
        if board[x][y] == 2:
            heapq.heappush(ans, (m, x, y))
        for dx, dy in dxy:
            rx,ry = dx +x , dy+y
            if 0 <= rx < N and 0 <= ry < N and not visited[rx][ry] and board[rx][ry] != 1:
                if m+1 <=S:
                    visited[rx][ry] = True
                    que.append((rx,ry,m+1))
    if ans:
        return ans[0][0], ans[0][1], ans[0][2]
    else:
        return -1, -1, -1


def moving(sx, sy, ex, ey):
    start = deque([(sx, sy, 0)])
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[sx][sy] = True
    while start:
        x, y, m = start.popleft()
        if x == ex and y == ey:
            return m
        for dx, dy in dxy:
            rx, ry = x + dx, y + dy
            if 0 <= rx < N and 0 <= ry < N and not visited[rx][ry] and board[rx][ry] != 1:
                if m + 1 <= S:
                    visited[rx][ry] = True
                    start.append((rx, ry, m + 1))
    return -1


while person and S > 0:
    ms, x,y= checking(cx, cy, person)
    if ms == -1:
        S = -1
        break
    idx = item.index((x, y))
    sx, sy, ex, ey = person[idx]
    S -= ms
    if S < 0:
        break
    move = moving(sx, sy, ex, ey)
    if move == -1:
        S = -1
        break
    S -= move
    S += move * 2
    cx, cy = ex, ey
    board[x][y] = 0
    del person[idx]
    del item[idx]

if S < 0:
    S = -1
if person:
    S = -1
print(S)
