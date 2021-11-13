def solution(rows, columns, queries):
    answer = []
    board = [[(i) * columns + j + 1 for j in range(columns)] for i in range(rows)]

    for x1, y1, x2, y2 in queries:
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        mins = board[x1][y1]
        new_board = []
        for j in range(len(board)):
            new_board.append(board[j][:])

        for i in range(y1, y2):
            new_board[x1][i + 1] = board[x1][i]
            mins = min(mins, board[x1][i])
            new_board[x2][i] = board[x2][i + 1]
            mins = min(mins, board[x2][i + 1])

        for i in range(x1, x2):
            new_board[i + 1][y2] = board[i][y2]
            mins = min(mins, board[i][y2])
            new_board[i][y1] = board[i + 1][y1]
            mins = min(mins, board[i + 1][y1])

        board = new_board
        answer.append(mins)

    return answer