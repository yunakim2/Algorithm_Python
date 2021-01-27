from itertools import combinations


def solution(nums):
    def sieve(n):
        is_prime = [True] * (n + 1)
        is_prime[0] = False
        is_prime[1] = False

        for candidate in range(2, n + 1):
            if not is_prime[candidate]:
                continue
            for multiple in range(candidate * candidate, n + 1, candidate):
                is_prime[multiple] = False
        return [idx for idx, value in enumerate(is_prime) if value]

    combi_num = [sum(num) for num in combinations(nums, 3)]
    check_prime = sieve(max(combi_num))
    return len([num for num in combi_num if num in check_prime])

if __name__ == "__main__":
    print(solution([1, 2, 3, 4]))
    print(solution([1, 2, 7, 6, 4]))