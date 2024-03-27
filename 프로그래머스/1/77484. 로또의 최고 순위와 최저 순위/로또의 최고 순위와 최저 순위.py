def solution(lottos, win_nums):
    
    min_rank = 7 - (len(set(lottos) & set(win_nums)))
    # 2개 일치, 7 - 2 -> 5등
    max_rank = 7 - lottos.count(0) + (min_rank -7)
    
    if min_rank == 7:
        min_rank = 6
    if max_rank == 7:
        max_rank = 6
        
    return [max_rank, min_rank]

# lottos에 0이 몇개인지 확인하고 -> 추가 당첨
# win과 겹치는 숫자 몇개인지 확인하기 -> 기본 당첨 개수
# 당첨 개수로 순위 따지는 것은 7 - 당첨 개수 = 순위

# first_count = len(set_lottos.intersection(set_win))
# 더 간단히 set(ex1 & ex2) 가능.