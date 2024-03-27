def solution(sizes):
    maxWidth = 0
    minHeight = 0
    
    for a, b in sizes:
        if a < b:
            a, b = b, a # 2차원 배열 큰 값이 앞으로 스왑
            
        maxWidth = max(maxWidth, a) # 최대 중에서 최대
        minHeight = max(minHeight, b) # 최소 중에서 최대
    
    return maxWidth * minHeight

# 최소 직사각형 만들기
# 가로 길이가 최대, 세로 길이가 최소인 사각형
        