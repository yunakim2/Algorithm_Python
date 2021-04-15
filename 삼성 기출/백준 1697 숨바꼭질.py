from collections import deque

def bfs(n, k):
    queue = deque([n])
    visited[n] = True
    while queue:
        now = queue.popleft()
        for move in [now+1, now-1, now*2]:
            if 0<= move <= MAX and not visited[move]:
                visited[move] = True
                queue.append(move)
                dist[move] = dist[now]+1
    return dist[k]





if __name__ == '__main__':
    n, k = map(int,input().split())
    MAX = 200000
    visited = [False]* (MAX+1)
    dist = [0]* (MAX+1)
    print(bfs(n,k))
