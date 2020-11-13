def solution(N, stages):
    result = {}
    num = len(stages)

    for stage in range(1, N+1):
        if num != 0:
            count = stages.count(stage)
            result[stage] = count / num
            num -= count
        else:
            result[stage] = 0

    # result[x] - > dictinaly 기준 value값으로 정렬됨
    return sorted(result, key=lambda x : result[x], reverse=True)

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))