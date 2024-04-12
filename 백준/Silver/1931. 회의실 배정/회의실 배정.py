# 종료 시간 정렬 -> 시작 시간 정렬로 빨리 끝나는 회의를 우선으로

# 입력받기
N = int(input())
time = [list(map(int, input().split())) for _ in range(N)]

# 시간을 종료 시간을 우선으로 정렬하기
time.sort(key=lambda x: (x[1], x[0]))

# time을 돌면서 끝나는 시간 기록 -> 다음 회의 시작과 비교하고 count +1
last = 0 # 회의 끝난 시간 기록용
count = 0 # 회의 수

for t in time:
    start, end = t
    if start >= last:
        last = end
        count += 1
        
print(count)