
def dfs(x,y,road,k):
    dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    global max_road
    if max_road < road+1:
        max_road = road+1

    visited[x][y] = True
    for dx,dy in dxy:
        nx,ny = x+dx, y+dy
        if 0<= nx <n and 0<=ny <n and not visited[nx][ny]:
            if maps[nx][ny] < maps[x][y]:
                dfs(nx,ny, road+1,k)
            elif maps[nx][ny] - k < maps[x][y]:
                pre = maps[nx][ny]
                maps[nx][ny] = maps[x][y]-1
                dfs(nx,ny, road+1, 0)
                maps[nx][ny] = pre
    visited[x][y] = False

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,k = map(int, input().split())
    maps = [list(map(int,input().split()))for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    max_value = 0
    max_road = 0
    for i in range(n):
        for j in range(n):
            if max_value < maps[i][j]:
                max_value = maps[i][j]

    for i in range(n):
        for j in range(n):
            if maps[i][j] != max_value:
                continue
            else:
                dfs(i,j,0,k)

    print('#',end='')
    print(str(test_case),end =' ')
    print(max_road)

