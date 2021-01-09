import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while len(scoville) > 1 and scoville[0] < K:
        num = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        answer += 1
        heapq.heappush(scoville, num)

    if len(scoville) == 1 and scoville[0] < K:
        return -1

    return answer


print(solution([1, 2, 3], 11))
