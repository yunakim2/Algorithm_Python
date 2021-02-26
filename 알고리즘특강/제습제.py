
def check_map(maps):
    for i in range(len(maps)):
        if 1 in maps[i]:
            return False
    return True

def dfs(maps, cnt,check):
    if check_map(maps):
        return cnt
    for x in range(n):
        for y in range(n):
            if maps[x][y] == 0 and not check[x][y]:
                dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
                for dx, dy in dxy:
                    new_x = x + dx
                    new_y = y + dy
                    if 0 <= new_x < n and 0 <= new_y < n and maps[new_x][new_y] == 1 and not check[new_x][new_y]:
                        maps[new_x][new_y] = 0
                        check[new_x][new_y] = True
    if check_map(maps):
        return cnt
    else:
        check = [[False for _ in range(n)] for _ in range(n)]
        return dfs(maps,cnt +1, check)


n = int(input())
maps = []
check = [[False for _ in range(n)] for _ in range(n) ]
for _ in range(n):
    maps.append(list(map(int, input().split())))


print(dfs(maps, 1,check))
