nums = list(map(int, input().split()))  # 주사위의 눈을 리스트로 입력받음

# 주사위 눈의 개수를 세는 리스트 초기화
count_nums = [0] * 7  # 0부터 6까지의 인덱스를 갖는 리스트 생성

# 각 눈의 개수를 세기
for num in nums:
    count_nums[num] += 1

# 3개의 눈이 같은 경우
if count_nums.count(3) == 1:
    print(10000 + count_nums.index(3) * 1000)
# 2개의 눈이 같은 경우
elif count_nums.count(2) == 1:
    print(1000 + count_nums.index(2) * 100)
# 모든 눈이 다를 경우
else:
    print(max(nums) * 100)