'''
평균 시간 복잡도 O(NlogN)
'''

if __name__ == '__main__':
    item  = [9,8,7,6,5,4,3,2,1]
    for i in range(len(item)):
        print('i-- ',i)
        minIdx = i
        for j in range(i+1, len(item)):
            if item[j] < item[minIdx] :
                minIdx = j
        tmp = item[minIdx]
        item[minIdx] = item[i]
        item[i] = tmp
        print(item)


    print(item)