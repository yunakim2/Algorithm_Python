def solution(max_weight, specs, names):
    weights = 0
    answer = 1
    dict_specs = {item: int(weight) for item, weight in specs}
    for name in names:
        weights += dict_specs[name]
        if weights > max_weight:
            weights = dict_specs[name]
            answer += 1

    return answer


if __name__ == '__main__':
    print(solution(200, [["toy", 70], ["snack", 200]], ["toy", "snack", "toy"]))
