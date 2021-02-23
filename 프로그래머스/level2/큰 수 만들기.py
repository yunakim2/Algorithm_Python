def solution(number, k):
    stack = []
    for idx, num in enumerate(number):
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
        if k == 0:
            stack += number[idx:]
            break
        stack.append(num)

    stack = stack[:-k] if k > 0 else stack
    return ''.join(stack)


if __name__ == "__main__":
    print(solution("1924", 2))
    print(solution("1231234", 3))
    print(solution("4177252841", 4))
    print(solution("4444", 2))
