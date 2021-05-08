from collections import deque


def solution(n, start, end, roads, traps):
    time = 0
    if start == end:
        return 0
    queue = deque([(start, 0, roads)])
    traps = set(traps)
    while queue:
        start, time, roads = queue.popleft()
        # print('start', start,'time ', time,'roads',roads)
        # print('qu',queue)
        for road in roads:
            p,q,s = road[0], road[1], road[2]
            if p == start:
                if p == start and q == end:
                    return time + s
                if q in traps:
                    for i in range(len(roads)):
                        if roads[i][0] == q or roads[i][1] == q:
                            tmp = roads[i][0]
                            roads[i][0] = roads[i][1]
                            roads[i][1] = tmp
                queue.append((q, time+s, roads))
                # print('q - ',queue,'st-',start)
    return


if __name__ == "__main__":
    print(solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2,3]))
    # print(solution(3,1,3,[[1, 2, 2], [3, 2, 3]]	,[2]))
    # print(solution(2,1,2,[[1,2,3]],[2]))