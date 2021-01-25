from collections import deque


def solution(n, signs):
    check_sign = [[False for _ in range(n)] for _ in range(n)]

    def dfs(i, n, row):
        if i == n:
            return
        if check_sign[row]:
            return
        check_sign[row] = True
        for col in range(n):
            if signs[row][col] == 1 and not check_sign[col]:
                dfs(i+1, n, col)

    dfs(0, n, 0)
    print(signs)
    return


if __name__ == "__main__":
    print(solution(3, [[0, 1, 0], [0, 0, 1], [1, 0, 0]]))
