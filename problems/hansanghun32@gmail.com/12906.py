def solution(arr):
    answer = []
    for i in arr: 
        if i not in answer or answer[-1] != i: 
            answer.append(i) # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다. 
            
    print('Hello Python') 
    return answer