def checkHanNum(n):
    n1 = n // 100 % 10
    n2 = n // 10 % 10
    n3 = n % 10
    if n2 * 2 == n1 + n3: return 1

    return 0


num = int(input())

if num < 100:
    print(num)
else:
    res = 99
    for i in range(100, num + 1):
        res += checkHanNum(i)
    if num == 1000:
        res -= 1
    print(res)
