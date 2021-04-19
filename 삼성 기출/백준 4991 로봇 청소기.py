from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[0]* c for _ in range(r)]
    visited[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] != 'x' and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    return visited


if __name__ == '__main__':
    while True:
        c, r = map(int, input().split())
        if c == 0 and r == 0:
            break
        maps = [list(input()) for _ in range(r)]
        dirty = [(0,0)]
        for i in range(r):
            for j in range(c):
                if maps[i][j] == 'o':
                    dirty[0] = (i,j)
                if maps[i][j] == '*':
                    dirty.append((i,j))

