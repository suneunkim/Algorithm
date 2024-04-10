# combinations로 1부터 n개 만큼 nums의 조합을 만들기
# 모든 조합을 한번씩 sum()한 값이 s와 같으면 count을 1씩 증가시키기

import sys
from itertools import combinations

input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))
count = 0

for i in range(1, n+1):
    # nums의 숫자들을 i개의 원소로 조합 만들기.
    comb = combinations(nums, i)
    
    # 조합을 돌면서 조건 확인하기
    for x in comb:
        if sum(x) == s:
            count += 1
print(count)
