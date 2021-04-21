from collections import deque

def bfs(x,y, k_val):
    home_cnt = 0
    tmp = 0
    visited = [[False] * N for _ in range(N)]

    for i in range(x-k_val,x+1):
        for j in range(y-tmp, y+tmp+1):
            if 0<= i < N and 0<= j < N:
                if visited[i][j]:
                    continue
                if maps[i][j] == 1:
                    visited[i][j] = True
                    home_cnt += 1
            if i == x:
                continue
            if 0<= -i < N and 0<= j < N:
                if visited[-i][j]:
                    continue
                if maps[-i][j] == 1:
                    visited[-i][j] = True
                    home_cnt += 1
        tmp += 1
    tmp = 0
    for i in range(x+k_val,x, -1):
        for j in range(y-tmp, y+tmp+1):
            if 0<= i < N and 0<= j < N:
                if visited[i][j]:
                    continue
                if maps[i][j] == 1:
                    visited[i][j] = True
                    home_cnt += 1
            if i == x:
                continue
            if 0<= -i < N and 0<= j < N:
                if visited[-i][j]:
                    continue
                if maps[-i][j] == 1:
                    visited[-i][j] = True
                    home_cnt += 1
        tmp+= 1

    return home_cnt




if __name__ == '__main__':
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        N, M = map(int,input().split())
        maps = [list(map(int,input().split()))for _ in range(N)]
        max_k = N
        ans = 0
        for k in range(max_k,-1, -1):
            K = k+1
            sums_k = K*K + (K-1)* (K-1)
            for i in range(N):
                for j in range(N):
                    h_cnt = bfs(i,j,k)
                    if M * h_cnt - sums_k >= 0:
                        ans = max(ans, h_cnt)


        print('#{} {}'.format(test_case, ans))

