import heapq
# def solution(no, works):
#     for _ in range(no):
#         works.sort()
#         if works[-1] == 0:
#             break
#         works[-1] -= 1
#
#     return sum([i*i for i in works])


def solution(no, works):
    MaxHeap = []
    if no >= sum(works):
        return 0
    for i in works:
        heapq.heappush(MaxHeap,(-i,i))
    for _ in range(no):
        i = heapq.heappop(MaxHeap)[1]-1
        heapq.heappush(MaxHeap,(-i,i))
    return sum(i[1]**2 for i in MaxHeap)



print(solution(4,[4,3,3]))