def solution(m, n, puddles):
    set_puddles = set()
    for puddle in puddles:
        set_puddles.add(tuple(puddle))

    load = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i == 1 and j == 1:
                load[i][j] = 1
            elif (i, j) not in set_puddles:
                load[i][j] = load[i - 1][j] + load[i][j - 1]
    return load[m][n] % 1_000_000_007


if __name__ == "__main__":
    print(solution(4, 3, [[2, 2]]))
