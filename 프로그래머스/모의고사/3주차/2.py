import math


def solution(n, stations, w):
    answer = 0
    distance = []
    for idx in range(1, len(stations)):
        distance.append((stations[idx] - w - 1) - (stations[idx - 1] + w))

    distance.append(stations[0] - w - 1)
    distance.append(n - (stations[-1] + w))

    for d in distance:
        if d <= 0:
            continue
        answer += math.ceil(d / ((w * 2) + 1))
    return answer


if __name__ == "__main__":
    print(solution(11, [4, 11], 1))
    print(solution(16, [9], 2))
