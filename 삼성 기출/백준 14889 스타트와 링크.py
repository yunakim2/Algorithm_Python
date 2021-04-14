import sys
import time


def backtracking(idx, start):
    global min_value
    if idx == number:
        sum_value = 0
        diff_value = 0
        link_team = list((total- set(start_team)))
        for i in range(number):
            for j in range(i+1, number):
                sum_value += power[start_team[i]][start_team[j]] + power[start_team[j]][start_team[i]]
                diff_value += power[link_team[i]][link_team[j]] + power[link_team[j]][link_team[i]]

        min_value = min(min_value, abs(sum_value-diff_value))
        return

    for i in range(start, n):
        if check[i]:
            continue
        check[i] = True
        start_team[idx] = i
        backtracking(idx+1, i+1)
        check[i] = False

if __name__ == '__main__':
    start = time.time()  # 시작 시간 저장

    n = int(sys.stdin.readline())
    number = n//2
    power = []
    total = set(range(0,n))
    for i in range(n):
        power.append(list(map(int,sys.stdin.readline().split())))
    min_value = float('inf')
    start_team = [0] * number
    check = [False] * n
    backtracking(0,0)
    print(min_value)
    print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간