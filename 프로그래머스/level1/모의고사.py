def solution(answers):
    answer = []
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    sc = [0,0,0]
    for i in range(len(answers)) :
        if answers[i] == s1[i%5] : sc[0] +=1
        if answers[i] == s2[i%8] : sc[1] +=1
        if answers[i] == s3[i%10] : sc[2] +=1

    for j in range(3) :
        if sc[j] == max(sc) :
            answer.append(j+1)

    return answer


print(solution([5]))