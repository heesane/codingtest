## 1300 : K번째 수
### 정렬
# N*N 행렬에서 X보다 작은 수의 개수를 찾는 문제
# N이 최대 10^5이므로, O(N^2)으로는 시간초과가 난다.
# 이분탐색을 이용하여 O(N*logN)으로 풀어야 한다.
# 이분탐색을 위해 start와 end를 설정한다.

import sys
input = sys.stdin.readline

N = int(input())
X = int(input())

start = 1
end = N*N

while start <= end:
    mid = (start+end)//2
    cnt = 0
    for i in range(1, N+1):
        cnt += min(mid//i, N)
    if cnt >= X:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1
    
print(answer)

