def solution(s, n):
    answer = ''
    for i in s :
        if i == ' ' :
            answer +=i

        else :
            if ord(i)>=97 and ord(i)<=122 :
                ord_i = ord(i) + n
                print(ord_i)
                if ord_i > ord('z') :
                    ord_i = ord_i - 123 +97
                    print(ord_i)
                    answer += chr(ord_i)
                else :
                    print(ord_i)
                    answer += chr(ord_i)
            else :
                ord_i = ord(i) + n
                print(ord_i)
                if ord_i > ord('Z'):
                    ord_i = ord_i - 91 + 65
                    print(ord_i)
                    answer += chr(ord_i)
                else:
                    print(ord_i)
                    answer += chr(ord_i)
    return answer

print(solution("AaZz",25))