def solution(numbers, hand):
    answer = ''
    left = '*'
    right = '#'

    def get_distance(hand, number):
        location = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
                    '4': (1, 0), '5': (1, 1), '6': (1, 2),
                    '7': (2, 0), '8': (2, 1), '9': (2, 2),
                    '*': (3, 0), '0': (3, 1), '#': (3, 2)}
        x_hand, y_hand = location[hand]
        x_number, y_number = location[number]
        return abs(x_hand - x_number) + abs(y_hand - y_number)

    for number in numbers:
        if number in (1, 4, 7):
            left = number
            answer += 'L'
        elif number in (3, 6, 9):
            right = number
            answer += 'R'
        else:
            left_d = get_distance(str(left), str(number))
            right_d = get_distance(str(right), str(number))
            if left_d > right_d:
                answer += 'R'
                right = number
            elif left_d < right_d:
                answer += 'L'
                left = number
            else:
                if hand == "right":
                    answer += 'R'
                    right = number
                else:
                    answer += 'L'
                    left = number

    return answer


if __name__ == "__main__":
    print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
