def dfs(x, y, cnt, sum_value):
    dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    if cnt == k:
        global max_value
        max_value = max(max_value, sum_value)
        return
    for i in range(x, n):
        for j in range(y if i == x else 0, m):
            if check[i][j]:
                continue
            for dx, dy in dxy:
                nx, ny = i + dx, j + dy
                if 0 <= nx < n and 0 <= ny < m and check[nx][ny]:
                    break
            else:
                check[i][j] = True
                dfs(i, j, cnt + 1, sum_value + item[i][j])
                check[i][j] = False


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    item = []
    for _ in range(n):
        item.append(list(map(int, input().split())))

    max_value = 0
    check = [[False for _ in range(m)] for _ in range(n)]
    dfs(0, 0, 0, 0)
    print(max_value)
