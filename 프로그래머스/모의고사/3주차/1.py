from itertools import combinations


def solution(nums):
    def is_prime(n):
        if n == 2:
            return True
        else:
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

    return len([num for num in combinations(nums, 3) if is_prime(sum(num))])


if __name__ == "__main__":
    print(solution([1, 2, 3, 4]))
    print(solution([1, 2, 7, 6, 4]))
