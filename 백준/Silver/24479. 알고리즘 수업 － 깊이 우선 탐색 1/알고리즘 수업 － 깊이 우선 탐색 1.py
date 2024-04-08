import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, M, R = map(int, input().split()) # 정점의 수 N, 간선의 수 M, 시작 정점
graph = [[] for _ in range(N+1)]  # 1번 인덱스부터 사용
visited = [0] * (N+1)  # 각 정점의 방문 여부
cnt = 1  # 방문 순서를 나타내는 변수 초기화

# 간선 정보 2차원 리스트로 표현
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)  # a는 a번째 인덱스에 넣음. a -> b로 갈 수 있다
    graph[b].append(a)  # 양방향
    
def dfs(t):
    global cnt  # cnt 변수를 전역 변수로 사용하기 위해 선언
    visited[t] = cnt  # 현재 노드 t를 방문한 것으로 표시하고 방문 순서를 저장
    
    graph[t].sort()  # 현재 노드와 연결된 노드들을 오름차순으로 정렬
    for i in graph[t]:  # 현재 노드와 연결된 각 노드에 대해 반복
        if visited[i] == 0:  # 방문하지 않은 노드인 경우
            cnt += 1  # 방문 순서를 증가시킴
            dfs(i)  # 재귀적으로 해당 노드를 방문

dfs(R)

for i in range(1, N+1):
    print(visited[i])