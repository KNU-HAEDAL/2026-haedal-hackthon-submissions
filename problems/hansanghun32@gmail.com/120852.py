def solution(n):
    answer = []
    divisor = 2
    while n > 1:
        if n % divisor ==0:
            answer.append(divisor)
            while n%divisor == 0:
                    n //= divisor
        divisor += 1
    return answer