def solution(board, nums):
    answer = 0
    set_num = set(nums)
    N = len(board)

    def check_bingo(check_bg):
        return len(check_bg) == N

    # 가로 빙고 검사
    for i in range(N):
        check_bg = []
        for j in range(N):
            if board[i][j] in set_num:
                check_bg.append(True)
        if check_bingo(check_bg):
            answer += 1

    # 세로 빙고 검사
    for i in range(N):
        check_bg = []
        for j in range(N):
            if board[j][i] in set_num:
                check_bg.append(True)
        if check_bingo(check_bg):
            answer += 1

    check_bg = []
    for i in range(N):
        if board[i][i] in set_num:
            check_bg.append(True)

    if check_bingo(check_bg):
        answer += 1

    check_bg = []
    for i in range(N - 1, -1, -1):
        if board[N - i - 1][i] in set_num:
            check_bg.append(True)

    if check_bingo(check_bg):
        answer += 1

    return answer


if __name__ == "__main__":
    print(solution([[11, 13, 15, 16], [12, 1, 4, 3], [10, 2, 7, 8], [5, 14, 6, 9]], [14, 3, 2, 4, 13, 1, 16, 11, 5, 15]))
    print(solution([[6,15,17,14,23],[5,12,16,13,25],[21,4,2,1,22],[10,20,3,18,8],[11,9,19,24,7]],[15,7,2,25,9,16,12,18,5,4,10,13,20]))
