def solution(participant, completion):
    dict = {}
    answer = ''
    # 참가자 목록에서 이름을 key, 동명이인 대비로 사람 수를 값으로.
    for p in participant:
        if p in dict:
            dict[p] += 1
        else:
            dict[p] = 1
    
    # 완주한 목록을 key로 접근해서 사람 수 줄이기.
    for c in completion:
        if c in dict:
            dict[c] -= 1
    
    for p in participant:
        if dict[p] > 0:
            answer = p
    
    return answer