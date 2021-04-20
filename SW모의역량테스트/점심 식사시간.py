from collections import deque

def bfs(e,person_list):
    time = 0
    ex, ey = enter[e]
    queue = deque([(ex, ey, 1)])
    process = deque()
    visited = [[False]* n  for _ in range(n)]
    dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    while queue:
        x,y,t = queue.popleft()
        visited[x][y] = True
        for dx,dy in dxy:
            nx = x+dx
            ny = y+dy
            if 0 <= nx < n and 0<=ny <n  and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny,t+1))
                if (nx,ny) in person_list:
                    process.append([t, nx, ny])
    cnt = 3
    time = process[0][0]
    while process:
        print(process,time)
        t, x, y = process.popleft()
        while cnt:
            if len(process) >=1:
                if t == process[0][0]:
                    process.popleft()
            cnt -= 1
        cnt = 3
        for i in range(maps[ex][ey]):
            time += 1
    print(time)
    return time



if __name__ == '__main__':
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        n = int(input())
        maps = [list(map(int,input().split())) for _ in range(n)]

        person = []
        penter = {0: [], 1: []}
        enter = {}
        tmp = 0
        for i in range(n):
            for j in range(n):
                if maps[i][j] == 1:
                    person.append((i,j))
                    continue
                elif maps[i][j] > 1:
                    enter[tmp] = (i,j)
                    tmp+=1


        for px,py in person:
            t1 = abs(px-enter[0][0]) + abs(py-enter[0][1])
            t2 = abs(px-enter[1][0]) + abs(py-enter[1][0])
            if t1 > t2:
                penter[1].append((px, py))
            elif t1 < t2:
                penter[0].append((px, py))
            else:
                if len(penter[1]) > len(penter[0]):
                    penter[0].append((px,py))
                else:
                    penter[1].append((px,py))

        ans = 0

        print(penter)
        for i in penter.keys():
            ans = max(ans, bfs(i, penter[i]))

        print('#{} {}'.format(test_case,ans))


