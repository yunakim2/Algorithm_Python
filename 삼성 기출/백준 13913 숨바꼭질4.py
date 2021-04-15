from collections import deque
import sys



def bfs(n, k):
    queue = deque([n])
    visited[n] = True
    dist_value[n] = str(n)
    while queue:
        now = queue.popleft()
        for move in [now+1, now-1, now*2]:
            if 0 <= move < MAX and not visited[move]:
                visited[move] = True
                dist_value[move] = now
                queue.append(move)
                dist[move] = dist[now]+1
    return dist[k]


def print_path(n,k):
    if n!=k:
        print_path(n, dist_value[k])
    print(k, end=' ')



if __name__ == '__main__':
    n, k = map(int,input().split())
    MAX = 200000
    sys.setrecursionlimit(MAX)
    visited = [False]* (MAX+1)
    dist = [0]* (MAX+1)
    dist_value = [0] * (MAX+1)
    print(bfs(n,k))
    print_path(n,k)

