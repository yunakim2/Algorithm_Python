from collections import deque


def solution(n, m, image):
    answer = 0
    check = [[0 for _ in range(m)] for _ in range(n)]

    def bfs(x, y):
        dxy = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        queue = deque([(x, y)])
        while queue:
            item = queue.popleft()
            for xy in dxy:
                new_x = int(item[0] + xy[0])
                new_y = int(item[1] + xy[1])
                if 0 <= new_x < n and 0 <= new_y < m and check[new_x][new_y] != 1:
                    if image[new_x][new_y] == image[item[0]][item[1]]:
                        queue.append((new_x, new_y))
                        check[new_x][new_y] = 1
        return 1

    for i in range(n):
        for j in range(m):
            if check[i][j] != 1:
                answer += bfs(i, j)

    return answer


if __name__ == '__main__':
    # print(solution(4, 4,[[1,1,2,3],[1,1,4,4],[3,3,2,2],[1,1,1,1]]))
    print(solution(5, 5, [[1, 1, 1, 2, 4], [2, 1, 3, 2, 4], [3, 1, 3, 2, 4], [4, 1, 2, 2, 3], [5, 1, 1, 1, 1]]))
