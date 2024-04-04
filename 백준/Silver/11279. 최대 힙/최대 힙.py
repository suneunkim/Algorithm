from sys import stdin
from heapq import *

input = stdin.readline

n = int(input())
heap = []

for _ in range(n):
    a = int(input())
    if a: # 0이 아니라면 추가하기
        heappush(heap,-a)
    else: # 0이면 가장 큰 값 출력하기
        if heap: # 빈 배열인지 확인
            print(-heappop(heap))
        else:
            print(0)