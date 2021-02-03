def solution(land):
    for row in range(1, len(land)):
        for col, _ in enumerate(land[row]):
            land[row][col] += max([land[row - 1][i] for i in range(4) if i != col])

    return max(land[-1])