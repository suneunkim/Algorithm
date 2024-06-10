# 노드의 개수와 쿼리의 개수
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 노드 간 비용 그래프 생성
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c]) # a노드 -> b노드의 가중치 c
    graph[b].append([a, c]) # 양방향
    
def dfs(start, end, dist):
    global count
     # a 노드에서 b노드까지 비용구하기. return 시 쿼리 수행에서 count가 print.
    if start == end:
        count = dist
        return
    
    for node, value in graph[start]:
        if not visited[node]:
            visited[node] = True
            dfs(node, end, dist + value)
            
# 쿼리 수행
for _ in range(m):
    a, b = map(int, input().split())
    visited = [False] * (n + 1)
    count = 0
    visited[a] = True
    dfs(a, b, 0)
    print(count)
        