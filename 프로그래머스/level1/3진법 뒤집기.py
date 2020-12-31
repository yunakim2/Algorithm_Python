def solution(n):
    temp = []
    while n >= 3 :
        temp.append(str(n%3))
        n = n//3

    temp.append(str(n))
    nums = ''.join(temp)
    answer = int(nums,3)
    return answer



print(solution(125))