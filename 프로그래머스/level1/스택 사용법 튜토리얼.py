def solution(sentence):
    stack = []
    for alphabet in sentence:
        while stack and stack[-1] == alphabet:
            stack.pop()
        stack.append(alphabet)
    return ''.join(stack)


if __name__ == "__main__":
    print(solution("aaabbbcabbccc"))