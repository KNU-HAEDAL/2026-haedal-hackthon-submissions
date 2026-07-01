def solution(n):
    answer = 0
    
    a = 0
    b = 1
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    for i in range(2, n+1):
        answer = (a + b) % 1234567
        a = b
        b = answer
    return answer