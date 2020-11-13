def solution(s):
    small = []
    big = []
    for i in s :
        if 'a'<=i<='z' :
            small.append(i)
        else :
            big.append(i)
    small.sort(reverse=True)
    big.sort(reverse=True)

    return ''.join(small)+''.join(big)


print(solution("Zbcdefg"))