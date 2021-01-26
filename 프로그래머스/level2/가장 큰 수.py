def solution(numbers):
    answer = []
    ans = ''
    for number in numbers:
        tmp_number = [str(i) for i in str(number)]
        while len(tmp_number) < 4:
            for i in str(number):
                tmp_number.append(i)
            tmp_number = tmp_number[0:4]
        answer.append([str(''.join(tmp_number)), number])
    answer.sort(reverse=True)
    for _, item in answer:
        ans += str(item)
    return str(0) if not int(ans) else ans

if __name__ == '__main__':
    print(solution([0,0,0,1000]))
    print(solution([6,10,2]))
    print(solution([0,0,0,0]))
