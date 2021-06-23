from collections import deque


class cell:
    def __init__(self, access, power, active):
        self.access = access
        self.power = power
        self.active = active


def extendBoard(maps):
    extend_maps = [[cell(0, 0, 0) for _ in range(400)] for _ in range(400)]
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            extend_maps[i+200][j+200] = maps[i][j]

    return extend_maps


def active(queue, activeTime):
    dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    queue = deque(list(sorted(queue, key=lambda x: -x[0])))
    reQueue = []
    while queue:
        active, x, y = queue.popleft()
        for dx, dy in dxy:
            nx, ny = dx + x, dy + y
            if board[nx][ny].power == 0:
                board[nx][ny].power = active
                board[nx][ny].access = active + activeTime + 1
                board[nx][ny].active = active

        board[x][y].active -= 1
        if board[x][y].active > 0:
            reQueue.append((active, x, y))
        else:
            board[x][y].power = -1
            board[x][y].active = 0

    return reQueue


T = int(input())

for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = cell(board[i][j], board[i][j], board[i][j])
    board = extendBoard(board)
    time = 1

    queue = []
    while time < K:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j].access == time:
                    queue.append((board[i][j].power, i, j))
        reQueue = active(queue, time)
        if reQueue:
            queue = reQueue
        else:
            queue = []
        time += 1

    answer = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j].power != 0 and board[i][j].power != -1:
                answer += 1

    print("#{} {}".format(test_case, answer))
