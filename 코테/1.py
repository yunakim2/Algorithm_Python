'''
정렬 은 우선 빈도,
같으면 크기 순
'''
from collections import defaultdict
from collections import deque
def sorting(arr):
    tmp_arr = []
    for i in range(len(arr)):

        size = arr[i][1]

        for j in range(i+1,len(arr)):
            if size != arr[j][1]:
                break
            else:

        else:
            for i in range(len(arr)):
                for j in range(i, len(arr)):
                    if arr[i] > arr[j]:
                        arr[i], arr[j] = arr[j], arr[i]



    return arr

def coutingSort(arr):
    count_arr = defaultdict()
    for item in arr:
        if item not in count_arr.keys():
            count_arr[item] = 1
        else:
            count_arr[item] += 1

    count_arr = sorting(count_arr)
    # count_arr = list(sorted(count_arr.items(), key=lambda x : -x[1]))
    res = []
    for idx in count_arr:
        for _ in range(int(idx[1])):
            res.append(idx[0])
    return res

if __name__ == '__main__':
    arr = [1,3,3,5,5,6,7,8]
    print(coutingSort(arr))