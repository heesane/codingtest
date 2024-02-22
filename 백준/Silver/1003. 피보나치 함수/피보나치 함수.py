# 백준 1003 피보나치 함수
for _ in range(int(input())):
    zeros,ones = 1,0
    for i in range(int(input())):
        zeros,ones = ones,zeros+ones
    print(zeros,ones)