


def dfs(r1, c1, mode):
    if r1 == n - 1 and c1 == n - 1:
        return 1
    ans = cnt[r1][c1][mode]
    if ans != -1:
        return ans

    ans = 0
    if mode == H:
        if c1 + 1 < n and maps[r1][c1 + 1] == 0:
            ans += dfs(r1, c1 + 1, H)
        if r1 + 1 < n and c1 + 1 < n and maps[r1 + 1][c1 + 1] == 0 and maps[r1 + 1][c1] == 0 and maps[r1][c1 + 1] == 0:
            ans += dfs(r1 + 1, c1 + 1, D)

    elif mode == V:
        if r1+1 <n and maps[r1+1][c1] == 0:
            ans += dfs(r1 + 1, c1, V)
        if  r1 + 1 < n and c1 + 1 < n and maps[r1 + 1][c1 + 1] == 0 and maps[r1 + 1][c1] == 0 and maps[r1][c1 + 1] == 0:
            ans += dfs(r1 + 1, c1 + 1, D)

    else:
        if r1 + 1 < n and maps[r1 + 1][c1] == 0:
            ans += dfs(r1 + 1, c1, V)
        if c1 + 1 < n and maps[r1][c1 + 1] == 0:
            ans += dfs(r1, c1 + 1, H)
        if  r1 + 1 < n and c1 + 1 < n and maps[r1 + 1][c1 + 1] == 0 and maps[r1 + 1][c1] == 0 and maps[r1][c1 + 1] == 0:
            ans += dfs(r1 + 1, c1 + 1, D)
    cnt[r1][c1][mode] = ans
    return ans


if __name__ == '__main__':
    n = int(input())

    maps = [list(map(int, input().split())) for _ in range(n)]
    cnt = [[[-1] * 3 for j in range(n)] for i in range(n)]
    H = 0
    D = 1
    V = 2
    print(dfs(0, 1, H))
    '''H - 가로, V-세로, D - 대각선'''
