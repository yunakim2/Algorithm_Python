def solution(dartResult):
    answer = 0
    dart = list(dartResult)
    dart = list(reversed(dart))
    index = -1
    num = 0
    renum = 0
    while len(dart) > 0:
        item = dart.pop()
        if item != 'S' and item != 'D' and item != 'T' and item != '*' and item != '#':
            reitem = dart.pop
            if  reitem!= 'S' and reitem != 'D' and reitem != 'T' and reitem != '*' and reitem != '#':
                num = int(item+reitem)
            else:
                num = int(item)
                dart.append(reitem)
        else:
            if item == 'S' or item == 'D' or item == 'T':
                index += 1
                if item == 'S':
                    num = num
                elif item == 'D':
                    num = num ** 2
                else:
                    num = num ** 3

                if len(dart) > 0:
                    mode = dart.pop
                    if mode == '*' or mode == '#':
                        if mode == '*':
                            num = num * 2
                            answer -= renum
                            renum = renum * 2
                            answer = answer + renum + num
                        if mode == '#':
                            num = -num
                            answer = answer + num

                    else:
                        dart.append(mode)
                        answer = answer + num
                else:
                    answer = answer + num

                renum = num

    return answer


# def solution(dartResult):
#     answer = []
#     dartResult = dartResult.replace('10','k')
#     point = ['10' if i == 'k' else i for i in dartResult]
#     print(point)
#
#     i = -1
#     sdt = ['S', 'D', 'T']
#     for j in point:
#         if j in sdt :
#             answer[i] = answer[i] ** (sdt.index(j)+1)
#         elif j == '*':
#             answer[i] = answer[i] * 2
#             if i != 0 :
#                 answer[i - 1] = answer[i - 1] * 2
#         elif j == '#':
#             answer[i] = answer[i] * (-1)
#         else:
#             answer.append(int(j))
#             i += 1
#     return sum(answer)

print(solution("1S*2T*3S"))
