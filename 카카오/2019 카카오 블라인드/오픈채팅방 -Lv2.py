def solution(record):
    answer = []
    ans = []
    uid_list = {}
    for str in record:
        st_l = list(str.split())
        moving, uid = st_l[0], st_l[1]
        if moving == 'Leave':
            tmp = "L " + uid
            answer.append(tmp)
        else:
            nickname = st_l[2]
            if moving == 'Enter':
                uid_list[uid] = nickname
                tmp = "E " + uid
                answer.append(tmp)
            elif moving == 'Change':
                uid_list[uid] = nickname


    for a in answer:
        mode, uid = a.split()
        if mode == 'E':
            ans.append(uid_list[uid] + '님이 들어왔습니다.')
        else:
            ans.append(uid_list[uid] + '님이 나갔습니다.')

    return ans


if __name__ == "__main__":
    print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))

