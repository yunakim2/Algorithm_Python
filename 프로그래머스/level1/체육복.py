# 그리디 알고리즘

def solution(n, lost, reserve):
    cnt =0
    mem = []
    for i in lost :
        if i in reserve :
            reserve.remove(i)
        else :
            mem.append(i)

    for i in range(1,n+1) :
        if i not in mem :
            cnt+=1
    print(mem)
    for j in mem:
        flag = False
        if 1<j<n :
            if j-1 in reserve :
                reserve.remove(j-1)
                flag = True
                cnt += 1
            if j+1 in reserve and flag == False :
                reserve.remove(j+1)
                cnt += 1


        else :
            if j==1 :
                if j + 1 in reserve :
                    reserve.remove(j + 1)
                    cnt += 1
            else :
                if j - 1 in reserve:
                    reserve.remove(j - 1)
                    cnt += 1


    return cnt


print(solution(7, [2,3,4], [1,2,3,6]))
