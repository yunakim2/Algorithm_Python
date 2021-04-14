
def backtracking(cnt,sum_value, plus, minus, mul, div):
    global min_value, max_value
    if cnt == n:
        min_value = min(min_value,sum_value)
        max_value = max(max_value, sum_value)
        return
    if plus > 0:
        backtracking(cnt+1, sum_value+value[cnt], plus-1, minus, mul, div)
    if minus > 0:
        backtracking(cnt+1, sum_value-value[cnt], plus,minus-1, mul, div)
    if mul > 0:
        backtracking(cnt+1, sum_value*value[cnt], plus,minus, mul-1, div)
    if div > 0:
        if sum_value >= 0:
            backtracking(cnt+1, sum_value//value[cnt], plus,minus, mul, div-1)
        else:
            backtracking(cnt+1, -(-sum_value//value[cnt]),plus,minus,mul, div-1)





if __name__ == '__main__':
    n = int(input())
    value = list(map(int,input().split()))
    plus, minus, multi, div = map(int, input().split())
    max_value = float('-inf')
    min_value = float('inf')
    backtracking(1,value[0], plus, minus,multi, div)
    print(max_value)
    print(min_value)
