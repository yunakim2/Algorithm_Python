def solution(priorities, location):
    answer = 1
    sorted_priorities = priorities[::]
    sorted_priorities.sort()
    while sorted_priorities:
        for i in range(len(priorities)):
            if priorities[i] == sorted_priorities[-1]:
                if i == location:
                    return answer
                sorted_priorities.pop()
                answer += 1


