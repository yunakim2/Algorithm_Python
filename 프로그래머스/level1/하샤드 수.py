def solution(x):
    answer = True
    data = sum([int(i) for i in str(x)])
    if x%data !=0 : answer = False
    return answer

print(solution(10))