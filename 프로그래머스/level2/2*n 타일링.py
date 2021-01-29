def solution(n):
    if n <= 1:
        return 0
    if n % 2 == 0:
        count = int(n ** 0.5)
        return 2 ** count + (count-1) % 1000000007

    else:
        return solution(n - 1)


if __name__ == '__main__':
    print(solution(4))
    print(solution(2))
    print(solution(3))
    print(solution(0))
    print(solution(1))
