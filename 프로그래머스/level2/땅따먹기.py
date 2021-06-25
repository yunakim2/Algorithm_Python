def solutionDfs(land):
    def bruteforce(row, select_i, cnt):
        if row == len(land):
            nonlocal answer
            answer = max(answer, cnt)
            return

        for i in range(row, len(land)):
            for j in range(len(land[0])):
                if j == select_i:
                    continue
                bruteforce(i + 1, j, cnt + land[i][j])

    answer = 0
    for i in range(len(land[0])):
        bruteforce(1, i, land[0][i])

    return answer


def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i - 1][:j] + land[i - 1][j+1:]) + land[i][j]

    return max(land[-1])


if __name__ == "__main__":
    print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
    print(solution([[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]
                   ))
