# 백준 9461 파도반 수열

N = int(input())
ret = []
for _ in range(N):
    target = int(input())
    answer = [1,1,1]
    
    if target <= 3:
        ret.append(answer[target-1])
    
    else:
        for i in range(3,target):
            answer.append(answer[i-2] + answer[i-3])
        ret.append(answer[-1])

for r in ret:
    print(r)