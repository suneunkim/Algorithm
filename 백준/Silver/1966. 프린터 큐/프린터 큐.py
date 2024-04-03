# N은 문서의 개수. M은 몇 번째로 인쇄되었는지 궁금한 문서의 위치

case = int(input()) # 3

for _ in range(case):
    N, M = map(int, input().split()) # 4 2
    docs = list(map(int, input().split())) # 1 2 3 4

    result = 1 # 몇 번째로 출력되는지 알려줄 결과
    while docs: # docs가 남아 있는 동안 반복
        if docs[0] < max(docs): # 맨 앞에 있는 문서가 중요도가 가장 높지 않으면
            docs.append(docs.pop(0)) # 맨 앞이 중요도 가장 커야해서 뒤로 보냄
            
        else: # 맨 앞에 문서가 제일 중요도가 가장 높은 경우
            if M == 0:
                break

            docs.pop(0) # 맨 앞 출력
            result += 1

        M = M - 1 if M > 0 else len(docs) - 1
        # 목표 문서가 맨 앞이면 인쇄된 문서 수 감소
        # 목표 문서가 맨 앞이 아니라면 docs 길이 줄이기
    
    print(result)