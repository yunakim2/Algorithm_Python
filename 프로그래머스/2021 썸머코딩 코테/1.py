def solution(code, day, data):
    answer = {}
    for d in data:
        tmp_d = list(d.split())
        tmp_d[0] = tmp_d[0].replace('price=','')
        tmp_d[1] = tmp_d[1].replace('code=', '')
        tmp_d[2] = tmp_d[2].replace('time=','')
        if tmp_d[1] == code:
            if tmp_d[2][:8] == day:
                answer[tmp_d[2][8:]] = int(tmp_d[0])


    answer = sorted(answer.items(), key = lambda x: x[0])
    ans = []
    for x,y in answer:
        ans.append(y)
    return ans


if __name__ == "__main__":
    print(solution("012345","20190620",["price=80 code=987654 time=2019062113","price=90 code=012345 time=2019062014","price=120 code=987654 time=2019062010","price=110 code=012345 time=2019062009","price=95 code=012345 time=2019062111"]))