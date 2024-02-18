def solution(n):
    answer = 0
    DIVIDED_NUMBER = 1000000007
    ans = (3,11)
    new_ans = (0,0)
    n /= 2
    n -= 2
    while n>0:
        ans =(ans[1],4*ans[1]-ans[0])
        n -= 1
    
    return ans[1] % 1000000007