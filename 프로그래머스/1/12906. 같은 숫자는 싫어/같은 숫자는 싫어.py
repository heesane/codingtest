from collections import deque
def solution(arr):
    answer = []
    dq = deque()
    dq.append(arr[0])
    answer.append(arr[0])
    for i in arr:
        left = dq.popleft()
        if left == i:
            dq.append(i)
        else:
            dq.append(i)
            answer.append(i)
            
        
    return answer