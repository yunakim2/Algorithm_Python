from itertools import combinations


def check_num(n):
    if n == 2:
        return True
    else:
        m = int(n ** 0.5)
        for i in range(2, m + 1):
            if n % i == 0:
                return False
        return True


def solution(nums):
    answer = 0
    combi = list(combinations(nums, 3))
    print(combi)
    for i in range(len(combi)):
        sum_c = sum(combi[i])
        if check_num(sum_c):
            answer += 1

    return answer


if __name__ == "__main__":
    print(solution([1, 2, 3, 4]))
