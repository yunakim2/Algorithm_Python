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


n = int(input())
for _ in range(n):
    _, j = map(int, input().split())
    h = list(map(int, input().split()))
    print(solution(h,j))
