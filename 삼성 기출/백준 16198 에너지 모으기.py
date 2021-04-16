

def dfs(e):
    if len(e) == 2:
        return 0
    ans = 0
    for idx in range(1,len(e)-1):
        tmp_energy = e[idx-1] * e[idx+1]
        tmp_e = e[:idx]+e[idx+1:]
        tmp_energy += dfs(tmp_e)
        ans = max(ans, tmp_energy)
    return ans


if __name__ == '__main__':
    n = int(input())
    energy = list(map(int,input().split()))
    print(dfs(energy))