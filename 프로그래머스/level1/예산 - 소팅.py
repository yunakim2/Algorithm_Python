def solution(d, budget):
    d.sort()
    answer = 0
    while budget > 0 and d:
        budget = budget - d.pop(0)
        if budget >= 0:
            answer += 1
    return answer

if __name__ == '__main__':
    print(solution([1,3,2,5,4]	, 9))
    print(solution([2,2,3,3],10))