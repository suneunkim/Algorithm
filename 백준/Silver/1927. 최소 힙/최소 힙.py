# heap 자료구조
# heap[0] -> 최솟값
# heappop(heap) -> 최솟값 추출(제거됨)
# heappush(3) -> 힙에 3을 추가

from sys import stdin
from heapq import *

input = stdin.readline

n = int(input())
heap = []

for _ in range(n):
    a = int(input())
    if a: # a가 0이 아니라면
        heappush(heap, a)
    else:
        if heap: # 빈 배열이 아니라면
            print(heappop(heap))
        else:
            print(0)

# 0이면 최솟값 출력, 제거. 빈배열이면 0을 출력