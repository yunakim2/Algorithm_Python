def solution(s):
    heap = list(map(int,s.split()))
    heap.sort()
    answer = str(heap[0]) + " "+ str(heap[-1])
    return answer



print(solution("-1 -2 -3 -4"))