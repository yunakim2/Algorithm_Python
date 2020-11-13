

def solution(s):
    c = 0
    answer = ''
    for i in range(len(s)):
        if s[i] == ' ':
            c = 0
            answer += ' '
        elif c%2 == 0:
            if s[i]!= ' ':
                answer += s[i].upper()
            elif s[i] == ' ':
                answer += ' '
            c += 1
        elif c%2 != 0:
            if s[i]!= ' ':
                answer += s[i].lower()
            elif s[i] == ' ':
                answer += ' '
            c += 1
    return answer

print(solution("heelo Work"))