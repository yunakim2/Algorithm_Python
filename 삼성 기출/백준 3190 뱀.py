from collections import deque


def change_direction(d, check):
    if check == 'D':
        d = (d + 1) % 4
    else:
        d = (d - 1) % 4
    return d


def boundary_check(x, y):
    return True if 0 <= x < n and 0 <= y < n else False


def dummy_game():
    dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    timer = 0
    nx, ny = 0, 0
    d = 1
    while True:
        timer += 1
        nx += dxy[d][0]
        ny += dxy[d][1]
        if timer in move.keys():
            d = change_direction(d, move[timer])

        if boundary_check(nx, ny):
            if [nx, ny] in snake:
                break
            if board[nx][ny] == 1:
                board[nx][ny] = 0
                snake.append([nx, ny])
            elif board[nx][ny] == 0:
                snake.append([nx, ny])
                snake.popleft()
        else:
            break
    return timer


if __name__ == '__main__':
    n = int(input())
    board = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(int(input())):
        row, col = map(int, input().split())
        board[row - 1][col - 1] = 1

    move = {}
    for _ in range(int(input())):
        x,y = input().split()
        move[int(x)] = y
    snake = deque([[0, 0]])
    print(dummy_game())
