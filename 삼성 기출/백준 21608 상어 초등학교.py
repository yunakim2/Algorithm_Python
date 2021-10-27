from collections import deque


def check(mem):
    checking = deque([])
    for i in range(N):
        for j in range(N):
            if res[i][j] in board[mem]:
                checking.append((i, j))

    calculator = []
    tmp_cal = deque([])
    while checking:
        x, y = checking.popleft()
        for dx, dy in dxy:
            if 0 <= x + dx < N and 0 <= y + dy < N and res[x + dx][y + dy] == 0 and (x + dx, y + dy) not in tmp_cal:
                tmp_cal.append((x + dx, y + dy))
    while tmp_cal:
        x, y = tmp_cal.popleft()
        tmp = 0
        tmp2 = 0
        for dx, dy in dxy:
            if 0 <= x + dx < N and 0 <= y + dy < N:
                if res[x + dx][y + dy] == 0:
                    tmp += 1
                if res[x + dx][y + dy] in board[mem]:
                    tmp2 += 1
        calculator.append((x, y, tmp2, tmp))

    if not calculator:
        for k in range(N):
            for l in range(N):
                if res[k][l] == 0:
                    tmp = 0
                    for dx, dy in dxy:
                        if 0 <= k + dx < N and 0 <= l + dy < N and res[k + dx][l + dy] == 0:
                            tmp += 1
                    calculator.append((k, l, 0, tmp))

    ans = sorted(calculator, key=lambda x: (-x[2], -x[3], x[0], x[1]))
    return ans[0][0], ans[0][1]


N = int(input())
board = dict()
res = [[0 for _ in range(N)] for _ in range(N)]
answer = 0
dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]

for _ in range(N * N):
    tmp = list(map(int, input().split()))
    board[tmp[0]] = tmp[1::]

for i in board.keys():
    rx, ry = check(i)
    res[rx][ry] = i

for x in range(N):
    for y in range(N):
        tmp = 0
        for dx, dy in dxy:
            if 0 <= x + dx < N and 0 <= y + dy < N and res[x + dx][y + dy] in board[res[x][y]]:
                tmp += 1
        answer += int(10 ** (tmp - 1))

print(answer)
