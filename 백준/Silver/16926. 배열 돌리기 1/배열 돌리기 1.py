from collections import deque

def rotate_matrix(matrix, R):
    N, M = len(matrix), len(matrix[0]) # 행의 수와 열의 수
    answer = [[0] * M for _ in range(N)]
    deq = deque()

    loops = min(N, M) // 2 # 회전 수행 할 테두리의 수
    
    for i in range(loops):
        deq.clear()
        deq.extend(matrix[i][i:M-i])
        deq.extend([row[M-i-1] for row in matrix[i+1:N-i-1]])
        deq.extend(matrix[N-i-1][i:M-i][::-1])
        deq.extend([row[i] for row in matrix[i+1:N-i-1]][::-1])

        deq.rotate(-R)

        for j in range(i, M-i):                 # 위쪽
            answer[i][j] = deq.popleft()
        for j in range(i+1, N-i-1):             # 오른쪽
            answer[j][M-i-1] = deq.popleft()
        for j in range(M-i-1, i-1, -1):         # 아래쪽
            answer[N-i-1][j] = deq.popleft()  
        for j in range(N-i-2, i, -1):           # 왼쪽
            answer[j][i] = deq.popleft()    

    return answer

N, M, R = map(int, input().split())

matrix = []
for _ in range(N):
    matrix.append(input().split())

rotated_matrix = rotate_matrix(matrix, R)

for line in rotated_matrix:
    print(" ".join(line))
