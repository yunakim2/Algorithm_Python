
'''1부터N까지자연수중에서M개를고른수열을모두구하는문제(중복선택가능)'''
def dfs(idx, start):
    if idx == m:
        for i in item:
            print(i+1, end =' ')
        print()
        return
    else:
        for i in range(n):
            item[idx] = i
            dfs(idx+1, start+1)


if __name__ == '__main__':
    n,m = map(int, input().split())
    item = [0] * m
    dfs(0,0)
