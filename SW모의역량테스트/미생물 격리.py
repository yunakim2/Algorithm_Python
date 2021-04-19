from collections import deque


def bfs(item):
    ans = 0
    for i in range(1, M + 1):
        new_item = []
        for r, c, cnt, move in item:
            if cnt == 0 and move == 0:
                continue
            nx, ny = r + moving[move][0], c + moving[move][1]

            if nx == 0 or ny == 0 or nx == N - 1 or ny == N - 1:
                cnt = cnt // 2
                if move == 1:
                    move = 2
                elif move == 2:
                    move = 1
                elif move == 3:
                    move = 4
                else:
                    move = 3
            new_item.append([nx, ny, cnt, move])

        item = new_item
        for i in range(len(item)):
            maxV = item[i][2]
            sumV = item[i][2]
            maxT = item[i][3]
            for j in range(i + 1, len(item)):
                if item[i][0] == item[j][0] and item[i][1] == item[j][1]:
                    if maxV < item[j][2]:
                        sumV += item[j][2]
                        maxV = item[j][2]
                        maxT = item[j][3]
                        item[j][2] = 0
                        item[j][3] = 0
                    else:
                        sumV += item[j][2]
                        item[j][2] = 0
                        item[j][3] = 0

            item[i][2] = sumV
            item[i][3] = maxT
    for i in range(len(item)):
        ans += item[i][2]
    return ans


if __name__ == '__main__':
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    moving = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}
    for test_case in range(1, T + 1):
        N, M, K = map(int, input().split())
        item = []
        for _ in range(K):
            item.append(list(map(int, input().split())))

        print('#{} {}'.format(test_case, bfs(item)))
