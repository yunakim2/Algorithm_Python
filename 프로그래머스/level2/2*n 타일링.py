def solution(n):
    dp = [0] * 60001
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1_000_000_007
    return dp[n]


if __name__ == '__main__':
    print(solution(4))
