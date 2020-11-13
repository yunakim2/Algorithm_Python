def solution(a, b):
    total = 0
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(a-1) :
        total += month[i]
    total +=b-1
    answer = day[total%7]
    return answer


print(solution(5,24))