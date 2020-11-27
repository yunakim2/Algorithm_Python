n = int(input())

dp = [0] * n

for i in range(n) :
    dp[i] = list(map(int,input().split()))


print(dp)

for i in range(1,n) :
    if i == 1:
        dp[i][0] = dp[i][0]+dp[0][0]
        dp[i][1] = dp [i][1]+dp[0][0]
    else :
        for j in range(len(dp[i])) :

            if j == 0 :
                dp[i][j] = dp[i-1][j]+ dp[i][j]
            elif j == len(dp[i])-1 :
                dp[i][j] = dp[i][j]+ dp[i-1][j-1]
            else :
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + dp[i][j]



print(dp)
print(max(dp[n-1]))