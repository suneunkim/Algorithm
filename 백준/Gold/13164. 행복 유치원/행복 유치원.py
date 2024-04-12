# 원생들의 키 차이대로 diff를 만드는 것이 핵심
# diff를 정렬하고 K-1개만큼 앞에서부터 더하기
# k-1개만큼 작은 키 차이를 선택

N, K = map(int, input().split())
heights = list(map(int, input().split()))

# 키 차이를 계산하고 정렬
diffs = [heights[i+1] - heights[i] for i in range(N-1)]
diffs.sort()

cost = diffs[:N-K]

print(sum(cost))