from collections import deque
def solution(x, y, n):
    if x == y:
        return 0
    
    queue = deque([(x, 0)])  
    visited = set()   
    
    while queue:
        current, count = queue.popleft()
        
        if current == y:
            return count
        
        
        if current + n <= y and current + n not in visited:
            queue.append((current + n, count + 1))
            visited.add(current + n)
        
        
        if current * 2 <= y and current * 2 not in visited:
            queue.append((current * 2, count + 1))
            visited.add(current * 2)
        
        
        if current * 3 <= y and current * 3 not in visited:
            queue.append((current * 3, count + 1))
            visited.add(current * 3)
    return -1