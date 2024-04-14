def solution(n):
    answer = 0
    cnt = 1
    while True:
        if cnt ** 2> n:
            answer = -1
            break
        if n % cnt == 0 and n // cnt == cnt:
            answer = (cnt+1)**2
            break
        else:
            cnt += 1
    return answer