def solution(n):
    if n !=1 :
        for i in range (n) :
            if (i*i) == n :
                answer = i+1
                break
            else :
                answer= -1

        if answer != -1 :
            return answer*answer
        else : return  -1
    else :
        return 4



print(solution(1))