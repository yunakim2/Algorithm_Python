from collections import deque
import heapq

direct = {0: (-1,0), 1:(-1,-1), 2:(0,-1), 3:(1,-1), 4:(1,0), 5:(1,1), 6:(0,1), 7:(-1,1)}

shark = deque([(0,0)])
shark_d = 0
fish = []
d_fish = []
N = 4
for _ in range(N):
    strs = list(map(int, input().split()))
    tmp_f = []
    tmp_d = []
    for idx,s in enumerate(strs):
        if idx % 2 == 0:
            tmp_f.append(s)
        else:
            tmp_d.append(s-1)
    fish.append(tmp_f)
    d_fish.append(tmp_d)

def fish_moving(fish, d_fish,sx,sy):
    fish_num = []
    for i in range(N):
        for j in range(N):
            heapq.heappush(fish_num, (fish[i][j], i, j))

    fish_num = sorted(fish_num, key = lambda x : x[0])
    for idx, i, j in fish_num:
        item = d_fish[i][j]
        re_item = item
        if (i,j) in (sx,sy):
            continue
        if fish[i][j] == 0 :
            continue
        while True:
            dx, dy = direct[re_item]
            x , y = i + dx, j + dy
            if 0<= x < N and 0 <= y < N and (x,y) not in (sx,sy):
                fish_num[fish[x][y]-1] = (fish_num[fish[x][y]-1][0], i, j)
                d_fish[x][y] , d_fish[i][j] = d_fish[i][j] , d_fish[x][y]
                fish[x][y], fish[i][j] = fish[i][j] , fish[x][y]
                break
            re_item = (re_item + 1) % 8
            if item == re_item:
                break


def shark_moving(r,c,d, sum) :
    global ans
    board = [[0for _ in range(4)] for _ in range(4)]
    d_board = [[0for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            board[i][j] = fish[i][j]
            d_board[i][j] = d_fish[i][j]

    fish_moving(fish, d_fish, r, c)

    if ans < sum:
        ans = sum

    for i in range(1,4):
        dx, dy = direct[d]
        snr = r+ dx * i
        snc = c + dy * i
        if 0 <= snr < N and 0 <= snc < N:
            if fish[snr][snc] == 0 :
                continue
            else:
                f = fish[snr][snc]
                fish[snr][snc] = 0
                shark_moving(snr, snc,d_fish[snr][snc], sum + f)
                fish[snr][snc] = f
        else:
            break
    for i in range(4):
        for j in range(4):
            fish[i][j] = board[i][j]
            d_fish[i][j] = d_board[i][j]

ans = 0

shark_moving(0,0,d_fish[0][0], 0)
for i in range(N):
    for j in range(N):
        print(fish[i][j], end= ' ')
    print()
print(ans)