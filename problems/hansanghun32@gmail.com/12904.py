def solution(s):
    n = len(s)
    
    if n == 1:
         return 1
    
    answer = 1
    
    for center in range(n):
        left = center
        right = center
        
        while left >= 0 and right < n and s[left] == s[right]:
            answer = max(answer, right - left + 1)
            left -= 1
            right += 1
            
        left = center
        right = center + 1
        
        while left >= 0 and right < n and s[left] == s[right]:
            answer = max(answer, right - left + 1)
            left -= 1
            right += 1
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer