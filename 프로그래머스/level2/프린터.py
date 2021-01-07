import heapq

def solution(priorities, location):
    heap = []
    answer = 1
    for item in priorities:
        heapq.heappush(heap, (-item))
    while heap:
        for i in range(len(priorities)):
            if priorities[i] == -heap[0]:
                if i == location:
                    return answer
                heapq.heappop(heap)
                answer += 1


print(solution([1, 1, 9, 1, 1, 1], 0))
