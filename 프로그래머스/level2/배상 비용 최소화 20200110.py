import heapq


def solution(no, works):
    heap = []
    if sum(works) <= no:
        return 0
    for work in works:
        heapq.heappush(heap, (-work, work))

    while no > 0:
        work = heapq.heappop(heap)[1] - 1
        heapq.heappush(heap, (-work, work))
        no -= 1

    return sum([i[1] ** 2 for i in heap])


print(solution(4, [4, 3, 3]))
