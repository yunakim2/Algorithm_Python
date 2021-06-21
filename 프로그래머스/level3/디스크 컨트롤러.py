import heapq
from collections import deque


def solution(jobs):
    answer, now, start = 0, 0, -1
    work = []
    jobs = list(sorted(jobs, key= lambda k : k[0]))
    jobs = deque(jobs)
    total_cnt = len(jobs)
    while jobs or work:
        while jobs and start < jobs[0][0] <= now:
            w_time, w_access = jobs.popleft()
            heapq.heappush(work, [w_access, w_time])

        if work:
            current = heapq.heappop(work)
            start = now
            now += current[0]
            answer += (now - current[1])
        else:
            now += 1

    return int(answer / total_cnt)



if __name__ == "__main__":
    print(solution([[0, 9], [1, 1], [1, 1], [1, 1], [1, 1]]))
