def solution(n, lost, reserve):
    a = set(lost) & set(reserve)
    lost = list(set(lost) - a)
    reserve = list(set(reserve) - a)
    print(reserve)
    for member in reserve:
        if member + 1 in lost:
            lost.remove(member + 1)
        elif member - 1 in lost:
            lost.remove(member - 1)
    return n - len(lost)


if __name__ == "__main__":
    print(solution(5, [2, 4,3], [1, 3, 5]))
