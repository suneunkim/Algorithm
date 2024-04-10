import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
min_value = sys.maxsize # 최대값 설정 -> 최소값으로 업데이트
visited = [0] * n

def dfs(depth, start, cost):
    global min_value
    
    # 모든 도시를 방문했고 출발 도시로 돌아갈 수 있다
    if depth == n - 1 and arr[start][0] != 0:
        min_value = min(min_value, cost + arr[start][0])
        return
    
    # 모든 도시 탐색
    for i in range(n):
        if not visited[i] and arr[start][i] != 0: #(0,0) 제외 (0,1)부터.
            visited[i] = 1 # 방문 처리
            dfs(depth + 1, i, cost + arr[start][i])
            visited[i] = 0

            # 시작 도시 방문
visited[0] = 1
dfs(0,0,0)
print(min_value)
    
# sys.maxsize (정수) && float('inf') (부동소수점)
# m = 1e9로도 최대값 설정가능 (10억)
# 최소값을 찾는 문제에서 초기화값으로 사용(최대값임)
# min() 함수를 사용하여 더 작은 값을 찾고 최소값을 업데이트