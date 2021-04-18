def check(x, y):
    if 0 <= x < n and 0 <= y < n and maps[x][y] != 1:
        return True
    return False


def dfs(r1, c1, mode):
    global ans
    if r1 == n - 1 and c1 == n - 1:
        return 1
    ans = cnt[r1][c1][mode]
    if ans != -1:
        return ans
    ans = 0
    if mode == H:
        if check(r1, c1 + 1):
            ans += dfs(r1, c1 + 1, H)
        if check(r1 + 1, c1 + 1) and check(r1, c1 + 1) and check(r1 + 1, c1):
            ans += dfs(r1 + 1, c1 + 1, D)

    elif mode == V:
        if check(r1 + 1, c1):
            ans += dfs(r1 + 1, c1, V)
        if check(r1 + 1, c1 + 1) and check(r1, c1 + 1) and check(r1 + 1, c1):
            ans += dfs(r1 + 1, c1 + 1, D)

    else:
        if check(r1 + 1, c1):  # 세로
            ans += dfs(r1 + 1, c1, V)
        if check(r1, c1 + 1):  # 가로
            ans += dfs(r1, c1 + 1, H)
        if check(r1 + 1, c1 + 1) and check(r1, c1 + 1) and check(r1 + 1, c1):
            ans += dfs(r1 + 1, c1 + 1, D)
    cnt[r1][c1][mode] = ans
    return ans


if __name__ == '__main__':
    n = int(input())

    maps = [list(map(int, input().split())) for _ in range(n)]
    cnt = [[[-1] * 3 for _ in range(n)] for _ in range(n)]
    ans = 0
    H = 0
    D = 1
    V = 2
    if maps[n - 1][n - 1] != 1:
        print(dfs(0, 1, H))
    '''H - 가로, V-세로, D - 대각선'''
