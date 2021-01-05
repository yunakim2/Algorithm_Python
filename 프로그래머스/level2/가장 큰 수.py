import itertools


# def solution(numbers):
#     answer = ''
#     numbers = map(str, numbers)
#     tmp = list(map(''.join, itertools.permutations(numbers)))
#     return max(tmp)

def solution(numbers):
    answer = ''
    numbers = map(str, numbers)
    tmp = list(map(''.join, itertools.permutations(numbers)))
    return max(tmp)

print(solution([3, 30, 34, 5, 9]))
