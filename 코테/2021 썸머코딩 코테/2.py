from collections import deque

def solution(t, r):
    answer = []
    member = deque([ [] for _ in range(len(t))])

    for i in range(len(t)):
        member[i].append(i)
    for idx, m_t in enumerate(t):
        member[idx].append(m_t)
    for idx, m_r in enumerate(r):
        member[idx].append(m_r)

    member = deque(sorted(member, key=lambda x: (x[1],x[2],x[0])))
    res = 0
    # print(member)
    queue = deque([])
    while member or queue:
        # print('mem', member)
        # print('qu - ',queue)
        if queue and member:
            if queue[0][1] == member[0][1]:
                if queue[0][2] < member[0][2]:
                    mem = queue.popleft()
                elif queue[0][2] > member[0][2]:
                    mem = member.popleft()
                else:
                    if queue[0][0] > member[0][0]:
                        mem = member.popleft()
                    else:
                        mem = queue.popleft()
            else:
                mem = queue.popleft()
        elif member:
            mem = member.popleft()
        else:
            mem = queue.popleft()

        while member and mem[1] == member[0][1]:
            queue.append(member.popleft())

        answer.append(mem[0])

        for i,_ in enumerate(queue):
            queue[i][1] += 1

    return answer


if __name__ == "__main__":
    # print(solution([0,1,3,0],[0,1,2,3]))
    print(solution([7,6,8,1],[0,1,2,3]))
    print(solution([0,0,0,0],[0,1,2,3]))
    print(solution([0,1,1,1],[0,1,0,0]))