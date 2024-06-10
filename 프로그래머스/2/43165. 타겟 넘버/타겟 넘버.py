def solution(numbers, target):
    answer = 0
    n = len(numbers)
    def dfs(idx, total):
        # 종료 조건
        if idx == n:
            if total == target:
                nonlocal answer
                answer += 1
            return
        dfs(idx + 1, total + numbers[idx])
        dfs(idx + 1, total - numbers[idx])
    
    dfs(0, 0)
    return answer