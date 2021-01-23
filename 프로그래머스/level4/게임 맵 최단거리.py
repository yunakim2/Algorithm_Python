from collections import deque


def solution(maps):
    answer = 0
    ROW = len(maps)
    COL = len(maps[0])
    check_maps = [[False for _ in range(COL)] for _ in range(ROW)]

    def available(x, y):
        return 0 <= x < ROW and 0 <= y < COL

    def bfs(x, y):
        count = 1
        dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        queue = deque([[x, y, count]])
        check_maps[x][y] = True
        while queue:
            x, y, count = queue.popleft()
            if x == ROW - 1 and y == COL - 1:
                return count
            for dx, dy in dxy:
                new_x, new_y = x + dx, y + dy
                if available(new_x, new_y) and not check_maps[new_x][new_y]:
                    if maps[new_x][new_y] == 1:
                        queue.append([new_x, new_y, count + 1])
                        check_maps[new_x][new_y] = True
        return -1

    return bfs(0, 0)


if __name__ == "__main__":
    print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
    print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))
