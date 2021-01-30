CONNECTED = 1
# adjacency list를 만들어주는 함수.
def build_adj_list(signs):
    n = len(signs)
    answer = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if signs[i][j] == CONNECTED:
                answer[i].append(j)
    return answer


def solution(n, signs):
    adj_list = build_adj_list(signs)

    def dfs(start_node, init_node, visited):
        if start_node == init_node and False not in visited:
            return
        for destination in adj_list[start_node]:
            if not visited[destination] :
                signs[init_node][destination] = CONNECTED
                visited[destination] = True
                dfs(destination, init_node, visited)

        return

    for start_row in range(len(adj_list)):
        visited = [False] * len(adj_list)
        dfs(start_row, start_row, visited)

    return signs


if __name__ == "__main__":
    print(solution(3, [[0, 1, 0], [0, 0, 1], [1, 0, 0]]))
    print(solution(3, [[0, 0, 1], [0, 0, 1], [0, 1, 0]]))
