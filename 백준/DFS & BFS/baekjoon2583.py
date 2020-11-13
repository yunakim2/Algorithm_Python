from collections import deque



m,n,k=map(int,input().split())
graph = [[0 for _ in range(n)] for _ in range(m)]


for _ in range(k):
  x1,y1,x2,y2=map(int,input().split())
  for i in range(y1,y2):
    for j in range(x1,x2):
      graph[i][j]=-1

dx = [-1,0,0,1]
dy = [0,-1,1,0]

def bfs(x,y):
  result=1
  queue=deque()
  queue.append([x,y])
  graph[x][y]=-1
  while queue:
    x,y=queue.popleft()
    for i in range(4):
      nx=x+dx[i]
      ny=y+dy[i]
      if 0<=nx<m and 0<=ny<n and graph[nx][ny]==0:
        graph[nx][ny]=-1
        queue.append((nx,ny))
        result+=1
  return result

answer=[]
total=0
for i in range(m):
  for j in range(n):
    if graph[i][j]==0:
      total+=1
      answer.append(bfs(i,j))
answer.sort()
print(total)
print(*answer)

