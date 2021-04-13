def solution(info, query):
    answer = []
    for q in query:
        query_item = list(q.split())
        lang = query_item[0]
        type = query_item[2]
        career = query_item[4]
        food = query_item[6]
        number = int(query_item[7])
        temp = []
        for item in info:
            info_item = list(item.split())
            if info_item[0] != lang and lang !='-':
                continue
            if info_item[1] != type and type !='-':
                continue
            if info_item[2] != career and career!='-':
                continue
            if info_item[3] != food and food!='-':
                continue
            if int(info_item[4]) < number:
                continue
            temp.append(item)
        answer.append(len(temp))
    return answer



if __name__ == "__main__":
    print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))