from collections import deque


def move(x, y, dx, dy):
    cnt = 0
    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt


def bfs(rx,ry,bx,by):
    queue = deque()
    queue.append((rx, ry, bx, by,1))
    visited[rx][ry][bx][by] = True
    dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    while queue:
        rx, ry, bx, by,depth = queue.popleft()
        if depth > 10:
            break
        for dx, dy in dxy:
            new_rx, new_ry, rcnt = move(rx, ry, dx, dy)
            new_bx, new_by, bcnt = move(bx, by, dx, dy)

            if board[new_bx][new_by] != 'O':
                if board[new_rx][new_ry] == 'O':
                    return depth
                if new_rx == new_bx and new_ry == new_by:
                    if rcnt > bcnt:
                        new_rx -= dx
                        new_ry -= dy
                    else:
                        new_bx -= dx
                        new_by -= dy
                if not visited[new_rx][new_ry][new_bx][new_by]:
                    visited[new_rx][new_ry][new_bx][new_by] = True
                    queue.append((new_rx, new_ry, new_bx, new_by,depth+1))
    return -1


if __name__ == '__main__':
    row, col = map(int, input().split())
    board = [list(input().strip()) for _ in range(row)]
    visited = [[[[False] * col for _ in range(row)] for _ in range(col)] for _ in range(row)]

    for i in range(row):
        for j in range(col):
            if board[i][j] == 'R':
                rx,ry = i,j
            if board[i][j] == 'B':
                bx,by = i,j

    print(bfs(rx,ry,bx,by))
