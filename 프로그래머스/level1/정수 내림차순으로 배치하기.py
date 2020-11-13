def solution(n):
    n = list(str(n))
    n.sort()
    n.reverse()

    return int(''.join(n))