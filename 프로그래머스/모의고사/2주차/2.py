def solution(s):
    stack = []
    open = {'{': 0, '(': 1, '[': 2}
    close = {'}': 0, ')': 1, ']': 2}
    for char in s:
        if char in close.keys():
            if stack and open[stack[-1]] == close[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return False if stack else True


if __name__ == "__main__":
    print(solution("{{}}"))
    print(solution("({})[]"))
    print(solution("("))
