from collections import deque

def solution(n, start, end, roads, traps):
    def dfs(start, roads, time, res):
        if start == end:
            print('end????', res)
            print(time)
            return time
        for i in range(len(roads)):
            if roads[i][0] == start:
                break
        else:
            return

        res.append(start)
        for road in roads:
            p, q, s = road[0], road[1], road[2]
            if p == start:
                if q in traps:
                    for i in range(len(roads)):
                        if roads[i][0] == q or roads[i][1] == q:
                            tmp = roads[i][0]
                            roads[i][0] = roads[i][1]
                            roads[i][1] = tmp
                dfs(q,roads, time + s, res)


    return dfs(start,roads,0, [])


if __name__ == "__main__":
    print(solution(4,1,4,[[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2,3]))
    # print(solution(3,1,3,[[1, 2, 2], [3, 2, 3]]	,[2]))
