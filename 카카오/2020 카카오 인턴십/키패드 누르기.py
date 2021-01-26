
def get_distance(hand, number):
    location = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
                '4': (1, 0), '5': (1, 1), '6': (1, 2),
                '7': (2, 0), '8': (2, 1), '9': (2, 2),
                '*': (3, 0), '0': (3, 1), '#': (3, 2)}
    x_hand, y_hand = location[hand]
    x_number, y_number = location[number]
    return abs(x_hand - x_number) + abs(y_hand - y_number)


def solution(numbers, hand):
    answer = ''
    left = ['1', '4', '7']
    right = ['3', '6', '9']
    rHand : str = '#'
    lHand: str = '*'
    for i in numbers:
        i= str(i)
        if i in left:
            answer += 'L'
            lHand =i
        elif i in right:
            answer += 'R'
            rHand=i
        else:
            ldist = get_distance(lHand,i)
            rdist = get_distance(rHand,i)
            if (ldist == rdist):
                if hand == 'right':
                    answer += 'R'
                    rHand=i
                else:
                    answer += 'L'
                    lHand=i
            else:
                if (ldist > rdist):
                    answer += 'R'
                    rHand=i
                else:
                    answer += 'L'
                    lHand=i

    return answer

arr = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
print(solution(arr, "right"))
