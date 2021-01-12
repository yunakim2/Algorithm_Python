from collections import deque


def solution(reqs):
    answer = []
    items = deque()
    for i, item in enumerate(reqs):
        items.append([i, item])
    queue = [items.popleft()]
    timer = 0
    while queue:
        if len(queue) != 0:
            queue.sort(key=lambda x: x[1][0])
            item = queue.pop()

        for _ in range(item[1][1]):
            timer += 1
            if timer % 3 == 0:
                if items:
                    queue.append(items.popleft())
        else:
            answer.append(item[0] + 1)
            if len(queue) == 0:
                if len(items) != 0:
                    queue.append(items.popleft())

    return answer
