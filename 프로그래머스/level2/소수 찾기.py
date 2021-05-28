from itertools import combinations


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


def solution(numbers):
    list_n = list(numbers)
    answer = 0
    check_list = set()
    boolean_check = [False] * len(list_n)

    def bruteforce(num, idx):
        nonlocal answer
        if idx == len(list_n):
            if num == '':
                return
            if int(num) not in check_list:
                check_list.add(int(num))
                if prime(int(num)):
                    answer += 1

            return

        for index, i in enumerate(list_n):
            if boolean_check[index]:
                continue
            bruteforce('', idx + 1)
            boolean_check[index] = True
            bruteforce(num + i, idx + 1)
            boolean_check[index] = False

    bruteforce('', 0)
    return answer