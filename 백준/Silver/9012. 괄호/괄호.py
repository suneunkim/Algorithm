# 개념 및 접근법 작성
# 괄호가 짝이 맞아야함 +,-나 문자열 입력, 삭제
# +,- 이용 시 count = 0 확인을 마지막에하면 '()' 모양이 안맞는 경우있음
# 그렇기에 count가 0보다 작아지는 순간 ')' 이 먼저 온거니 잘못된 모양이 됨

T = int(input())

for _ in range(T):
    count = 0
    p = input() # ())(()) 
    
    for c in p: # (
        if c == '(':
            count += 1
        else:
            count -= 1
            if count < 0:
                print("NO")
                break
    else: # for-else 구문. break 안걸린 경우를 위함. 안쓰면 의도와 다른 출력
        print("YES" if count == 0 else "NO")