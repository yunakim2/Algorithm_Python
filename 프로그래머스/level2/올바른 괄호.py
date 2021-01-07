def solution(s):
    stack = []
    for bracket in s:
        if bracket == '(':
            stack.append(bracket)
        else:
            if len(stack) >= 1 and stack[-1] == '(':
                stack.pop()
            else:
                return False

    return len(stack) == 0


print(solution("))))()"))
