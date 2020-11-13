tmp = inp = int(input())
count = 0
while True:
    a1 = tmp // 10
    a2 = tmp % 10
    res = a1 + a2
    count += 1
    tmp = int(str(tmp % 10) + str(res%10))

    if (inp == tmp):
        break
print(count)
