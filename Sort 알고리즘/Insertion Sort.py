

'''
    시간 복잡도 : O(N^2)
'''
if __name__ == '__main__' :
    item = [9,8,7,6,5,4,3,2,1]

    for i in range(1, len(item)):
        tmp = item[i]
        prev = i-1
        while prev >= 0 and item[prev] > tmp:
            item[prev+1] = item[prev]
            prev -= 1
        item[prev+1] = tmp

    print(item)

