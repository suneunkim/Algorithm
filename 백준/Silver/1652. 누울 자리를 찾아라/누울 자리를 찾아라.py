N = int(input())
room = []

for _ in range(N):
    room.append(input())

# print(room)
# ['....X', '..XX.', '.....', '.XX..', 'X....']

count = [0, 0] # 가로 공간, 세로 공간

for row in room:
    empty = 0 # 연속된 빈 공간
    for cell in row:
        if cell == '.': # 빈 공간
            empty += 1
        else: # 짐
            if empty >= 2: # 빈 공간 2칸 이상이면 가로 눕기 +1
                count[0] += 1
            empty = 0 # 짐때문에 연속된 빈 공간 없으니 초기화
    if empty >= 2:
        count[0] += 1

for j in range(N):
    empty = 0
    for i in range(N):
        if room[i][j] == '.': # room[i]가 변동, 줄 바뀌어서 검사
            empty += 1
        else:
            if empty >= 2:
                count[1] += 1
            empty = 0
    if empty >= 2:
        count[1] += 1 # 짐 없이 empty만 오르면 count 올려줘야함

print(*count)