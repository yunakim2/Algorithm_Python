def solution(n):
    global answer
    answer = 0
    col = [True] * n
    diagonal1 = [True] * (2 * n - 1)
    diagonal2 = [True] * (2 * n - 1)

    def check_queen(x, y):
        return col[y] and diagonal1[x + y] and diagonal2[x - y + n - 1]

    def dfs(x):
        global answer
        if x == n:
            answer += 1
        else:
            for idx in range(n):
                if check_queen(x, idx):
                    col[idx] = False
                    diagonal1[x + idx] = False
                    diagonal2[x - idx + n - 1] = False
                    dfs(x + 1)
                    col[idx] = True
                    diagonal1[x + idx] = True
                    diagonal2[x - idx + n - 1] = True

    dfs(0)
    return answer


if __name__ == "__main__":
    print(solution(4))
