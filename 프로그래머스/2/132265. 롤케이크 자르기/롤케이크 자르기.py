from collections import Counter
def solution(topping):
    answer = 0
    length = len(topping)
    
    front = Counter()
    back = Counter(topping)
    
    for t in range(length - 1):
        
        front[topping[t]] += 1
        back[topping[t]] -= 1
        
        if back[topping[t]] == 0:
            del back[topping[t]]
        
        if len(front) == len(back):
            answer += 1

    return answer