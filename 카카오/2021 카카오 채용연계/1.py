from collections import deque
def solution(s):
    answer = ''
    numbering = {'zero' : '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    s = deque(list(s))
    while s:
        ch = s.popleft()
        if ch in numbering.values():
            answer += ch
            continue
        else:
            tmp = ch
            while s and s[0] not in numbering.values():
                tmp += s.popleft()
                if tmp in numbering.keys():
                    break
            answer += numbering[tmp]

    return int(answer)


if __name__ == "__main__":
    print(solution("23four5six7"))
