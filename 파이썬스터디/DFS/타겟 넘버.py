def solution(numbers, target):
    # 타겟 넘버 갯수
    cnt = 0
    def dfs(i, total):
        if i == len(numbers):
            if total == target:
                nonlocal cnt
                cnt += 1
        else:
            dfs(i + 1, total + numbers[i])
            dfs(i + 1, total - numbers[i])

    dfs(0, 0)
    return cnt


print(solution([1,1,1,1,1],3))