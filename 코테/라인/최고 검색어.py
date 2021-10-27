from collections import Counter


def solution(research, n, k):
    total = [[0] * len(research) for _ in range(26)]

    for day, re in enumerate(research):
        item_list = Counter(re)
        for key, item in item_list.items():
            total[int(ord(key) - 97)][day] = item

    total_dict = dict()
    for alpha, alpha_list in enumerate(total):
        if sum(alpha_list) == 0:
            continue
        total_dict[chr(alpha + 97)] = alpha_list

    true_list = dict()
    for key, item_list in total_dict.items():
        true_list[key] = 0
        for idx, i in enumerate(item_list):
            if i >= k and idx + n - 1 < len(item_list):
                sum_check = i
                for check_idx in range(idx + 1, idx + n):
                    if item_list[check_idx] < k:
                        break
                    else:
                        sum_check += item_list[check_idx]
                if sum_check >= 2 * n * k:
                    true_list[key] += 1

    true_list = sorted(true_list.items(), key=lambda x: -x[1])
    print(true_list)
    if true_list[0][0] == 0:
        return "None"
    else:
        return true_list[0][0]


if __name__ == "__main__":
    print(solution(["abaaaa", "aaa", "abaaaaaa", "fzfffffffa"], 2, 2))
    print(solution(["yxxy", "xxyyy", "yz"], 2, 1))
    print(solution(["xy", "xy"], 1, 1))
