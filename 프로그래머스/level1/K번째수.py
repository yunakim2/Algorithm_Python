def solution(array, commands):
    answer = []
    for t in range(len(commands)) :
        temp = array[commands[t][0]-1:commands[t][1]]
        temp.sort()
        answer.append(temp[commands[t][2]-1])

    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))