from collections import deque


def solution(board, skill):
    answer = 0
    warning = deque([])
    for types, r1, c1, r2, c2, degree in skill:
        if types ==1:
            
    for types, r1, c1, r2, c2, degree in skill:
        tmp_warning = deque([])
        while warning:
            x, y = warning.popleft()
            if r1 <= x <= r2 and c1 <= y <= c2:
                if types == 1 and board[x][y] - degree <= 0:
                    tmp_warning.append((x,y))
        warning = tmp_warning

    print(len(board)*len(board[0]))
    print(len(warning))
    return len(board) * len(board[0]) - len(warning)

if __name__ == "__main__":
    print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
                   [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
