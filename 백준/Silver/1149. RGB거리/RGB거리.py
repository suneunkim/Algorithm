N = int(input())
cost = []

# 집을 칠하는 비용 입력 받기
for _ in range(N):
    cost.append(list(map(int, input().split())))

# DP 테이블 초기화
dp = [[0] * 3 for _ in range(N)]

# 첫 번째 집의 비용은 그대로
dp[0] = cost[0]

# DP 점화식 적용
for i in range(1, N):
    # 빨간색(R)을 선택할 경우
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    
    # 초록색(G)을 선택할 경우
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    
    # 파란색(B)을 선택할 경우
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

# 마지막 집의 색깔 중 최소 비용을 출력
print(min(dp[N-1]))
