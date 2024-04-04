from heapq import *
from sys import stdin
input = stdin.readline

n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    if num: # 0이 아니면
        heappush(heap, (abs(num), num))
    # 0이라 출력
    else: 
        if heap:
            print(heappop(heap)[1])

        else: # 빈 배열이라면
            print(0)