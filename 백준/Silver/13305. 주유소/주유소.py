# 도시 수 만큼 주유소가 있고 마지막 주유소는 도착지이므로 제외
# 따라서 반복문의 범위 n-1에서 기름값과 거리를 곱하기
# 최소 가격을 저장하는 변수로 가격 낮아지면 값을 갱신하기

N = int(input())
km = list(map(int, input().split()))
prices = list(map(int, input().split()))

min_price = prices[0] # 최소 주유 비용을 저장할 변수 초기화
total = 0

for i in range(N-1):
    min_price = min(min_price, prices[i])
    total += min_price * km[i]
    
print(total)