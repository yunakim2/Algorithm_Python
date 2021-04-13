

def dfs(idx, start):
    if idx == m:
        for i in combi:
            print(item[i], end=' ')
        print()
        return
    else:
        for i in range(n):
            combi[idx] = i
            dfs(idx+1, i)



if __name__ == '__main__':
    n, m = map(int, input().split())
    item = list(map(int, input().split()))
    item.sort()
    combi = [0] * m
    dfs(0, 0)