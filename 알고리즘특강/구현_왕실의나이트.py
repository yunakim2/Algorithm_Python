data = """b1"""

list_a = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
row = int(data[1])
col = int(list_a[data[0]])
N = 8
dxy = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
cnt = 0
for dx, dy in dxy:
    if 1 <= dx + row <= N and 1 <= dy + col <= N:
        cnt += 1

print(cnt)
