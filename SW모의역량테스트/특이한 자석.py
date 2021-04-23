
def item_move(item, c):
    tmp = []
    if c == 1:
        re_item = item[-1]
        tmp.append(re_item)
        for idx in range(0,7):
            tmp.append(item[idx])
    elif c == -1:
        re_item = item[0]
        for idx in range(1, len(item)):
            tmp.append(item[idx])
        tmp.append(re_item)
    else:
        tmp = item
    return tmp

if __name__ == '__main__':
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        K = int(input())
        maps = [list(map(int,input().split()))for _ in range(4)]

        for _ in range(K):
            tn,tm = map(int,input().split())
            tn -= 1
            move = [(tn,tm)]
            temp = tm
            for i in range(tn-1,-1,-1):
                if maps[i][2] != maps[i+1][6]:
                    temp *=-1
                    move.append((i,temp))
                else:
                    break
            temp = tm
            for i in range(tn+1,4):
                if maps[i][6] != maps[i-1][2]:
                    temp *= -1
                    move.append((i,temp))
                else:
                    break


            for i,m in move:
                maps[i] = item_move(maps[i],m)

        ans = 0
        if maps[0][0] == 1:
            ans += 1
        if maps[1][0] == 1:
            ans += 2
        if maps[2][0] == 1:
            ans += 4
        if maps[3][0] == 1:
            ans += 8

        print('#{} {}'.format(test_case, ans))


