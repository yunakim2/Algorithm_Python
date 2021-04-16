from collections import deque


def dfs(x,y,str,idx):
    if idx == 6:
        number.add(str)
        return
    dxy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    for dx,dy in dxy:
        nx = x+dx
        ny = y+dy
        if 0 <= nx <5 and 0<= ny <5 :
            dfs(nx,ny, str+board[nx][ny],idx+1)



if __name__ == '__main__':
    board = [input().split() for _ in range(5)]
    number = set()
    for i in range(5):
        for j in range(5):
            dfs(i,j, board[i][j], 1)


    print(len(number))

