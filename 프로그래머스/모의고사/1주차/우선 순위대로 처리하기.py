from collections import deque
import heapq


def solution(reqs):
    answer = []
    queue = deque([(*req, idx) for idx, req in enumerate(reqs, 1)])
    heap = []
    RANK, TIME , IDX = 0,1,2
    item = queue.popleft()
    heapq.heappush(heap, (-item[RANK], item[IDX]))
    time = 0

    while heap:
        work = heapq.heappop(heap)
        index = work[1]-1
        timer = reqs[index][1]
        answer.append(index+1)
        for _ in range(timer):
            time += 1
            if time % 3 == 0 :
                if queue:
                    item = queue.popleft()
                    heapq.heappush(heap,(-item[RANK], item[IDX]))
        if not heap:
            if queue:
                item = queue.popleft()
                heapq.heappush(heap,(-item[RANK], item[IDX]))

    return answer


if __name__ == "__main__":
    print(solution([[1, 7], [4, 1], [5, 2], [3, 1], [7, 2]]))
    print(solution([[3, 7], [8, 7], [29, 6], [6, 7], [2, 2], [19, 10]]))
