def solution(id_list, report, k):
    answer = []
    warning = dict()
    user_list = dict()

    for user in id_list:
        user_list[user] = []

    for re in report:
        user, stop = re.split()
        if stop not in user_list[user]:
            user_list[user].append(stop)
            if stop in warning:
                warning[stop] += 1
            else:
                warning[stop] = 1

    for key, values in warning.items():
        if values >= k:
            answer.append(key)

    answer = set(answer)
    result = []
    for users, check in user_list.items():
        check = set(check)
        total = len(check)
        tmp = len(check.difference(answer))
        result.append(total - tmp)

    return result


if __name__ == "__main__":
    print(solution(["muzi", "frodo", "apeach", "neo"],
                   ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
    print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
