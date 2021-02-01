from itertools import combinations


def solution(m, weights):
    answer = 0
    for i in range(len(weights)):
        tmp_combi = combinations(weights, i)
        answer += len([sum_combi for sum_combi in tmp_combi if sum(sum_combi) == m])
    return answer


if __name__ == "__main__":
    print(solution(3000, [500, 1500, 2500, 1000, 2000]))
