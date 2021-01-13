from collections import Counter
import math


def solution(progresses, speeds):
    queue = []
    zipped = list(zip(progresses,speeds))
    for i in range(len(zipped)):
        progress= zipped[i][0]
        speed = zipped[i][1]
        queue.append(math.ceil((100 - progress) / speed))

    for i, item in enumerate(queue):
        if i != 0:
            if item < queue[i-1]:
                queue[i] = queue[i-1]

    return list(Counter(queue).values())


if __name__ == '__main__':
    print(solution([93, 30, 55], [1, 30, 5]))