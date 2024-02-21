# 백준 11729 하노이 탑 이동 순서

N = int(input())
answer = []
def hanoi(x,start,end):
    if x == 1:
        print(start,end)
        return
    
    hanoi(x-1,start,6-start-end)
    print(start,end)
    hanoi(x-1,6-start-end,end)

try_count = 2 ** N - 1
print(2**N-1)
hanoi(N,1,3)