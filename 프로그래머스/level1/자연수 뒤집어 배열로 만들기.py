def solution(n):
    n = list(str(n))
    n.reverse()
    n = list(map(int,n))
    return n
print(solution(12345))

str.upp