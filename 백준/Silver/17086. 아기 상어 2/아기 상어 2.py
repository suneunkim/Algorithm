# 상어가 없으면 0, 있으면 1. deque로 상어위치부터 검색을 시작.
# 범위 내에서, 8개의 방향을 탐색. 탐색한 곳의 값을 +1, 다시 deque에 넣고 탐색

from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)] # N개 행만큼

#[1] 8가지 이동방향 설정하기.
d = [(1,0),(-1,0),(0,-1),(0,1),(-1,-1),(1,1),(-1,1),(1,-1)]
q = deque()

#[2] 처음에 사용할 상어 위치
for x in range(N):
    for y in range(M):
        if graph[x][y]: # 값이 있으면 상어
            q.append((x,y))

#[3] 상어 위치를 q로 꺼내서 쓰고 8방향 탐색. 상어가 없는 새 위치를 다시 q로.
def bfs():
    while q: #새로운 지점을 큐에 담을거라 사용시 popleft()
        x, y = q.popleft()
        for dx, dy in d:
            # 현재 위치에서 각 이동할 방향들 더함
            nx, ny = x + dx, y + dy
            # 범위 내부인지 확인
            if 0 <= nx < N and 0 <= ny < M:
                # 상어가 없는 곳인지
                if not graph[nx][ny]: # if not -> 0(False) 이라면
                    graph[nx][ny] = graph[x][y] + 1
                    # nx,ny에서 다시 8방향으로 탐색해야함
                    q.append((nx,ny))
                
bfs()
ans = map(max, graph)
print(max(ans) -1)