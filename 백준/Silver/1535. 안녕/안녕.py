# 백준 1535 안녕

N = int(input())

minus = list(map(int,input().split()))
plus = list(map(int,input().split()))

dp = [[0] * 101 for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(100):
        if j - minus[i-1]>=0:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-minus[i-1]]+plus[i-1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][99])