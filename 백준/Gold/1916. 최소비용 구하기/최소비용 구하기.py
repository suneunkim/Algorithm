# 우선순위 큐에 최소 비용을 0으로 한 출발 노드 삽입해서 while 시작.
# 출발 노드에서 갈 수 있는 도시와 비용을 탐색 -> heap에 다시 삽입

import sys
from heapq import *
input = sys.stdin.readline

N = int(input()) # 도시
M = int(input()) # 버스
graph = [[] for _ in range(N+1)] # 도시(인덱스)에서 도착지와 비용

# 버스 노선 입력 받고 graph에 담기
for _ in range(M):
    a, b, cost = map(int, input().split())
    graph[a].append([b, cost])
start, end = map(int, input().split()) # 목표 출발지와 도착지. 입력받기 끝

# 나머지 초기값 설정과 heap에서 쓸 처음 조건 삽입
costs = [1e9 for _ in range(N+1)] # 인덱스=도시번호=그 도시까지의 누적비용
heap = []
costs[start] = 0 # 시작지점 비용 0
heappush(heap, [0, start])

while heap:
    current_cost, city = heappop(heap)
    if costs[city] < current_cost: # costs에 최소값을 담을것이라 크다면 스킵
        continue
    # graph에 시작 도시로 갈 수 있는 도시들 for문 탐색
    for next_city, next_cost in graph[city]:
        sum_cost = next_cost + current_cost
        if costs[next_city] <= sum_cost:
            continue # costs에 담긴게 최소값일테니 크거나 같다면 필요없음
        costs[next_city] = sum_cost 
        heappush(heap, [sum_cost, next_city])
        
print(costs[end]) # costs의 도착지 도시
    
#  graph. 1번 인덱스: 1번 도시에서 [2,2] 2번 도시로 2 비용.
#  [[2, 2], [3, 3], [4, 1], [5, 10]],
#  [[4, 2]], 
#  [[4, 1], [5, 1]],
#  [[5, 3]],