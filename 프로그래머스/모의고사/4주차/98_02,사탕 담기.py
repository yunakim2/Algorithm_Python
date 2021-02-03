from itertools import combinations


def solution(m, weights):
    answer = 0
    for num_cadies in range(len(weights)):
        combi_cadies = combinations(weights, num_cadies)
        answer += len([sum_combi for sum_combi in combi_cadies if sum(sum_combi) == m])
    return answer