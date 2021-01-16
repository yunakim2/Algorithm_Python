from collections import deque


def solution(m, n, infests, vaccinateds):
    check = [[False for _ in range(n)] for _ in range(m)]
    bfs_queue = deque()

    def available(x, y):
        return 0 <= x < m and 0 <= y < n

    def bfs(queue, answer):
        dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        count = answer
        while queue:
            item = queue.popleft()
            check[item[0]][item[1]] = True
            count = item[2]
            for dx, dy in dxy:
                new_x = int(dx) + int(item[0])
                new_y = int(dy) + int(item[1])
                if available(new_x, new_y) and not check[new_x][new_y] and [new_x + 1, new_y + 1] not in vaccinateds:
                    check[new_x][new_y] = True
                    queue.append([new_x,new_y, count+1])
                if available(new_x, new_y) and not check[new_x][new_y] and [new_x + 1, new_y + 1] in vaccinateds:
                    check[new_x][new_y] = True

        return count

    answer = 0
    for infest_x, infest_y in infests:
        bfs_queue.append([infest_x - 1, infest_y - 1, answer])
    answer = bfs(bfs_queue, answer)
    for check_row in check:
        for check_item in check_row:
            if not check_item:
                return -1
    else:
        return answer


if __name__ == '__main__':
    print(solution(2, 4, [[1, 4], [2, 2]], [[1, 2]]))
    print(solution(2, 3, [[2, 2]], [[1, 2], [2, 1]]))
    print(solution(2, 2, [[1, 1], [2, 2]], [[1, 2], [2, 1]]))
