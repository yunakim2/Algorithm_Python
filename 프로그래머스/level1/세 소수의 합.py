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

    def dfs(cur_idx, count, total):
        if count == 3:
            if total == n:
                return 1
            else:
                return 0
        if cur_idx >= len(prime_num):
            return 0
        return dfs(cur_idx + 1, count, total) + dfs(cur_idx + 1, count + 1, total + prime_num[cur_idx])

    prime_num = sieve(n)
    return dfs(0, 0, 0)


if __name__ == "__main__":
    print(solution(33))
    print(solution(9))
