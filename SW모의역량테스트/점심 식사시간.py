
from collections import deque
def bfs(teamA,teamB):
    timeA = deque()
    timeB = deque()
    for i,x,y in teamA:
        t_time = abs(x-dest[0][1]) + abs(y-dest[0][2])
        timeA.append((i,t_time))
    for i,x,y in teamB:
        t_time = abs(x-dest[1][1]) + abs(y-dest[1][2])
        timeB.append((i,t_time))

    timeA = deque(sorted(timeA, key= lambda t : t[1]))
    timeB = deque(sorted(timeB, key = lambda t : t[1]))
    accessA = deque([])
    accessB = deque([])

    time_A = 0
    time_B = 0
    # print('A시작-----')
    while True:
        c = 3
        tmp = []
        for access in accessA:
            if access[1] == 0:
                continue
            else:
                tmp.append(access)

        accessA = deque(tmp)
        for i, access in enumerate(accessA):
            if c == 0:
                break
            accessA[i][1] = access[1]-1
            c -= 1

        while len(timeA) > 0 and time_A == timeA[0][1]:
            item_id,_ = timeA.popleft()
            accessA.append([item_id,dest[0][0]])
        # print('time_A', time_A, 'timeA --', timeA, 'accessA--', accessA)
        if len(timeA) == 0 and len(accessA) == 0:
            break
        time_A += 1

    tmp = []
    # print('B 시작 ----')
    while True:
        c = 3
        tmp = []
        for access in accessB:
            if access[1] == 0:
                continue
            else:
                tmp.append(access)

        accessB = deque(tmp)

        for i, access in enumerate(accessB):
            if c == 0:
                break
            accessB[i][1] = access[1] - 1
            c -= 1

        while len(timeB) > 0 and time_B == timeB[0][1]:
            item_id, _ = timeB.popleft()
            accessB.append([item_id, dest[1][0]])

        if len(timeB) == 0 and len(accessB) == 0:
            break
        time_B += 1
        # print('time_B', time_B, 'timeB --', timeB, 'accessB--', accessB)
    # print('끝ㄴ-----',time_A,time_B)
    return max(time_A, time_B)

def dfs(idx, teamA, teamB):
    global min_value
    if idx == cnt:
        min_value = min(min_value, bfs(teamA, teamB))
        return
    teamA.append(load[idx])
    dfs(idx+1, teamA,teamB)
    teamA.remove(load[idx])
    teamB.append(load[idx])
    dfs(idx+1, teamA, teamB)
    teamB.remove(load[idx])
    teamA = [(1,0,2),(2,0,3),(3,1,2),(4,2,3)]
    teamB = [(5,3,1),(6,4,0)]
    bfs(teamA,teamB)
    # #
    # teamA = [(1,0,1),(2,0,2),(3,1,2)]
    # teamB = [(4,2,1),(5,2,3),(6,4,0)]
    # bfs(teamA,teamB)
    #
    # teamA = [(1,0,1),(2,0,2),(3,1,2),(4,2,1),(5,2,3)]
    # teamB =[(6,4,0)]
    # bfs(teamA,teamB)


if __name__ == '__main__':
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        N = int(input())
        maps = [list(map(int,input().split())) for _ in range(N)]
        load = []
        dest = {}
        idx = 0
        id = 0
        for i in range(N):
            for j in range(N):
                if maps[i][j] == 1:
                    load.append((id,i,j))
                    id += 1

                if maps[i][j] > 1:
                    dest[idx] = (maps[i][j] , i,j)
                    idx += 1

        cnt = len(load)
        min_value = float('inf')

        dfs(0,[],[])
        print('#{} {}'.format(test_case, min_value))




