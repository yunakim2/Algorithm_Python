def dfs(graph,v,visited) :
    visited[v] = True
    print(v, end=' ')
    for i in graph[v] :
        if not visited[i] :
            dfs(graph,i,visited)




# 각 노드가 연결된 정보표현(인접리스트형식으로)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]* 9
dfs(graph,1,visited)