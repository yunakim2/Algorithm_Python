'''N개의 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
고른 수열은 비내림차순이어야 한다'''

def dfs(idx, start):
    if idx == m:
        for i in combi:
            print(item[i], end=' ')
        print()
        return
    else:
        for i in range(start,n):
            combi[idx] = i
            dfs(idx+1, i)



if __name__ == '__main__':
    n, m = map(int, input().split())
    item = list(map(int, input().split()))
    item.sort()
    combi = [0] * m
    dfs(0, 0)