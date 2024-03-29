N, M = map(int, input().split())
result = []

def backtrack():
    # 출력 조건
    if len(result) == M:
        print(' '.join(map(str, result)))
        
    for i in range(1, N + 1):
        if i not in result: 
            result.append(i)
            backtrack()
            result.pop()
            
backtrack()

# [1] -> [1,2] -> 출력 -> 2 빼고 [1] -> [1,3] -> 출력