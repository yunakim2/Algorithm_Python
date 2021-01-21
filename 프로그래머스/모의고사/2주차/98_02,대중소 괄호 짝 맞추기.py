def solution(s):
    stack = []
    pair = {'(': ')', '{': '}', '[': ']'}
    for char in s:
        print(char)
        if char not in pair:
            if stack and pair[stack[-1]] == char:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)

    return False if stack else True