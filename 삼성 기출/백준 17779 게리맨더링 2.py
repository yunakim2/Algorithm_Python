from collections import deque

def bfs(x, y, d1, d2):
    sum_group = [0] * 6
    tmp_group = [[0] * (n+1) for _ in range(n+1)]

    for i in range(d1+1):
        tmp_group[x+i][y-i] = 5
        tmp_group[x+d2+i][y+d2-i] = 5
    for i in range(d2+1):
        tmp_group[x+i][y+i] = 5
        tmp_group[x+d1+i][y-d1+i] =5
    for i in range(d1):
        k = 1
        while tmp_group[x+i+k][y-i] != 5:
            tmp_group[x+i+k][y-i] = 5
            k+=1
    for i in range(d2):
        k = 1
        while tmp_group[x+i+k][y+i] != 5:
            tmp_group[x+i+k][y+i] = 5
            k+= 1


    for r in range(n):
        for c in range(n):
            if 1 <= r < x + d1 and 1 <= c <= y and tmp_group[r][c] !=5:
                sum_group[0] += int(board[r][c])
                tmp_group[r][c] =1
            elif 1 <= r <= x + d2 and y < c <= n and tmp_group[r][c] !=5:
                sum_group[1] += int(board[r][c])
                tmp_group[r][c] =2

            elif x + d1 <= r <= n and 1 <= c < y - d1 + d2 and tmp_group[r][c] !=5:
                sum_group[2] += int(board[r][c])
                tmp_group[r][c] =3

            elif x + d2 < r <= n and y - d1 + d2 <= c <= n and tmp_group[r][c] !=5:
                sum_group[3] += int(board[r][c])
                tmp_group[r][c] =4
            else:
                sum_group[4] += int(board[r][c])
                tmp_group[r][c] =5


    for tmp in tmp_group:
        print(tmp)
    # print(max(sum_group), min(sum_group))
    return max(sum_group) - min(sum_group)


if __name__ == '__main__':
    n = int(input())
    board = [input().split() for _ in range(n)]

    min_value = float('inf')
    for x in range(n):
        for y in range(n):
            for d1 in range(1, n + 1):
                for d2 in range(1, n + 1):
                    if 1 <= x < x + d1 + d2 <= n and 1 <= y - d1 < y <= y + d2 <= n:
                        print(x, y, d1, d2)
                        min_value = min(min_value, bfs(x, y, d1, d2))

    print(min_value)
