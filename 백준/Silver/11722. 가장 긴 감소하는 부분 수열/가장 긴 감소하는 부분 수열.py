N = int(input())
A = list(map(int, input().split()))

# dp 배열 초기화
dp = [1] * N

# 각 원소에 대해 가장 긴 감소하는 부분 수열의 길이 계산
for i in range(N):
    for j in range(i):
        if A[j] > A[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# dp 배열 중 최대값 출력
print(max(dp))
