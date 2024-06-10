n = int(input()) # 컴퓨터의 수
m = int(input()) # 연결되어있는 수
graph = [[] for _ in range(n + 1)]
# 0부터 컴퓨터 n개까지 리스트 초기화)

# 그래프에 연결되어있는 컴퓨터 번호 입력하기.
# 그래프[1번 컴퓨터] = [2번, 3번 컴퓨터]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 컴퓨터 개수만큼 방문 리스트 초기화
visited = [False] * (n + 1)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]: # 방문 안된 곳에서 재귀함수 호출
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)

print(visited.count(True) - 1) # 시작점 1번 컴퓨터 제외