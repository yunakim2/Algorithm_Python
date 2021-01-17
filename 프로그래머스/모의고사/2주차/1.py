def solution(seat):
    answer = 0
    check_seat = set()
    for person in seat:
        if tuple(person) not in check_seat:
            check_seat.add(tuple(person))
            answer += 1

    return answer





if __name__ == "__main__":
    print(solution([[1,1],[2,2],[3,3]]))
    print(solution([[1,1],[2,1],[1,2],[3,4],[2,1],[2,1]]))
