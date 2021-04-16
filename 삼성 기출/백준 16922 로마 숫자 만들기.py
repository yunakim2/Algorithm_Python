def dfs():
    for i in range(n+1):
        for j in range(n-i+1):
            for k in range(n-i-j+1):
                l = n-i-j-k
                val = i+5*j+10*k+50*l
                total[val] = True


if __name__ == '__main__':
    n = int(input())
    total = [False] *(50*20+1)
    total_cnt = 0
    dfs()
    for i in range(1, 50*20+1):
        if total[i]:
            total_cnt += 1

    print(total_cnt)
