# CONNECTED = 1
#
# # adjacency list를 만들어주는 함수.
# def build_adj_list(signs):
#     n = len(signs)
#     answer = [[] for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if signs[i][j] == CONNECTED:
#                 answer[i].append(j)
#     return answer
#
# def dfs(어쩌고):
#
# def solution(n, signs):
#     adj_list = build_adj_list(signs)

if __name__ == "__main__":
    print(solution(3, [[0, 1, 0], [0, 0, 1], [1, 0, 0]]))
    print(solution(3, [[0, 0, 1], [0, 0, 1], [0, 1, 0]]))

