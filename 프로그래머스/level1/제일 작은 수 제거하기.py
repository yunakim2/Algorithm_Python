def solution(arr):

    mins = min(arr)
    arr.remove(mins)

    if len(arr)==0:
        return [-1]
    else:
        return arr


print(solution([4,3,2,1]))
