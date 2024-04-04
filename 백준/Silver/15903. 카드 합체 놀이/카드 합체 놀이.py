# 점수를 가장 작게 만들어야 하므로 x + y는 최소값으로 선정
# heappop으로 최소값 2번 빼내고 서로 더한값 heappush하기

from heapq import *
n,m = map(int, input().split())

nums = list(map(int, input().split()))
heapify(nums)

for _ in range(m):
    x = heappop(nums)
    y = heappop(nums)
    heappush(nums, (x+y))
    heappush(nums, (x+y))
    
print(sum(nums))