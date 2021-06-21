from collections import deque


def solution(inputString):
    answer = 0
    inputString = deque(list(inputString))
    while True:
        if answer == 0:
            answer = int(inputString.popleft())
        if answer%10 == int(inputString[0]):
            answer = 10 * (answer // 10 +1) + int(inputString.popleft())
            print(answer)
        else:
            break

    for number in inputString:
        number = int(number)
        if answer < number:
            answer = number
        else:
            tmp = answer // 10
            check_num = 10 * (tmp+1) + number
            print('num',number,answer,check_num)
            if answer < check_num:
                if answer % 10 >= check_num % 10:
                    if check_num % 10 != 0:
                        if answer <= check_num - 10:
                            answer = check_num - 10
                        else:
                            answer = check_num
                else :
                    if answer <= check_num-10:
                        answer = check_num-10
        print(answer)


    return answer


if __name__ == '__main__':
    # print(solution('12345'))
    # print(solution('2349101'))
    print(solution('7777729'))
    # print(solution('7234032479947'))
