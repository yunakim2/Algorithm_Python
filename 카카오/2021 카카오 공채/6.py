from collections import deque


def solution(board, skill):
    for types, r1, c1, r2, c2, degree in skill:
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if types == 1:
                    board[r][c] -= degree
                else:
                    board[r][c] += degree

    answer = [b for board_list in board for b in board_list if b > 0]
    return len(answer)


if __name__ == "__main__":
    print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
                   [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
