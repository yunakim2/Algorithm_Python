def solution(genres, plays):
    answer = []
    item_d = dict()
    tmp_s = set(genres)
    for i in tmp_s:
        item_d[i] = 0
        for idx, j in enumerate(genres):
            if j == i:
                item_d[i] += plays[idx]

    item_d = sorted(item_d.items(), key= lambda x : -x[1])

    for item in item_d:
        tmp_item = []
        for idx, j in enumerate(genres):
            if j == item[0]:
                tmp_item.append((idx, plays[idx]))
        tmp_item = sorted(tmp_item, key= lambda x : (-x[1], x[0]))

        if len(tmp_item) >= 2:
            answer.append(tmp_item[0][0])
            answer.append(tmp_item[1][0])
        else:
            answer.append(tmp_item[0][0])

    return answer


if __name__ == "__main__":
    print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))
