from itertools import combinations


def solution(n):
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

    prime_num = sieve(n)
    return len([prime for prime in combinations(prime_num, 3) if sum(prime) == n])


if __name__ == "__main__":
    print(solution(33))
    print(solution(9))
