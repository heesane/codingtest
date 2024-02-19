# 백준 11053 가장 긴 증가하는 부분 수열

N = int(input())

num_list = list(map(int,input().split()))
real = [num_list[0]] 

for n in range(1,N):
    if real[-1] < num_list[n]:
        real.append(num_list[n])
    else:
        for i in range(len(real)):
            if real[i] >= num_list[n]:
                real[i] = num_list[n]
                break
print(len(real))
