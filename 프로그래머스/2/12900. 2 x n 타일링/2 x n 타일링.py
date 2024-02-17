from collections import deque
def pibo(n):
    prev,now = 1,2
    for _ in range(n-2):
        prev,now = now,now+prev
    return now

def solution(n):
    answer = 0
    DIVIDED_NUMBER = 1000000007
    return pibo(n) % DIVIDED_NUMBER