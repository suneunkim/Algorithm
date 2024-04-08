import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# 입력 받기
N, M, R = map(int, input().split()) # 정점의 수 N, 간선의 수 M, 시작 정점
graph = [[] for _ in range(N+1)]  # 1번 인덱스부터 사용
visited = [0] * (N+1)  # 각 정점의 방문 여부
cnt = 1

# 간선 정보 2차원 리스트로 표현
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)  # a는 a번째 인덱스에 넣음. a -> b로 갈 수 있다
    graph[b].append(a)  # 양방향

for i in range(N + 1):
    graph[i].sort()
    
def bfs(start):
    global cnt
    queue = deque([start])
    visited[start] = cnt  # 방문 순서 나타내기용

    while queue:
        v = queue.popleft() 
        for i in graph[v]:  # 현재 노드와 연결된 각 노드에 대해 반복
            if not visited[i]:  # 방문하지 않은 노드인 경우 큐에 추가함
                cnt += 1  # 방문 순서를 증가시킴
                visited[i] = cnt
                queue.append(i)
                
bfs(R)

for i in range(1, N+1):
    print(visited[i])