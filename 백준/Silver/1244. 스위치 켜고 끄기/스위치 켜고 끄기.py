N = int(input()) # 8 # 20개 이상이면 한 줄에 20개씩

switch = list(map(int, input().split())) 
# [0, 1, 0, 1, 0, 0, 0, 1]

students = int(input()) # 학생 수

def switch_change(i):
    switch[i] = 1 if switch[i] == 0 else 0

for _ in range(students):
    student = list(map(int, input().split()))
    
    if student[0] == 1: # 남학생
        num = student[1]
        for i in range(1, N + 1):
            if i % num == 0:
                switch_change(i-1)
    
    else: # 여학생
        i = student[1] - 1 # 스위치 번호를 인덱스로
        switch_change(i)
        count = 1
        while i - count >= 0 and i + count < N: # 인덱스 0미만 N 초과 안됨
            x, y = switch[i - count], switch[i + count]
            if x == y:
                switch_change(i - count)
                switch_change(i + count)
                count += 1
            else:
                break

for i in range(0, N, 20): # 1부터 N까지, 간격 20
    print(*switch[i:i+20])