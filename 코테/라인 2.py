from collections import deque

def solution(endingTime, jobs):
    answer = []
    if not jobs or endingTime == 0:
        return []
    else:
        jobs.sort(key=lambda x: x[2])
        jobs = deque(jobs)
        current_time = 0
        work_queue = deque([])
        while jobs:
            if current_time >= jobs[0][1]:
                item = jobs.popleft()
                work_queue.append(item)
            if work_queue:
                if work_queue[0][2] > endingTime or current_time + work_queue[0][3] > work_queue[0][2]:
                    work_queue.popleft()
                else:
                    current_work = work_queue.popleft()
                    current_time += current_work[3]
                    answer.append(current_work[0])
            else:
                current_time += 1
        return answer


if __name__ == '__main__':
    print(solution(	40, [[1, 10, 20, 3], [2, 14, 20, 9], [3, 18, 24, 2], [4, 25, 40, 5], [5, 28, 40, 1]]))

