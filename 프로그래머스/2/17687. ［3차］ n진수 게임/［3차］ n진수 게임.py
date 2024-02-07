def convert(n,num):
    # num을 n진수로 변환하는 함수
    ret = ''
    if num == 0:
        return '0'
    while num > 0:
        num, mod = divmod(num,n)
        if mod >= 10:
            ret += chr(65 + mod - 10)
        else:
            ret += str(mod)
    return ret[::-1]
def solution(n, t, m, p):
    answer = ''
    result = ''
    num = 0
    
    while len(result) < t * m:
        result += convert(n, num)
        num += 1
    for i in range(t):
        answer += result[i*m+p-1]
    return answer