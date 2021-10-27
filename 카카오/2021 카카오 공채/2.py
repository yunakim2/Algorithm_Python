def prime(n):
    if n in (0, 1):
        return False
    if n == 2:
        return True
    else:
        s = int(n ** 0.5)
        for i in range(2, s + 1):
            if n % i == 0:
                return False
        return True


def n_format(n, q):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]


def solution(n, k):
    answer = n_format(n, k).split('0')
    res = 0
    for i in answer:
        if i=='':
            continue
        if prime(int(i)):
            res += 1
    return res


if __name__ == "__main__":
    print(solution(437674, 3))
