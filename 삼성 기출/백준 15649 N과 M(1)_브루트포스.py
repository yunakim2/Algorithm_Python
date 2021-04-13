
'''1부터N까지자연수중에서중복없이M개를고른수열을모두구하는문제'''
def dfs(start, idx, check) :
    if idx == m:
        for i in item:
            print(i+1, end=' ')
        print()
        return

    for i in range(n):
        if check[i]:
            continue
        else:
            check[i] = True
            item[idx] = i
            dfs(start+1, idx+1, check)
            check[i] = False


if __name__ == '__main__':
    n, m = map(int, input().split())
    check = [False] * n
    item = [0] * m
    dfs(0, 0, check)
