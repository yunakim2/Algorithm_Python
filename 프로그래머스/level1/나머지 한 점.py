from collections import defaultdict


def solution(v):
    x_list = defaultdict(int)
    y_list = defaultdict(int)
    for x, y in v:
        x_list[x] += 1
        y_list[y] += 1

    def sort_dict(lists):
        return sorted(lists.items(), key=lambda x: x[1])

    answer = [sort_dict(x_list)[0][0], sort_dict(y_list)[0][0]]
    return answer


if __name__ == '__main__':
    print(solution([[1, 4], [3, 4], [3, 10]]))
