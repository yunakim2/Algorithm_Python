

def dfs(cnt,total):
    global ans
    if cnt >= len(month):
        ans = min(ans, total)
        return
    else:
        dfs(cnt+1, total + month[cnt] * money[0])
        dfs(cnt+1, total + money[1])
        dfs(cnt+3, total + money[2])





if __name__ == '__main__':
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        money = list(map(int, input().split()))
        month = list(map(int,input().split()))
        ans = float('inf')
        dfs(0,0)
        dfs(12, money[3])
        print('#{} {}'.format(test_case, ans))


