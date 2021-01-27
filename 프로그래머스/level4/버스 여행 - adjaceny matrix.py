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

def dfs(row,signs, adj_list):
    if len(adj_list[row]) == len(signs):
        return
    for destination in adj_list[row] :
        if signs[destination][row] == 1 and row not in adj_list[destination]:
            adj_list[row].append(destination)
            print(adj_list)
            signs[row][destination] = 1
            dfs(destination, signs, adj_list)


def solution(n, signs):
    adj_list = build_adj_list(signs)
    dfs(0, signs, adj_list)
    return signs





if __name__ == "__main__":
    print(solution(3, [[0,1,0], [0, 0, 1], [1, 0, 0]]))
    # print(solution(3, [[0, 0, 1], [0, 0, 1], [0, 1, 0]]))

