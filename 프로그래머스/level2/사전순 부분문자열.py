def solution(s):
    stack = []
    for char in s:
        while stack and stack[-1] < char:
            stack.pop()
        stack.append(char)

    return ''.join(stack)


if __name__ == "__main__":
    print(solution("xyb"))
    print(solution("yxyc"))
