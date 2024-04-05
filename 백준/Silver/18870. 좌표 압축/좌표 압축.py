# 문제 이해하기! x(i)보다 작은 원소가 몇개인지 구하기
# [2,4,-10,4,-9] -> 2는 2보다 작은 원소 2개.
# 좌표를 크기 순으로 정렬
# list.index(i) -> O(N) {dict[요소]: index} O(1)

import sys

input = sys.stdin.readline

n = int(input())

nums = list(map(int, input().split())) # 입력받기
arr = sorted(set(nums)) # set으로 중복 없애고 정렬

# [-10, -9, 2, 4]

nums_dict = {arr[i]: i for i in range(len(arr))}
# {-10: 0, -9: 1, 2: 2, 4: 3}
# 오름차순 정렬로 i는 본인보다 작은 수가 있는지의 값이 됨

for i in nums:
    print(nums_dict[i], end=" ")

# 한줄에 표시되길 원하면 print(i, end=" ") 사용