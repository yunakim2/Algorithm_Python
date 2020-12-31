def solution(strings, n):
    strings.sort(key = lambda x: (x[n],x))
    return strings

print(solution(["abce","abcd","cdx"],2))


