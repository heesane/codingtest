from collections import deque

def solution(order):
    answer = []
    init_box = deque([i+1 for i in range(len(order))]) # 1~10
    sub_box = []
    cnt = 0
    while True:
        if init_box and init_box[0] == order[cnt]:
            answer.append(init_box.popleft())
            cnt += 1
        elif sub_box and sub_box[-1] == order[cnt]:
            answer.append(sub_box.pop())
            cnt += 1
        else:
            if init_box:
                sub_box.append(init_box.popleft())
            else:
                break
    
    return len(answer)