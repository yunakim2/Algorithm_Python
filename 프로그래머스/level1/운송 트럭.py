def solution(max_weight, specs, names):
    weight = 0
    answer = 0
    dict_specs = dict()
    for spec in specs:
        dict_specs[spec[0]] = spec[1]

    if len(names) >= 1:
        answer += int(1)

    for name in names:
        print("name::",name, "answer::",answer,"weight ::",weight)
        if weight + int(dict_specs[name]) < max_weight:
            weight += int(dict_specs[name])
        else:
            weight = 0
            answer += int(1)

    return answer


if __name__ == '__main__':
    print(solution(200, [["toy", 70], ["snack", 200]], ["toy", "toy", "snack"]))
