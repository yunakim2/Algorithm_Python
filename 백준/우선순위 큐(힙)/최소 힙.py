import heapq
import sys
n = int(sys.stdin.readline())
heap = []
heapq.heapify(heap)
for _ in range(n):
    item = int(sys.stdin.readline())
    if item == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, item)

