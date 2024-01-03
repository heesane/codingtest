# 4948 베르트랑 공준

def get_prime(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(x**0.5)+1):
            if x % i == 0:
                return False
        return True

answer = []
while True:
    
    n = int(input())
    if n == 0:
        break
    
    count = 0
    for i in range(n+1, 2*n+1):
        if get_prime(i):
            count += 1
    answer.append(count)

for _ in range(len(answer)):
    print(answer[_])