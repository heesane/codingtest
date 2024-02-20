# 백준 17087 숨바꼭질 6

N, S = map(int,input().split()) # N = 동생 수, S = 수빈이 위치

bro = list(map(int,input().split()))

for i in range(N):
    bro[i] = abs(bro[i]-S)
    
def gcd(a,b):
    while b!=0:
        a, b = b, a%b
    return a

result = bro[0]
for i in range(1,N):
    result = gcd(result, bro[i])
print(result)