n = 1260
money = [500, 100, 50, 10]
cnt = 0
for m in money:
    cnt += n // m
    n %= m

print(cnt)
