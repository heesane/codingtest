# 백준 1016 제곱 ㄴㄴ 수
min,max = map(int,input().split())

answer = max - min + 1

visited = [False] * (answer)

for i in range(2,int(max**0.5) +1):
    square = i ** 2
    for j in range((((min-1)//square)+1)*square,max+1,square):
        if not visited[j-min]:
            visited[j-min] = True
            answer -= 1

print(answer)