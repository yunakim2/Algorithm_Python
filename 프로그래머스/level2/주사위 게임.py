def solution(monster, S1, S2, S3):
    answer = 0
    for i in range(1, S1 + 1):
        for j in range(1, S2 + 1):
            for k in range(1, S3 + 1):
                move = i + j + k + 1
                if move not in monster:
                    answer += 1

    return int(answer / (S1 * S2 * S3) * 1000)


if __name__ == "__main__":
    print(solution([4, 9, 5, 8], 2, 3, 4))
    print(solution([4, 9, 5, 8], 2, 3, 3))
