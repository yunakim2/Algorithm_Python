from collections import deque

def calculater(cal):
    re_item = 0
    cal = deque(cal)
    while cal:
        number = cal.popleft()
        if number == '+' or number == '-' or number == '*':
            if number == '+':
                re_item = re_item + int(cal.popleft())
            elif number == '-':
                re_item = re_item - int(cal.popleft())
            else:
                re_item = re_item * int(cal.popleft())
        else:
            if re_item == 0:
                re_item = int(number)

    return re_item

def dfs(queue, length):
    global ans
    if length == len(queue):
        ans = max(ans, calculater(queue))
        return

    for idx in range(length, len(queue)-1, 2):
        dfs(queue, idx+2)
        check = queue[:]
        if check[idx] == '+':
            check[idx - 1] = int(queue[idx - 1]) + int(queue[idx + 1])
            check[idx + 1] = 0
            check[idx] = '+'

        elif check[idx] == '-':
            check[idx - 1] = int(queue[idx - 1]) - int(queue[idx + 1])
            check[idx + 1] = 0
            check[idx] = '+'

        else:
            check[idx - 1] = int(queue[idx - 1]) * int(queue[idx + 1])
            check[idx] = '+'
            check[idx + 1] = 0
        if idx+2 == n:
            dfs(check, idx+2)
        else:
            dfs(check, idx+4)


if __name__ == '__main__':
    n = int(input())
    item = list(input())
    ans = float('-inf')
    dfs(item, 1)
    print(ans)
