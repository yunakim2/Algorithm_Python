def solution(l, v):
    lower = 1
    upper = l + 1

    def is_possible(d):
        if 0 < v[0] - d or v[-1] + d < l:
            return False
        for i in range(1,len(v)):
            if v[i-1] + d < v[i] - d:
                return False
        return True

    v.sort()
    while lower <= upper:
        mid = (lower + upper) // 2
        if is_possible(mid):
            upper = mid - 1
        else:
            lower = mid + 1
    return upper + 1


if __name__ == "__main__":
    print(solution(15, [15, 5, 3, 7, 9, 14, 0]))
    print(solution(5,[2,5]))
