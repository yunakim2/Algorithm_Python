from collections import deque
import sys


def bfs(queue):
    dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    while queue:
        item = queue.popleft()
        answer = item[2]
        check[item[0]][item[1]] = True
        for dx, dy in dxy:
            new_x = int(dx) + int(item[0])
            new_y = int(dy) + int(item[1])
            if 0 <= new_x < m and 0 <= new_y < n and not check[new_x][new_y]:
                if tomato[new_x][new_y] == 0:
                    check[new_x][new_y] = True
                    queue.append([new_x, new_y, answer + 1])
    return answer


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    check = [[False for _ in range(n)] for _ in range(m)]
    tomato = []
    answer = 0
    queue = deque()
    for _ in range(m):
        tomato.append(list(map(int, sys.stdin.readline().split())))

    for row in range(m):
        for col in range(n):
            if tomato[row][col] == 1:
                queue.append([row, col, answer])
            elif tomato[row][col] == -1:
                check[row][col] = True
    answer = bfs(queue)
    for row in range(m):
        for col in range(n):
            if not check[row][col]:
                answer = -1

    print(answer)
