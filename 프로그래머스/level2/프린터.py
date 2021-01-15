def solution(priorities, location):
    answer = 1
    lists = priorities[::]
    lists.sort()
    while lists:
        for i in range(len(priorities)):
            if priorities[i] == lists[-1]:
                if i == location:
                    return answer
                lists.pop()
                answer += 1


