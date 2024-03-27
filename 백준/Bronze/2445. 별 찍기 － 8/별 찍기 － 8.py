N = int(input())

# 위쪽 삼각형 출력
for i in range(1, N + 1):
    stars = '*' * i  # 별의 개수는 줄 번호와 같음
    spaces = ' ' * (2 * N - 2 * i)  # 공백의 개수는 총 열 수 - 별의 개수
    print(stars + spaces + stars)

# 아래쪽 삼각형 출력
for i in range(N - 1, 0, -1):
    stars = '*' * i  # 별의 개수는 줄 번호와 같음
    spaces = ' ' * (2 * N - 2 * i)  # 공백의 개수는 총 열 수 - 별의 개수
    print(stars + spaces + stars)