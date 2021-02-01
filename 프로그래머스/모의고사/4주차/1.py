def solution(land):
    for row in range(1, len(land)):
        for col, _ in enumerate(land[row]):
            land[row][col] += max([land[row - 1][i] for i in range(4) if i != col])

    return max(land[len(land) - 1])


if __name__ == "__main__":
    print(solution([[1, 2, 3, 5], [5, 6, 7, 8], [4, 3, 2, 1]]))
