def solution(strings, n):
    middle = []
    for i in strings :
        middle.append(i[n])
    middle.sort()
    strings.sort()
    print(middle)
    for i in range (len(middle)) :
        for j in strings :
            if j.find(middle[i]) == n :
                middle[i] = j
                strings.remove(j)
                continue

    return middle

print(solution(["abce","abcd","cdx"],2))


