N, M = map(int, input().split())

no_hear = []
no_see = []

# 듣도 못한 사람의 이름 입력받기
for _ in range(N):
    no_hear.append(input())

# 보도 못한 사람의 이름 입력받기
for _ in range(M):
    no_see.append(input())

a = set(no_hear)
b = set(no_see)

answer = list(a & b)

print(len(answer))
for human in sorted(answer):
    print(human)

# 듣도 못한 사람과 보도 못한 사람의 교집합 찾기
# 사전 순 출력