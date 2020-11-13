
def check_num(n) :
    if n == 2 :
        return True
    else :
        m = int(n ** 0.5)
        for i in range(2,m+1) :
            if n%i == 0 :
                return False
        return True
def solution(n):
    answer = 0
    for i in range(2,n+1):
        if check_num(i) : answer+=1

    return answer

print(solution(2))