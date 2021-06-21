
def removeStr(string, remove) :
    str_list = list(string)
    check_list = list(remove)

    while True:
        for i in range(len(str_list)):
            if i + len(check_list) < len(str_list)and str_list[i] == check_list[0]:
                for j in range(len(check_list)):
                    print(i,j)
                    if str_list[i+j] != check_list[j]:
                        break
                else:
                    k = 0
                    while k < len(check_list) :
                        print('pop-',i)
                        str_list.pop(i)
                        k+=1
                    break
            print(str_list)
        else:
            return ''.join(str_list)



if __name__ == '__main__':
    print(removeStr('aaabbbb', 'ab'))