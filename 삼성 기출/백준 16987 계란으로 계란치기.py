import copy
def dfs(idx):
    global max_value
    if idx == n:
        ans = 0
        for item in egg.values():
            if item[0] <= 0:
                ans += 1
        max_value = max(max_value, ans)
        return
    if egg[idx][0] <= 0:
        return dfs(idx+1)

    for i in range(n):
        if i == idx:
            continue
        if egg[i][0] > 0:
            egg[i][0] -= egg[idx][1]
            egg[idx][0] -= egg[i][1]
            dfs(idx+1)
            egg[i][0] += egg[idx][1]
            egg[idx][0] += egg[i][1]
    else:
        dfs(idx+1)

    return


if __name__ == '__main__':
    n = int(input())
    egg = {}
    max_value = float('-inf')
    for i in range(n):
        t = list(map(int, input().split()))
        egg[i] = t

    dfs(0)
    print(max_value)
