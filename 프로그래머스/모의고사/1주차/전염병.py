def solution(m, n, infests, vaccinateds):
    answer = 0
    check = [[ 0 for _ in range(n)] for _ in range(m)]


    return answer


if __name__ == '__main__':
    print(solution(2, 4, [[1, 4], [2, 2]], [[1, 2]]))
    print(solution(2, 3, [[2, 2]], [[1, 2],[2,1]]))
    print(solution(2, 2, [[1, 1], [2, 2]], [[1, 2],[2,1]]))
