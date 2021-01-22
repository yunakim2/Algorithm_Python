def solution(l, v):
    v.sort()

    def check(d):
        check_bright = [False for _ in range(l + 1)]
        for item in v:
            min_v = item - d
            max_v = item + d
            if min_v < 0 :
                min_v = 0
            if max_v > l:
                max_v = l
            f
        return check_bright

    d = set()
    for idx, item in enumerate(v):
        if 1 <= idx < len(v):
            tmp_item = item - v[idx-1]
            if tmp_item > 0:
                d.add(tmp_item)
        elif idx == 0:
            tmp_item = item - 0
            if tmp_item > 0:
                d.add(tmp_item)
    while d:
        check_d = d.pop()
        check_b = check(check_d)
        if False not in check_b:
            return check_d



if __name__ == "__main__":
    print(solution(15, [15, 5, 3, 7, 9, 14, 0]))
    print(solution(5, [2, 5]))
