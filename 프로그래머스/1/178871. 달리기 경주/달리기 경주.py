def solution(players, callings):
    rank = {player: i for i, player in enumerate(players, start=1)}
    # {'mumu': 1, 'soe': 2, 'poe': 3, 'kai': 4, 'mine': 5}
    
    for who in callings:
        call_rank = rank[who] # 호명된 kai 선수의 등수인 4
        rank[who] = call_rank - 1 # 'kai': 3 으로 변경
        
# players[0] 은 "mumu" -> rank["mumu"]라면 값이 1
# players 에서 kai의 인덱스는 3
# call_rank - 2 를 해야 players에서 kai보다 앞선 poe임.
# poe의 원래 등수 3에 +1 해서 4로 변경
        rank[players[call_rank - 2]] += 1
# 호명된 선수의 앞사람과 호명된 선수를 players에서 위치 변경
        players[call_rank-1], players[call_rank-2] = players[call_rank-2], players[call_rank-1]
    
    return players

# dic으로 선수의 이름과 등수를 기록
# 불린 선수의 이름을 dic에서 등수를 변경