

def dfs(idx, total, minus,plus,mul,div):
    global max_val, min_val
    if idx == N:
        max_val = max(max_val,total)
        min_val = min(min_val, total)
        return

    if minus > 0:
        dfs(idx+1, total-number[idx], minus-1, plus,mul,div)
    if plus >0:
        dfs(idx+1, total+number[idx], minus, plus-1, mul, div)
    if mul > 0:
        dfs(idx+1, total*number[idx], minus, plus, mul-1, div)
    if div >0 :
        if total >= 0:
            dfs(idx+1, total//number[idx], minus,plus,mul,div-1)
        else:
            dfs(idx+1, -(-total // number[idx]), minus,plus, mul, div-1)



if __name__ == '__main__':
    T = int(input())
    # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
    for test_case in range(1, T + 1):
        N = int(input())
        plus,minus,mul, div = map(int,input().split())
        number = list(map(int,input().split()))
        max_val = float('-inf')
        min_val = float('inf')
        dfs(1, number[0], minus, plus, mul, div)
        print('#{} {}'.format(test_case, max_val-min_val))

