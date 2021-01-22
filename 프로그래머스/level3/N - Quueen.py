def solution(n):
    global answer
    answer = 0
    col = [True] * n
    diagonal1 = [True] * (2 * n - 1)
    diagonal2 = [True] * (2 * n - 1)

    def check_queen(x, y):
        print("check_queen", x, y, x + y, x - y + n - 1)
        return col[x] and diagonal1[x + y] and diagonal2[x - y + n - 1]

    def dfs(x, y):
        global answer
        if x == n:
            answer += 1
        else:
            for idx in range(n):
                if check_queen(x, y):
                    print(x,y)
                    col[x] = False
                    diagonal1[x + y] = False
                    diagonal2[x - y + n - 1] = False
                    dfs(x+1 ,idx)

    dfs(0, 0)
    return answer


if __name__ == "__main__":
    print(solution(4))
