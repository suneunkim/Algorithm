T = int(input()) # 예시 2

for _ in range(T): # range 0, 1
    R, S = input().split() # 예시 3과 ABC
    answer = ''
    
    for char in S:
        answer += char * int(R)
    print(answer)

