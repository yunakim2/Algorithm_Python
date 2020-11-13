def solution(arr):
    answer = []
    i=0
    while i<len(arr) :
        print(f"i == {i}")
        if i<len(arr)-1 :
            for j in range(i+1, len(arr)) :
                print(f"i == {i},{arr[i]}")
                print(f"j == {j},{arr[j]}")
                if arr[i] == arr[j] :
                    if j==len(arr)-1 :
                        answer.append(arr[i])
                        i = j
                        break
                    else :  continue
                else :
                    answer.append(arr[i])
                    i = j
                    print(f"change == i {i}")
                    print(f"answer == {answer}")
                    break
        else :
            if arr[i] != arr[i-1] :
                answer.append(arr[i])
                break
            else : break

    return answer

print(solution([1,2,3,4,5,6,7,8]))