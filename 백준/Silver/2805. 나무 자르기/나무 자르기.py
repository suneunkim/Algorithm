# 절단기의 높이의 최대값 구하기.
# 나무 중간 높이로 자르고 가져가는 길이의 합
# tree의 최대값을 이진탐색 범위 right 값으로
# 추가사항 나무 높이를 Counter로 저장하면 리스트보다 훨씬 빠르다

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
tree = list(map(int, input().split()))

start = 1
end = max(tree)

while start <= end:
    mid = (start + end) //2
    sum = 0 # 자른 나무들의 길이

    for t in tree: # 나무들을 중간값으로 자르기
        if t > mid:
            sum += t - mid

    if sum < m: # 자른 길이의 합계가 목표보다 작음
        end = mid - 1 # 더 잘라야 하니 높이 낮추기
    else:
        start = mid + 1
        
print(end)