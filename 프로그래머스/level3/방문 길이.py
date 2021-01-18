def solution(dirs):
    new_road = set()
    start = (0, 0)
    move = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    for direction in dirs:
        dx, dy = move[direction]
        new_x, new_y = start[0] + dx, start[1] + dy
        if -5 <= new_x <= 5 and -5 <= new_y <= 5:
            road_bottom = (start, (new_x, new_y))
            road_up = ((new_x, new_y), start)
            new_road.add(road_bottom)
            new_road.add(road_up)
            start = new_x, new_y
    return len(new_road)//2


if __name__ == "__main__":
    print(solution("ULURRDLLU"))
    print(solution("LULLLLLLU"))
    print(solution("UD"))
