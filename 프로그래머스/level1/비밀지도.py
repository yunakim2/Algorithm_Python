def solution(n, arr1, arr2):
    answer = []

    def trans(num):
        temp = []
        while num >= 2:
            temp.append(str(num % 2))
            num = num // 2

        temp.append(str(num))
        temp = list(reversed(temp))
        nums = ''.join(temp)
        nums = nums.zfill(n)
        return nums

    for i in range(n):
        tmp1 = list(trans(arr1[i]))
        tmp2 = list(trans(arr2[i]))
        string = ""
        for j in range(n):
            if tmp1[j] == '1' or tmp2[j] == '1':
                string += "#"
            else:
                string += " "

        answer.append(string)

    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
