def solution(words, queries):
    answer = []
    for i in queries :
        check = 0
        res = ""
        cnt =0
        length = len(i)
        if(i[0] == "?") :
            i =i[::-1]
            res = i.split("?")[0][::-1]
            for j in words:
                if len(res) == 0 and len(j) == length :
                    cnt+=1
                elif j.endswith(res) and len(j) == length :
                    cnt+=1

        else :
            res = i.split("?")[0]
            for j in words :
                if len(res) == 0 and len(j) == length :
                    cnt+=1
                elif j.startswith(res) and len(j) == length :
                    cnt+=1

        answer.append(cnt)

    return answer



words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words,queries))