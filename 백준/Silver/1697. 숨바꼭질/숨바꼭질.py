# 한칸 앞, 뒤로 이동하거나 현재 위치에서 2배로 이동
# 수빈이의 위치에서 BFS 시작하고 수빈위치>동생위치 -> 순간이동

from collections import deque

N, K = map(int, input().split())

def bfs(N, K):
    queue = deque([(N, 0)]) #시작 위치와 시간(초)
    visited = [False] * 100101 # N,K 범위 100000
    visited[N] = True # 시작점 방문체크

    while queue:
        c, time = queue.popleft() #덱에 있던 값
        if c == K: # 동생의 위치 도착
            return time
        # 수빈이 움직일 수 있는 세 가지 경우
        for next_c in (c - 1, c + 1, c * 2):
            if 0 <= next_c <= 100000 and not visited[next_c]:
                # 범위 안이고, 방문한 적 없는 위치치
                visited[next_c] = True
                # 위치와 함께 1초 증가시키기키
                queue.append((next_c, time + 1))
                
print(bfs(N,K))

# 입력값을 받아서 bfs 함수를 만들고, 기본값으로 사용
# bfs 함수는 deque를 만들어서 기본값을 넣기
# visited에 기본값(시작점) 넣어서 방문 체크하기
# while로 queue가 있다면? 조건으로 반복문.
# 위에서 deque에 넣은 값을 popleft로 꺼내서 사용
# 문제의 조건에 따라 위치를 탐색하는 코드를 추가(범위도설정)
# 가능한 방향에 따라 처음 시작점을 변경시키기
# 변경한 위치를 다시 queue에 추가하고 while 반복하기