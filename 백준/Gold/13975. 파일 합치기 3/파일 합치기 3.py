from heapq import *

T = int(input()) # 첫 반복문 조건. 테스트케이스가 여러개니까 T 반복문 안에서!

for _ in range(T):
    K = int(input()) # 챕터 수
    pile_size = list(map(int, input().split()))
    heap = [] # 파일들을 heap에 담아서 최소값 사용하기
    answer = 0 # 파일 크기를 더한 값을 담을 변수
    
    for p in pile_size:
        heappush(heap, p)
    # heap에 전부 담았으니 사용하기.
    while len(heap) > 1: # heap이 비었다면 다 꺼내서 더했다.
        a = heappop(heap)
        b = heappop(heap)
        answer += a + b
        heappush(heap, a + b) # 마지막 2개 더했다면 heap의 len은 1이라 끝.
        
    print(answer)

# 파일 사이즈들을 작은 크기부터 더해가야 함.
# heap에 파일 사이즈를 전부 담고 최소값을 2개씩 꺼내서 사용하기.
