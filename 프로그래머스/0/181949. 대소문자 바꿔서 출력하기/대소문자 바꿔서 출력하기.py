str = input()
answer = ''

# 입력받은 문자열의 각 문자를 순회
for x in str:
    # 각 문자가 소문자인지 확인
    if(x.islower()):
        # 소문자라면 대문자로 변환
        answer += x.upper()
    else:
        # 대문자라면 소문자로 변환
        answer += x.lower()
        
print(answer)

