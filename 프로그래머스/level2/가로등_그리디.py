import math


def solution(l, v):
    v.sort()
    max_d = max(v[0], l - v[-1])

    for i in range(1, len(v)):
        d = math.ceil((v[i] - v[i - 1]) / 2)
        max_d = max(max_d, d)
    return max_d


if __name__ == "__main__":
    print(solution(15, [15, 5, 3, 7, 9, 14, 0]))
    print(solution(5, [2, 5]))
