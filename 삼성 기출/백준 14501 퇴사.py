

def dfs(day, sum):
    if day == n+1:
        global max_value
        max_value = max(max_value, sum)
        return
    if day > n+1:
        return
    dfs(day+1,sum) # 선택 안하고
    dfs(day+days[day], sum+pays[day]) # 선택 하고



if __name__ == '__main__':
    n = int(input())
    max_value = 0
    days = [0] * (n+1)
    pays = [0] * (n+1)
    check = [False] * n
    for i in range(1,n+1):
        days[i], pays[i] = map(int,input().split())

    dfs(1,0)
    print(max_value)

