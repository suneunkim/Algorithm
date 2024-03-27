def solution(food):
    
    answer = ''
    
    for num in range(1,len(food)):
        answer += str(num) * (food[num] // 2)
    return answer + str(0) + answer[::-1]
    
    # [1,3,4,6]
    # 인덱스 기준 0번째는 물이라 제외.
    # 첫번째 음식 3 // 2 는 1. 1개씩
    # 두번째 음식 4개니까 2개씩
    # 세번째 음식 6개니까 3개씩.
    # 그래서 122333
    