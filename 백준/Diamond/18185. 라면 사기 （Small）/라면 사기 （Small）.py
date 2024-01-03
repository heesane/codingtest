## 18185 라면 사기 (Small)
## 15:20

N = int(input()) # 4
A = list(map(int, input().split())) # 1 1 0 1
A.append(0)
A.append(0)
price =  0
for i in range(N): 
    while A[i] != 0:
        if A[i+1] != 0 and A[i+2] != 0:
            if A[i+1] > A[i+2]:
                A[i] -= 1
                A[i+1] -= 1
                price += 5
            else:
                A[i] -= 1
                A[i+1] -= 1
                A[i+2] -= 1
                price += 7
        elif A[i+1] != 0 and A[i+2] == 0:
            A[i] -= 1
            A[i+1] -= 1
            price += 5
        elif (A[i+1] == 0 and A[i+2] == 0):
            A[i] -= 1
            price += 3
        elif (A[i+1] == 0 and A[i+2] != 0):
            A[i] -= 1
            price += 3
print(price)
            