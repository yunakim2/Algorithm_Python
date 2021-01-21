# def solution(citations):
#     citations.sort()
#     for idx , citation in enumerate(citations):
#         if citation >= len(citations) - idx :
#             return len(citations) - idx
#     return 0


def solution(citations):
    citations.sort(reverse=True)
    for idx , citation in enumerate(citations):
        if idx >= citation:
            return idx
    return len(citations)

if __name__ == '__main__':
    print(solution([3,0,6,1,5])) # 3
    print(solution([12, 11, 10, 9, 8, 1])) # 5
    print(solution([6,6,6,6,6,1]))
    print(solution([4,4,4]))
    print(solution([0,1]))
    print(solution([0, 1, 1, 3, 3, 5, 6, 7, 11, 13, 111, 1111, 10000] ))
    print(solution([5, 5, 5, 5]))
    print(solution([0,1,1]))
    print(solution([10,9,4,1,1]))