from collections import deque
import heapq

def insertionSort(data):
    for i in range(1, len(data)):
        for j in range(i-1, -1, -1):
            if data[i]<data[j]:
                data[i], data[j] = data[j], data[i]
                i -= 1
            else:
                break
    return data


def solution(n, k, cmd):
    answer = ''
    result = [i for i in range(n)]
    delete = []
    for c in cmd:
        # print('c',c)
        # print('k',k)
        # print(result)
        if c == 'C':
            if k == len(result)-1:
                delete.append(result[k])
                result.remove(result[k])
                k = len(result)-1
            else:
                delete.append(result[k])
                result.remove(result[k])

        elif c == 'Z':
            t = delete.pop()
            result.append(t)
            result = insertionSort(result)
            if result[k] >= t:
                k += 1

        else:
            tmp = list(c.split())
            if tmp[0] == 'D':
                k += int(tmp[1])
            else:
                k -= int(tmp[1])

        # print('c', c)
        # print('k', k)
        # print(result)

    result = set(result)
    for i in range(n):
        if i in result:
            answer += 'O'
        else:
            answer += 'X'

    return answer

if __name__ == "__main__":
    print(solution(8,2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))