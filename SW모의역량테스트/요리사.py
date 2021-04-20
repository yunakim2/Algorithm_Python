
def dfs(cnt,start):
    global ans
    if cnt == N//2:
        teamB = list(set(total) - set(teamA))
        sumA = 0
        sumB = 0
        for i in range(N//2):
            for j in range(i + 1, N//2):
                sumA += food[teamA[i]][teamA[j]] + food[teamA[j]][teamA[i]]
                sumB += food[teamB[i]][teamB[j]] + food[teamB[j]][teamB[i]]

        ans = min(ans, abs(sumA-sumB))

        return
    for i in range(start,N):
        if checking[i]:
            continue
        checking[i] = True
        teamA[cnt] = i
        dfs(cnt+1, i+1)
        checking[i] = False




if __name__ == '__main__':
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        ans = float('inf')
        N = int(input())
        food = []
        total = [i for i in range(N)]
        checking = [False] * N
        for i in range(N):
            food.append(list(map(int, input().split())))
        teamA = [0] * (N//2)
        dfs(0,0)
        print('#{} {}'.format(test_case,ans))


