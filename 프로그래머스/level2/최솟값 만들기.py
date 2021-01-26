def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for a,b in zip(A,B):
        answer += a*b
    return answer


if __name__ == '__main__':
    print(solution([1, 4, 2],[5, 4, 4]))
    print(solution([1,2],[3,4]))