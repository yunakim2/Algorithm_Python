def solution(skill, skill_trees):
    skill_list = list(skill)
    answer = 0
    for skill_item in skill_trees:
        lists = list(skill_item)
        correct = 0
        for item in lists:
            if item in skill_list:
                if skill_list[correct] == item:
                    correct += 1
                else:
                    break
        else:
            answer += 1

    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
