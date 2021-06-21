

'''
    시간 복잡도 : O(N^2)
'''
if __name__ == '__main__' :
    item = [9,8,7,6,5,4,3,2,1]

    for i in range(len(item)):
        for j in range(i+1, len(item)):
            if item[j] < item[i]:
                tmp = item[i]
                item[i] = item[j]
                item[j] = tmp

    print(item)

