def solution(people, limit):
    answer = 0
    people.sort()
    boat = []
    for w in people:
        if not boat:
            boat.append([w,1])
        else:
            if int(boat[-1][0]) + w <= limit and boat[-1][1] <= 1:
                boat[-1][0] += w
                boat[-1][1] +=1
            else:
                boat.append([w,1])

    return len(boat)


if __name__ == "__main__":
    print(solution([70,50,80,50], 100))
    print(solution([70, 80, 50], 100))
