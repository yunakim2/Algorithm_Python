def solution(s):
    answer = True
    if (s.count('p') + s.count('P')) == (s.count('y') + s.count('Y')):
        answer = True
    else:
        answer = False

    if s.count('p') + s.count('P') + s.count('y') + s.count('Y') == 0:
        answer = True

    return answer