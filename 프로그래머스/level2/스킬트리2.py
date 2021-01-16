def solution(skills_order, skill_tree):
    skills_order_set = set(skills_order)
    filtered = list(filter(lambda skill: skill in skills_order_set, skill_tree))
    return filtered == skills_order[:len(filtered)]
