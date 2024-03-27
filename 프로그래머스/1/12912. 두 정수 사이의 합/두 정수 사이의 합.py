def solution(a, b):
    
    # a와 b가 같으면 아무 수나 리턴
    if a == b:
        return a

    # a와 b 중 큰 값 찾기
    min_value = min(a,b)
    max_value = max(a,b)
    
    # a와 b 사이의 범위값 구하기
    result = range(min_value, max_value+1)
    
    return sum(result)