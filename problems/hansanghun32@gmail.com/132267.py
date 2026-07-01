def solution(a, b, n):
    answer = 0
    while n>=a:
        exchanged = (n//a)*b
        remain = n%a
        
        answer += exchanged
        n = exchanged + remain
        
    return answer