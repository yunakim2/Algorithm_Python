def solution(n, m, image):
    answer = 0
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    check = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for x, y in zip(dx, dy):
                new_x = int(i + x)
                new_y = int(j + y)
                if 0 <= new_x < n and 0 <= new_y < m:
                    if not check[new_x][new_y]:
                        check[new_x][new_y] = 1
                        if image[i][j] == image[new_x][new_y] and not check[i][j]:
                            break
            else:
                answer += 1

    return answer


print(solution(3, 2, [[1, 2], [1, 2], [4, 5]]))
