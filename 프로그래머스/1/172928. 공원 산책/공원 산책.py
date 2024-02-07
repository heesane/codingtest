def solution(park, routes):
    max_width = len(park[0])
    max_height = len(park)
    pos = None  # 초기화

    for i in range(max_height):
        for j in range(max_width):
            if park[i][j] == "S":
                pos = [i, j]
                break
        if pos is not None:  # 찾았으면 종료
            break

    for route in routes:
        op, n = route.split()
        n = int(n)
        if op == "E":
            if pos[1] + n < max_width:
                for s in range(pos[1] + 1, min(pos[1] + n + 1, max_width)):
                    if park[pos[0]][s] == "X":
                        break
                else:
                    pos[1] += n
        elif op == "W":
            if pos[1] - n >= 0:
                for s in range(max(0, pos[1] - n), pos[1])[::-1]:
                    if park[pos[0]][s] == "X":
                        break
                else:
                    pos[1] -= n
        elif op == "N":
            if pos[0] - n >= 0:
                for s in range(max(0, pos[0] - n), pos[0])[::-1]:
                    if park[s][pos[1]] == "X":
                        break
                else:
                    pos[0] -= n
        elif op == "S":
            if pos[0] + n < max_height:
                for s in range(pos[0] + 1, min(pos[0] + n + 1, max_height)):
                    if park[s][pos[1]] == "X":
                        break
                else:
                    pos[0] += n
    return pos