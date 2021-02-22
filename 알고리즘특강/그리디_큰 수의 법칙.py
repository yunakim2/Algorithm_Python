data = """5 8 3
2 4 5 4 6"""

data = data.split("\n")
n, m, k = map(int, data[0].split())
data = list(map(int, data[1].split()))
data.sort()
cnt = 0

while m:
    for i in range(k):
        cnt += data[-1]
        m -= 1
        if m == 0:
            break
    if m >= 1:
        cnt += data[-2]
        m -= 1

print(cnt)