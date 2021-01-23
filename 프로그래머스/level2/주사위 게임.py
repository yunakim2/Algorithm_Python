from itertools import product


def solution(monster, S1, S2, S3):
    answer = 0
    range_S1 = list(idx for idx in range(1, S1 + 1))
    range_S2 = list(idx for idx in range(1, S2 + 1))
    range_S3 = list(idx for idx in range(1, S3 + 1))

    for i, j, k in list(product(range_S1, range_S2, range_S3)):
        move = i + j + k + 1
        if move not in monster:
            answer += 1

    return int(answer / (S1 * S2 * S3) * 1000)


if __name__ == "__main__":
    print(solution([4, 9, 5, 8], 2, 3, 4))
    print(solution([4, 9, 5, 8], 2, 3, 3))
