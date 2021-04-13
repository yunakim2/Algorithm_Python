def solution(arr):
    m_item = []
    if arr[0] == 1:
        m_item.append(arr[1])
    else:
        m_item.append(arr[2])

    answer = 1 * m_item
    for idx in arr:
        for min_idx in m_item:
            if idx == min_idx:
                continue
          
    return answer


if __name__ == "__main__":
    print(solution([2,6,8,14]))
    print(solution([1,2,3]))
    print(solution([3,4,9,16]))
