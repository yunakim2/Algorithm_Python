def solution(skill, skill_trees):
    answer = 0
    skill_list = list(skill)
    for skill_item in skill_trees:
        lists = list(reversed(skill_item))
        correct = 0
        flag = False
        while len(lists) >= 0:
            if len(lists) == 0:
                flag = True
                break
            item = lists.pop()
            if item in skill_list:
                if skill_list[correct] == item:
                    correct += 1
                else:
                    flag = False
                    break
        if flag:
            answer += 1

    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
