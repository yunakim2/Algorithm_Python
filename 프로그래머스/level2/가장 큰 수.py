def solution(numbers):
    combi_number = []
    bigger_number = ''
    for number in numbers:
        tmp_number = (str(number)*4)[:4]
        combi_number.append([''.join(tmp_number), number])
    combi_number.sort(reverse=True)
    for _, item in combi_number:
        bigger_number += str(item)
    return str(int(bigger_number))

if __name__ == '__main__':
    print(solution([0,0,0,1000]))
    print(solution([6,10,2]))
    print(solution([0,0,0,0]))
