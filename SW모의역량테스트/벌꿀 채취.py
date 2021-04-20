def dfs(cnt, x,y):
    if cnt == 2:
        global ans
        tmp = []
        for i in range(N):
            for j in range(N):
                if visited[i][j]:
                    tmp.append((i,j))
        if len(tmp) == M*2:
            ans = max(ans,cal(tmp))
            return

    for i in range(x,N):
        if i > x:
            y = 0
        for j in range(y,N-M+1):
            if visited[i][j]:
                continue
            for k in range(M):
                visited[i][j+k] = True
            dfs(cnt+1,i,j)
            for k in range(M):
                visited[i][j+k] = False

def selected_item(sums, start, c, visited):
    global tmps
    if start == M:
        ts = 0
        for i in range(M):
            if visited[i]:
                ts += (c[i]*c[i])
        tmps = max(tmps, ts)
        return

    for i in range(start, M):
        if visited[i]:
            continue
        selected_item(sums, start + 1, c, visited)
        if sums + c[i] <= C:
            visited[i] = True
            selected_item(sums+c[i], start+1, c, visited)
            visited[i]= False



def cal(selected):
    global tmps
    t1 = selected[:M]
    t2 = selected[M:]
    c1 = []
    c2 = []

    for x, y in t1:
        c1.append(maps[x][y])
    for x, y in t2:
        c2.append(maps[x][y])

    s1 = 0
    s2 = 0

    if sum(c1) <= C:
        for s in c1:
            s1 += (s * s)
    else:
        visited = [False] * M
        tmps = 0
        selected_item(0, 0, c1,visited)
        s1 = tmps
    if sum(c2) <= C:
        for s in c2:
            s2 += (s * s)
    else:
        visited = [False] * M
        tmps = 0
        selected_item(0, 0, c2, visited)
        s2 = tmps
    return s1+s2


if __name__ == '__main__':
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        N,M,C = map(int,input().split())
        maps = [list(map(int,input().split()))for _ in range(N)]
        visited = [[False] * N for _ in range(N)]
        selected = []
        ans = 0
        tmps = 0
        dfs(0,0,0)
        print('#{} {}'.format(test_case,ans))


