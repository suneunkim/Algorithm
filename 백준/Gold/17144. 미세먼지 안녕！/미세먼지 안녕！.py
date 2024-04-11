import sys
input = sys.stdin.readline

# [0] 입력값 받기
R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

# [1] 청정기 위치 저장
for i in range(R):
    if arr[i][0] == -1:
        i1, i2 = i, i+1
        arr[i1][0] = arr[i2][0] = 0 # 0으로 초기화
        break
        
# T초동안 확산과 정화
for _ in range(T):
    # [2] 먼지 확산 (arr 복사해서 확산하고 대입하기)
    arr_t = [x[:] for x in arr]
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 4: # 5로 나눈 몫이 퍼지기 때문
                t = arr[i][j] // 5 # 4방향으로 퍼질 먼지 양
                for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
                    # 상하좌우 4번
                    ni, nj = i+di, j+dj # 현재 위치에서 한칸씩
                    # 지정된 크기 내에서, 청정기 위치 아니라면
                    if 0<=ni<R and 0<=nj<C and (ni,nj) != (i1,0) and (ni,nj) != (i2,0):
                        arr_t[i][j] -= t
                        arr_t[ni][nj] += t
    arr = arr_t

    # [3] 순환
    # 상단 공기순환
    for i in range(i1 - 1, 0, -1):  # 위쪽으로 이동하는 공기순환
        arr[i][0] = arr[i - 1][0]
    for j in range(C - 1):  # 오른쪽으로 이동하는 공기순환
        arr[0][j] = arr[0][j + 1]
    for i in range(i1):  # 아래쪽으로 이동하는 공기순환
        arr[i][-1] = arr[i + 1][-1]
    for j in range(C - 1, 0, -1):  # 왼쪽으로 이동하는 공기순환
        arr[i1][j] = arr[i1][j - 1]
    arr[i1][1] = 0  # 공기순환 후 공기청정기 옆 미세먼지 0으로 초기화

    # 하단 공기순환
    for i in range(i2 + 1, R - 1):  # 아래쪽으로 이동하는 공기순환
        arr[i][0] = arr[i + 1][0]
    for j in range(C - 1):  # 오른쪽으로 이동하는 공기순환
        arr[-1][j] = arr[-1][j + 1]
    for i in range(R - 1, i2, -1):  # 위쪽으로 이동하는 공기순환
        arr[i][-1] = arr[i - 1][-1]
    for j in range(C - 1, 0, -1):  # 왼쪽으로 이동하는 공기순환
        arr[i2][j] = arr[i2][j - 1]
    arr[i2][1] = 0  # 공기순환 후 공기청정기 옆 미세먼지 0으로 초기화

# map(sum(arr)) -> 각 행의 합계
ans = sum(map(sum, arr))
print(ans)


