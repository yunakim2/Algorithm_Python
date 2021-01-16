def solution(s):
    stack = []
    for char in s:
        if not stack:
            stack.append(char)
        elif stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return 1 if not stack else 0


if __name__ == "__main__":
    print(solution("baabaa"))
    print(solution("cdcd"))
