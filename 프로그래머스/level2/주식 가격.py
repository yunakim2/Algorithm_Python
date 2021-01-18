from collections import deque


def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        timer = 0
        price = prices.popleft()
        for price_ck in prices:
            timer += 1
            if price_ck < price:
                break
        answer.append(timer)

    return answer


if __name__ == "__main__":
    print(solution([1, 2, 3, 2, 3]))
