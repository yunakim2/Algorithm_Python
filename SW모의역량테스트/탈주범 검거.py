from collections import deque


def bfs(R,C):
    global ans
    queue = deque()
    queue.append((R,C,1))
    visited[R][C] = True

    while queue:
        x,y,t = queue.popleft()
        m = maps[x][y]
        for dx,dy in move[m]:
            nx,ny = x+dx, y+dy
            if 0<= nx < N and 0<= ny <M  and is_connect(x,y,nx,ny):
                if not visited[nx][ny]:
                    if t <= L-1:
                        ans += 1
                        queue.append((nx,ny,t+1))
                        visited[nx][ny] = True







def is_connect(x, y, nx, ny):
    for nnx, nny in move[maps[nx][ny]]:
        pre_x = nx + nnx
        pre_y = ny + nny
        if pre_x == x and pre_y == y:
            return True
    return False


if __name__ == '__main__':
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        move = {0 : [],1: [(0, 1), (0, -1), (1, 0), (-1, 0)], 2: [(1, 0), (-1, 0)], 3: [(0, -1), (0, 1)], 4: [(-1, 0), (0, 1)],
                5: [(1, 0), (0, 1)], 6: [(1, 0), (0, -1)], 7: [(-1, 0), (0, -1)]}
        N, M, R, C, L = map(int, input().split())
        maps = []
        visited = [[False]* M for _ in range(N)]
        ans = 1
        for i in range(N):
            maps.append(list(map(int, input().split())))
        bfs(R,C)

        print('#{} {}'.format(test_case,ans))
