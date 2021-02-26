import itertools


def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False

    for candidate in range(2, n + 1):
        if not is_prime[candidate]:
            continue
        for multiple in range(candidate * candidate, n + 1, candidate):
            is_prime[multiple] = False

    return [idx for idx, value in enumerate(is_prime) if value]


num = int(input())
sieve_list = sieve(num)
if sieve_list.count(num) == 1:
    print(1)
else:
    for sieve_num in sieve_list:
        if num % sieve_num == 0:
            if sieve_list.count(int(num / sieve_num)) == 1:
                print(1)
                break
    else:
        print(0)

