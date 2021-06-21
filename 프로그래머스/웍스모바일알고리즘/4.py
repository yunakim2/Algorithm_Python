INF = 20202020


def tsp(cur, visited):
    if visited == total:
        if not table[cur][0] == 0:
            return table[cur][0]
        else:
            return INF

    if not dp[cur][visited] == -1:
        return dp[cur][visited]

    cost = INF
    for i in range(n):
        if not visited & (1 << i) == 0:
            print(cur,'???')
            print(visited,"??")
            continue
        if table[cur][i] == 0:
            continue
        print(cur, bin(1<<i))
        print("visited", bin(visited))
        print('bitmasking-', bin(visited | (1<<i)))
        cost = min(cost, tsp(i, visited | (1 << i)) + table[cur][i])
    dp[cur][visited] = cost
    return cost


if __name__ == '__main__':
    n = 4
    table = [[0, 10, 15, 20], [5, 0, 9, 10], [6, 13, 0, 12], [8, 8, 9, 0]]
    dp = [[-1] * (1 << n) for _ in range(n)]
    print((1<<n))
    print(dp)
    total = (1 << n) - 1
    print(tsp(0, 1))
