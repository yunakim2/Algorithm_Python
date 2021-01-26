def solution(n, signs):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if signs[i][k] != 0 and signs[k][j] != 0:
                    signs[i][j] = 1
    return signs


if __name__ == "__main__":
    print(solution(3, [[0, 1, 0], [0, 0, 1], [1, 0, 0]]))
    print(solution(3,[[0,0,1],[0,0,1],[0,1,0]]))
