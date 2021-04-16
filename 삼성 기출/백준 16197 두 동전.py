from collections import deque
def bfs():
    coin = deque()
    tmp = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'o':
                tmp.append([i, j])

    dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    coin.append((tmp[0][0], tmp[0][1], tmp[1][0], tmp[1][1], 0))

    while coin:
        x1, y1, x2, y2, cnt = coin.popleft()
        if cnt >= 10:
            return -1
        for dx, dy in dxy:
            nx1, ny1 = x1 + dx, y1 + dy
            nx2, ny2 = x2 + dx, y2 + dy
            if 0 <= nx1 < n and 0 <= ny1 < m and 0 <= nx2 < n and 0 <= ny2 < m:
                if board[nx1][ny1] == '#':
                    nx1, ny1 = x1, y1
                if board[nx2][ny2] == '#':
                    nx2, ny2 = x2, y2
                coin.append((nx1, ny1, nx2, ny2, cnt + 1))

            elif 0 <= nx1 < n and 0 <= ny1 < m:  # coin2가 떨어진 경우
                return cnt + 1

            elif 0 <= nx2 < n and 0 <= ny2 < m:  # coin1가 떨어진 경우
                return cnt + 1
            else:  # 둘 다 빠진 경우 무시
                continue
    return -1


if __name__ == '__main__':
    n, m = map(int, input().split())
    board = []
    for i in range(n):
        board.append(list(input()))

    print(bfs())
