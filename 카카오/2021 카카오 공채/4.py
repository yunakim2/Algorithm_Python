def solution(n, info):
    answer = []
    sum_list = []

    def dfs(idx, win_lion, cnt):
        if idx == 11 and cnt == 0:
            if False not in visited:
                sums = 0
                sums_peach = 0
                for idx in range(len(info)):
                    if info[idx] == 0 and win_lion[idx] == 0:
                        continue
                    else:
                        if win_lion[idx] > info[idx]:
                            sums += 10 - idx
                        else:
                            sums_peach += 10 - idx

                if sums - sums_peach > 0:
                    answer.append(tuple(win_lion))
                    sum_list.append(sums - sums_peach)
            return

        for i in range(idx, len(info)):
            if visited[i]:
                continue
            visited[i] = True
            if info[i] + 1 <= cnt:
                win_lion[i] = info[i] + 1
                dfs(i + 1, win_lion, cnt - info[i] - 1)
            if i == 10 and cnt > 0:
                win_lion[i] = cnt
                cnt = 0
            else:
                win_lion[i] = 0
            dfs(i + 1, win_lion, cnt)
            visited[i] = False

    visited = [False] * 11
    dfs(0, [0] * 11, n)
    if sum_list:
        max_sum = max(sum_list)
        if sum_list.count(max_sum) > 1:
            tmp_answer = []
            for idx, l in enumerate(sum_list):
                if l == max_sum:
                    tmp_answer.append(list(answer[idx]))
            tmp_index = []
            for tmp in tmp_answer:
                for idx, item in enumerate(tmp[::-1]):
                    if item > 0:
                        tmp_index.append(idx)
                        break
            return list(tmp_answer[tmp_index.index(min(tmp_index))])
        else:
            return list(answer[sum_list.index(max_sum)])
    else:
        return [-1]


if __name__ == "__main__":
    # print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
    # print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
    # print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
    print(solution(	10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))