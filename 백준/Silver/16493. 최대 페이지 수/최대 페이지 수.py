# 백준 16439 최대 페이지 수

N,M = map(int,input().split()) # N = 남은 일, M = 챕터 수

books = [list(map(int,input().split()))for _ in range(M)]

dp = [[0] * (N+1) for _ in range(M+1)]

for i in range(1,M+1): # 1~N
    for j in range(1,N+1): # 0~M-1
        # print(dp)
        if j - books[i-1][0] >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-books[i-1][0]]+books[i-1][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[M][N])