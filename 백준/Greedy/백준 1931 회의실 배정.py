def solution(arr):
    answer = 0
    arr.sort(key=lambda k: (k[1], k[0]))
    end = 0
    for start, done in arr:
        if start >= end:
            answer += 1
            end = done
    return answer


n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

print(solution(arr))
