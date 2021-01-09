import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        num = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        answer += 1
        heapq.heappush(scoville, num)
        if answer >= len(scoville):
            answer = -1
            break

    return answer


print(solution([1, 2, 3, 9, 10, 12], 7))
