from collections import deque
import heapq


def solution(jobs):
    answer = []
    TIME = 0
    TOTAL_TIME = 1
    TYPE = 2
    PRIOR = 3
    jobs = deque(jobs)
    current_time = jobs[0][TIME]
    tmp_jobs = []
    while jobs:
        if not tmp_jobs:
            tmp_jobs = [jobs.popleft()]
        for job in jobs:
            if current_time >= job[TIME]:
                tmp_jobs.append(job)

        prior_dict = dict()

        for tmp in tmp_jobs:
            if tmp[TYPE] not in prior_dict:
                prior_dict[tmp[TYPE]] = tmp[PRIOR]
            else:
                prior_dict[tmp[TYPE]] += tmp[PRIOR]

        prior_dict = sorted(prior_dict.items(), key=lambda x: -x[1])
        print(prior_dict)

    return answer


if __name__ == "__main__":
    print(solution([[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [5, 2, 1, 5], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]]))
