import heapq


def solution(no, works):
    max_heap = []
    if no >= sum(works):
        return 0
    for work in works:
        heapq.heappush(max_heap, (-work, work))
    for _ in range(no):
        work = heapq.heappop(max_heap)[1] - 1
        heapq.heappush(max_heap, (-work, work))
    return sum(i[1] ** 2 for i in max_heap)


print(solution(4, [4, 3, 3]))
