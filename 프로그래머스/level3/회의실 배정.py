def solution(arr):
    answer = 0
    arr.sort(key=lambda k: (k[1], k[0]))
    end = 0
    for start , done in arr:
        if start >= end:
            answer += 1
            end = done
    return answer


if __name__ == "__main__":
    print(solution([[1, 2], [2, 4], [2, 2]]))
