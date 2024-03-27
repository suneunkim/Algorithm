def solution(k, score):
    answer = []
    hall = []
    
    for i in score:
        if len(hall) < k:
            hall.append(i)
        else:
            if i > min(hall):
                hall.remove(min(hall))
                hall.append(i)
        
        answer.append(min(hall))
        
    return answer

# 명예의 전당에 k번째까지는 전부 넣고 이후는 비교
# 명예의 전당에 있는 가장 낮은 점수와 비교하기
# sort로 정렬하면 맨 앞이 