'''N개의 자연수 중에서 M개를 고른 수열'''


def dfs(idx, start):
    if idx == m:
        for i in combi:
            print(str(item[i]), end=' ')
        print()
        return
    for i in range(n):
        if check[i]:
            continue
        else:
            check[i] = True
            combi[idx] = i
            dfs(idx +1, start+1)
            check[i] = False


if __name__ == '__main__':
    n,m = map(int, input().split())
    check = [False]*n
    item = list(map(int,input().split()))
    item.sort()
    combi = [0]*m
    dfs(0, 0)
