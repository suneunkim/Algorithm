def solution(s):
    split_s = s.split(' ') # ['1', '2', '3', '4']
    number_s = [int(x) for x in split_s] # [1, 2, 3, 4]
    
    max_s = str(max(number_s))
    min_s = str(min(number_s))
    
    answer = min_s + " " + max_s
    
    return answer

# 리스트로 만들고 타입을 숫자로 바꿔서 max와 min 사용
# 다시 str로 글자로 만들어서 사이에 공백 더하기