

n = int(input())
arr = []
dp = [0] *n
for i in range(n) :
    arr.append(int(input()))
if n != 1 and n!=2 :
    dp [0] = arr[0]
    dp [1] = max(arr[0]+arr[1], arr[1])
    dp [2] = max(arr[0]+arr[2], arr[1]+arr[2])

    for i in range(3,n) :
        dp[i] = max(dp[i-2]+arr[i] , dp[i-3]+arr[i-1]+arr[i])
else :
    if n == 1 :
        dp[n-1]= arr[n-1]
    else :
        dp[n-1] = max(arr[0] + arr[1], arr[1])

print(dp[n-1])