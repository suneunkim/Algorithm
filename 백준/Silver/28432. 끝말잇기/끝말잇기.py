N = int(input())
record = []

for n in range(N):
    record.append(input())
    
M = int(input())
candidates = []

for m in range(M):
    candidates.append(input())

if "?" in record:
    i = record.index("?") # "?"가 맨 처음일 경우
    if i == 0:
        first_char = ""
    else:
        first_char = record[i - 1][-1] #앞단어 마지막 글자
    
    if i == len(record) - 1: # "?"가 맨 마지막일 경우
        last_char = ""
    else:
        last_char = record[i + 1][0] #뒷단어 첫 글자

    for word in candidates:
        if word not in record:
            if (not first_char or word[0] == first_char) and (not last_char or word[-1] == last_char):
                print(word)

# "?"를 index()로 위치 확인, 앞과 뒤 글자 확인하기
# record에 not in 조건으로 중복 확인하기