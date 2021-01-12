from collections import Counter
import heapq


def solution(healths, items):
    answer = []
    power = 0
    heapq.heapify(healths)
    print(healths)
    while healths:
        health = heapq.heappop(healths)
        for i, item in enumerate(items):
            if health - item[1] >= 100:
                tmp_power = item[0] + power
                if tmp_power >= power:
                    power = tmp_power
                    answer.append(i + 1)

    return sorted(Counter(answer).keys())


if __name__ == '__main__':
    print(solution([200, 120, 150], [[30, 100], [500, 30], [100, 400]]))
    print(solution([300, 200, 500], [[1000, 600], [400, 500], [300, 100]]))
