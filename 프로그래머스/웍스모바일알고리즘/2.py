def setStr(string, k):
    str_list = list(string)

    while k > 0:
        check = False
        print(k, '---', ''.join(str_list))
        for i in range(len(str_list)):
            idx = i
            for j in range(i + 1, len(str_list)):
                if str_list[i] < str_list[j]:
                    idx = j
                    check = True
                    print('check!!')
            if check:
                break
        if check:
            print('i-', i, 'j-', j)
            str_list[i], str_list[idx] = str_list[idx], str_list[i]
            k -= 1
            continue
        else:
            break

    return ''.join(str_list)


if __name__ == '__main__':
    print(setStr('ccaaacbd', 2))
