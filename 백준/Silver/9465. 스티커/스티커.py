import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0] * n for _ in range(2)]

    # 첫번째 값 초기값으로로
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]
    
    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue
    # 첫번째 열 계산
    dp[0][1] = stickers[0][1] + dp[1][0]
    dp[1][1] = stickers[1][1] + dp[0][0]
    
    if n == 2:
        print(max(dp[0][1], dp[1][1]))
        continue
        
    # 점화식
    for i in range(2, n):
        dp[0][i] = stickers[0][i] + max(dp[1][i-1], dp[1][i-2])
        dp[1][i] = stickers[1][i] + max(dp[0][i-1], dp[0][i-2])
    # 최대 점수로 출력하기
    print(max(dp[0][-1], dp[1][-1]))