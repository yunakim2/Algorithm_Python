array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def partition(arr, left, right):
    pivot = arr[(left + right) // 2]
    print('pivot-',pivot)
    while left < right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while (array[left] < pivot) and (left < right):
            left += 1
        while array[right] > pivot and (left < right):
            right -=1
        if left < right:
            print('left, right',left,right)
            array[left], array[right] = array[right], array[left]

    return left


def quick_sort(arr, left, right):
    if left < right:
        print('lef', left)
        pivot_new = partition(arr, left, right)
        quick_sort(arr, left, pivot_new - 1)
        quick_sort(arr, pivot_new + 1, right)


quick_sort(array, 0, len(array) - 1)
print(array)
