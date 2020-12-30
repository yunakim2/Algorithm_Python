def solution(s):
    temp = []
    for i in s:
        if i == '(':
            temp.append(i)
        else:
            if len(temp) >= 1 and temp[-1] == '(':
                temp.pop()
            else:
                return False

    if len(temp) == 0:
        return True
    else:
        return False


print(solution("))))()"))
