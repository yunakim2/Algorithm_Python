data = """5
R R R U D D"""
data = data.split("\n")
N = int(data[0])
move = data[1].split()
print(move)
start = [1, 1]
dxy = {'L': (0,-1), 'R': (0,1), 'D': (1,0), 'U': (-1,0)}


def check(x, y):
    return 1 <= x <= N and 1 <= y <= N


for m in move:
    dx, dy = dxy[m]
    start_x, start_y = start
    if check(start_x+dx, start_y+dy):
        start = [start_x + dx, start_y + dy]

print(start)