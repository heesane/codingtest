# 백준 11047 동전 0

N, K = map(int,input().split())

coins = [int(input()) for _ in range(N) ]
coins.sort(reverse=True)
cnt = 0
while K !=0:
    for coin in coins:
        if coin <= K:
            cnt += K // coin
            K = K % coin
            
print(cnt)