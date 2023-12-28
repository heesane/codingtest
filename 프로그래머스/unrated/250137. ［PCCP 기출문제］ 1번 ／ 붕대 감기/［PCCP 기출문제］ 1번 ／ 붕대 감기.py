from collections import deque
def solution(bandage, health, attacks):
    answer = 0
    turn = 0
    now_attacks = []
    healing_time = 0
    max_health = health
    max_healing_time,heal,plus_heal = bandage[0],bandage[1],bandage[2]
    
    dq = deque()
    for attack in attacks:
        dq.append(attack)
    
    for i in range(1,max(attacks)[0]+1):
        attack_time, attack_damage = 0,0
        turn += 1
        
        if i == dq[0][0]:
            now_attacks = dq.popleft()

            attack_time,attack_damage = now_attacks[0],now_attacks[1]

        if turn == attack_time:
            health -= attack_damage
            healing_time = 0
            if health <= 0:
                return -1
        else:
            health += heal
            healing_time += 1
        
        if healing_time == max_healing_time:
            health += plus_heal
            healing_time = 0
            
        if health >= max_health:
            health = max_health
        
    return health