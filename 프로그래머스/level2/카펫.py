def solution(brown, red):
    for row in range(1, int(red ** 0.5) + 1):
        if red % row == 0:
            col = red // row
            if 2 * row + 2 * col + 4 == brown:
                return [col + 2, row + 2]


if __name__ == "__main__":
    print(solution(10, 2))
    print(solution(8, 1))
    print(solution(14, 4))
    print(solution(24, 24))
    print(solution(50, 22))
    print(solution(18, 6))
