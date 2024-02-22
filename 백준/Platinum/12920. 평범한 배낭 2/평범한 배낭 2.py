# 백준 12920 평범한 배낭 2

N, M = map(int,input().split()) # N = 물건 종류 수, M = 가방의 최대 무게
L = []
for i in range(N):
    V,C,K = map(int,input().split())
    check =0; sum =0
    while True:
        sum += 2**check
        if sum <= K:
            L.append([V*(2**check),C*(2**check)])
            check += 1
        else:
            if K - (sum - 2**check)!=0:
                L.append([V*(K-(sum-2**check)), C*(K-(sum-2**check))])
            break

dp = [[0]*(M+1) for _ in range(len(L)+1)]

for i in range(1,len(L)+1):
    weight = L[i-1][0]; value = L[i-1][1]
    for j in range(1,M+1):
        if j - weight >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[len(L)][M])