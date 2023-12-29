def solution(n):
    x,y = 0,0
    direction = "R"
    answer = [[0 for _ in range(n)] for _ in range(n)]
    
    for num in range(1,n**2+1):
        answer[x][y] = num
        if direction == "R":
            if y == n - 1 or answer[x][y+1] != 0:
                direction = "D"
                x += 1
            else:
                y = y + 1
        
        elif direction == "D":
            if x == n - 1 or answer[x+1][y] != 0:
                direction ="L"
                y -= 1
            else:
                x += 1
                
        elif direction == "L":
            if y == 0 or answer[x][y-1] != 0:
                direction = "U"
                x -= 1
            else:
                y -= 1
                
        elif direction =="U":
            if x == 0 or answer[x-1][y] != 0:
                direction = "R"
                y += 1
            else:
                x -= 1
        
    return answer