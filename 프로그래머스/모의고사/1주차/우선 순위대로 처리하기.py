from collections import deque
import heapq


def solution(reqs):
    answer = []
    heap = []
    current_time = 0
    work_done_time = 0
    reqs = [(-priority, sec, index) for index, [priority, sec] in enumerate(reqs)]
    reqs = deque(reqs)

    while reqs or heap:
        if reqs and current_time % 3 == 0:
            heapq.heappush(heap, reqs.popleft())

        if heap and work_done_time <= current_time:
            _, sec, index = heapq.heappop(heap)
            work_done_time = current_time + sec
            answer.append(index + 1)
        current_time += 1

    return answer


if __name__ == "__main__":
    print(solution([[1, 7], [4, 1], [5, 2], [3, 1], [7, 2]]))
    # print(solution([[3, 7], [8, 7], [29, 6], [6, 7], [2, 2], [19, 10]]))
    # print(solution([[338, 1], [58, 5], [60, 4], [142, 3]]))
