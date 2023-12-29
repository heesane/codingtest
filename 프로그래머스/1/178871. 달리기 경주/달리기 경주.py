def solution(players, callings):
    rank = {val:idx for idx,val in enumerate(players)}
    
    for call in callings:
        index = rank[call]
        rank[call] -= 1
        rank[players[index-1]] += 1
        players[index-1],players[index] = call,players[index - 1]
    return players