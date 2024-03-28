A, B = map(str, input().split()) # 슬라이싱 사용하려면 str

NewA, NewB = A[::-1], B[::-1] # 문자열 뒤집기

answer = max(int(NewA), int(NewB))

print(answer)