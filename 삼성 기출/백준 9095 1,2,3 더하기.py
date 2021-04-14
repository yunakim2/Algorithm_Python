'''정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성하시오.'''


def backtracking(num, sum):
    if sum == num:
        global ans
        ans += 1
        return
    if sum > num:
        return
    for i in range(1, 4):
        backtracking(num, sum + i)


if __name__ == '__main__':
    for _ in range(int(input())):
        number = int(input())
        ans = 0
        backtracking(number, 0)
        print(ans)
