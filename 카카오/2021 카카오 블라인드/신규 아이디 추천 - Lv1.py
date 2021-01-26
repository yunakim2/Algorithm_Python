import string

def level_4 (answer):
    # level 4
    while answer and answer[0] == '.':
        answer.pop(0)
    while answer and answer[-1] == '.':
        answer.pop()
    return answer

# level 2
def level_2(new_id):
    check_id = set(['-', '_', '.'])
    for word in new_id:
        if word not in string.punctuation:
            continue
        else:
            if word not in check_id:
                new_id = new_id.replace(word, '')
    return new_id

def solution(new_id):
    answer = []

    new_id = new_id.lower() # level 1
    new_id = level_2(new_id) # level 2
    # level 3
    for idx, char in enumerate(new_id):
        if char == '.' and idx < len(new_id) -1 and new_id[idx+1] =='.' :
            continue
        else:
            answer.append(char)
    answer = level_4(answer) # level 4
    # level 5
    if len(answer) == 0:
        answer = ['a']
    # level 6
    if len(answer) >= 16:
        answer = answer[0:15]
        answer = level_4(answer)
    # level 7
    if len(answer) <= 2:
        while len(answer) < 3:
            answer.append(answer[-1])
    return ''.join(answer)


if __name__ == "__main__":
    print(solution("...abc..."))
    print(solution("...!@BaT#*..y.abcdefghijklm"))
    # print(solution("z-+.^."))
    # print(solution("=.="))
    print(solution(".......b"))
    print(solution("123_.def"))
    print(solution(".1."))
    print(solution("3.2............3"))
    print(solution("~!@#$%^&*()=+[{]}:?,<>"))