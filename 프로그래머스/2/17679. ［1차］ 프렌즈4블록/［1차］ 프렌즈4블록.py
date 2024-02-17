def solution(m, n, board):
    answer = 0
    board = list(map(list,zip(*board)))

    while True:
        pop_set = set()
        for i in range(1,n):
            for j in range(1,m):
                if board[i][j] == board[i-1][j] == board[i][j-1] == board[i-1][j-1]!='_':
                    pop_set |= set([(i,j),(i-1,j),(i,j-1),(i-1,j-1)])
        if not pop_set:
            break
        
        for i,j in pop_set:
            board[i][j] = 0
        
        for idx,val in enumerate(board):
            
            empty = ["_"] * val.count(0)
            board[idx] = empty + [block for block in val if block != 0]
        answer += len(pop_set)
    return answer