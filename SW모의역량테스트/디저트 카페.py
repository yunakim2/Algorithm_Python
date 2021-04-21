
from collections import deque

def dfs(x,y,m,n):
    global sx,sy,ans

    if m == 3 and x == sx and y == sy:
        if ans < n:
            ans = n
    elif x < 0 or x >= N or y < 0 or y >= N:
        return
    elif maps[x][y] in U:
        return
    else:
        U.append(maps[x][y])
        if m == 0 or m ==1:
            dfs(x+move[m][0] , y+move[m][1] , m, n+1)
            dfs(x+move[m+1][0] , y+move[m+1][1] , m+1, n+1)
        elif m ==2:
            if x+y != sx+sy:
                dfs(x+move[2][0] , y+move[2][1], m, n+1)
            else:
                dfs(x+move[3][0], y+move[3][1], m+1,n+1)
        else:
            dfs(x+move[3][0], y+move[3][1] , m , n+1)
        U.remove(maps[x][y])


if __name__ == '__main__':
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        N = int(input())
        ans = -1
        maps = [list(map(int,input().split()))for _ in range(N)]
        move = [(1,1),(1,-1),(-1,-1),(-1,1)]
        U = []
        visited = [[False]* N for _ in range(N)]
        for i in range(N):
            for j in range(1,N-1):
                sx = i
                sy = j
                U.append(maps[i][j])
                dfs(i+1,j+1,0,1)
                U.remove(maps[i][j])

        print('#{} {}'.format(test_case, ans))
