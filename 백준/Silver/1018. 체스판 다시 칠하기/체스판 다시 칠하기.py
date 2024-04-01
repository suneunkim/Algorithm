N, M = map(int, input().split())
board = []

# 보드 생성
for _ in range(N):
    row = input()
    board.append(row)

# 최솟값 변수
min_repaint = float('inf') 

for i in range(N - 7):
    for j in range(M - 7):
        # 현재 위치에서 8x8 체스판 생성
        repaint_count = 0
        for x in range(8):
            for y in range(8):
                # (0, 0) 흰색 시작
                if (x + y) % 2 == 0:  
                    if board[i + x][j + y] != 'W':
                        repaint_count += 1
                # (0, 1) 검은색 시작
                else:
                    if board[i + x][j + y] != 'B':
                        repaint_count += 1
        min_repaint = min(min_repaint, repaint_count, 64 - repaint_count)
        
print(min_repaint)
