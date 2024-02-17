def solution(dirs):
    answer = 0
    x,y = 0,0
    visited = set()
    
    for step in dirs:
        prev_x,prev_y = x,y
        print(x,y)
        if step == "L":
            x -= 1
        elif step == "R":
            x+=1 
        elif step == "U":
            y+=1
        elif step == "D":
            y-=1
                
        if -5 <= x <= 5 and -5 <= y <= 5:
            visited.add((prev_x,prev_y,x,y))
            visited.add((x,y,prev_x,prev_y))
        else:
            x,y = prev_x,prev_y
    return len(visited) / 2