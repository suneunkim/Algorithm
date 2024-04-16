# 센서의 좌표를 정렬하고 거리 차이를 계산하기

N = int(input()) # 센서
K = int(input()) # 집중국
sensors = list(map(int, input().split()))

sensors.sort() # [1, 3, 6, 6, 7, 9]

distance = []
for i in range(1, N):
    distance.append(sensors[i] - sensors[i-1])
    
distance.sort(reverse=True) # [3, 2, 2, 1, 0]

# 가장 긴 센서 사이의 거리부터 K-1개의 거리를 제거
for _ in range(K-1):
    if distance:
        distance.pop(0)

print(sum(distance))