def solution(N, number):
    def blend(number1, number2):
        blended = set()
        for num1 in number1:
            for num2 in number2:
                blended.add(num1 + num2)
                blended.add(num1 - num2)
                blended.add(num1 * num2)
                if num2 != 0:
                    blended.add(num1 // num2)
        return blended

    dp = [set() for _ in range(8 + 1)]
    for count in range(1, 8 + 1):
        dp[count].add(int(str(N) * count))
        for i in range(1, count):
            dp[count] |= blend(dp[i], dp[count - i])
        print(dp[count])
        if number in dp[count]:
            return count
    return -1


if __name__ == "__main__":
    print(solution(5, 12))
