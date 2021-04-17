
def bfs(checking_queue,cassle):
    cnt = 0
    while checking_queue:
        delete_item = []
        for r,c in cassle:
            tmp_item = []
            for x,y in checking_queue:
                tmp_d = abs(r-x) + abs(c-y)
                if tmp_d <= d:
                    tmp_item.append((tmp_d,x,y))

            tmp_item.sort(key = lambda x:(x[0],x[2]))
            if len(tmp_item) >=1:
                delete_item.append((tmp_item[0][1], tmp_item[0][2]))
        delete_item = set(delete_item)
        cnt += len(delete_item)
        new_queue = []
        for x,y in checking_queue:
            if x+1 <n and (x,y) not in delete_item:
                new_queue.append((x+1,y))
        checking_queue = new_queue

    return cnt

if __name__ == '__main__':
    n,m,d = map(int, input().split())
    board = [list(map(int,input().split())) for _ in range(n)]
    army = 0
    queue = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                queue.append((i,j))
    queue.sort(key = lambda  x:(-x[0]))
    for i in range(m):
        for j in range(i+1,m):
            for k in range(j+1,m):
                # print(i,j,k)
                army = max(army,bfs(queue,[(n,i),(n,j),(n,k)]) )

    print(army)


