
data = """3 3
3 1 2
4 1 4
2 2 2"""

data = data.split("\n")
n, m = map(int, data[0].split())
arr = []
small= []
arr.append(map(int,data[1].split()))
arr.append(map(int,data[2].split()))
arr.append(map(int,data[3].split()))

for i in range(n):
    small.append(min(arr[i]))

print(max(small))