# 리스트에 넣고 정렬하기는 시간초과 -> 우선순위 큐 사용
# 다음 행 가면서 최소값 계속 비교하면서 지우고 새 숫자 투입
# N번째로 큰 수 -> heap에 N개 있다면 최소값은 N번째 큰 수

from sys import stdin
from heapq import *

input = stdin.readline

n = int(input())
heap = []

nums = list(map(int, input().split()))

# 첫 번째 행 heap에 입력
for num in nums:
    heappush(heap, num)
    
for _ in range(n-1):
    row = list(map(int, input().split()))
    for r in row:
        if r > heap[0]: # heap의 최소값을 보다 큰 값으로 계속 교체하기
            heappush(heap, r)
            heappop(heap)

# N개가 담긴 리스트에서, N번째 숫자는 최소값임
print(heap[0])