'''N개의 자연수 중에서 M개를 고른 수열
고른 수열은 오름차순이어야 한다.'''

def dfs(idx, start):
    if idx == m:
        for i in combi:
            print(item[i], end=' ')
        print()
        return
    for i in range(start, n):
        if check[i]:
            continue
        else:
            check[i] = True
            combi[idx] = i
            dfs(idx+1, i+1)
            check[i] = False


if __name__ == '__main__':
    n, m = map(int, input().split())
    check = [False] * n
    item = list(map(int, input().split()))
    item.sort()
    combi = [0] * m
    dfs(0, 0)