from math import gcd  # 최대공약수를 구하는 gcd() import
'''
최소 공배수 구하는 공식 최소공배수 = (x*y) / gcd(x,y)
'''
def solution(arr):
    answer = arr[0]
    for num in arr:
        answer = answer * num // gcd(answer,num)

    return answer


if __name__ == "__main__":
    print(solution([2,6,8,14]))
    print(solution([1,2,3]))
    print(solution([3,4,9,16]))
