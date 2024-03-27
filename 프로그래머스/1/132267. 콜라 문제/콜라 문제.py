def solution(a, b, n):
    total = 0
    
    while n >= a:
        remain_bottle = n % a
        n = (n // a) * b
        total += n
        n += remain_bottle
        
    return total
        
    
# 보유한 빈 병 n개가 마트에서 받는 빈 병 a 보다 같거나 클 때
# 나머지가 있으면 나중에 다시 n에 더해주기
# 돌려받은 개수를 n으로 바꿔주기