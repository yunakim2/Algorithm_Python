
'''1부터N까지자연수중에서M개를고른수열을모두구하는문제(중복선택가능,비내림차순)'''
def dfs(index, start):
    if index == m:
        for i in item:
            print(i+1, end=' ')
        print()
        return
    else:
        for i in range(start, n):
            item[index] = i
            dfs(index+1, i)


if __name__ == '__main__':
    n, m = map(int, input().split())
    item = [0]*m
    dfs(0,0)