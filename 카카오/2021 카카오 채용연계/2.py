from collections import deque


def bfs(queue, check_p):
    flag = True
    # print('----')
    for i in range(len(queue)):
        for j in range(i+1,len(queue)):
            x,y = queue[i]
            r,c = queue[j]
            dist = abs(x-r)+ abs(y-c)
            if dist <2:
                return False
            if dist ==2:
                # print(x,y ,'x,y')
                # print(r,c,'r,c')
                if x == r:
                    # print('x==r')
                    if check_p[x][y+1] == 'O':
                        # print('x==r')
                        flag = False
                        return flag
                elif y == c:
                    # print('y==c')
                    if check_p[x+1][y] == 'O':
                        # print('y==c')
                        flag = False
                        return flag
                else:

                    if y > c:
                        # print('y>c')
                        if check_p[x][y-1] == 'O' or check_p[x+1][y] =='O':
                            # print('y>c')
                            flag = False
                            return flag
                    else:
                        # print('y<c')
                        if check_p[x][y+1] == 'O' or check_p[x+1][y] == 'O':
                            # print('y<c')
                            flag = False
                            return flag
    return flag




def solution(places):
    answer = []
    for place in places:
        check_p = []
        queue = deque([])
        for p in place:
            check_p.append(list(p))
        for i in range(len(check_p)):
            for j in range(len(check_p[i])):
                if check_p[i][j] == 'P':
                    queue.append((i,j))
        if queue:
            if bfs(queue, check_p):
                answer.append(1)
            else:
                answer.append(0)
        else:
            answer.append(1)

    return answer


if __name__ == "__main__":
    print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
