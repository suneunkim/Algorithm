def solution(t, p):
    count = 0
    
    for i in range(len(t)-len(p) + 1):
        #print(list(range(len(t)-len(p) + 1)))
        slicing_str = int(t[i:i+len(p)])
        
        if slicing_str <= int(p):
            count += 1
            
    return count

# "12345" -> 123, 234, 345 만들어야 함
# 인덱스로 0번째부터 접근해서 :p 으로 슬라이싱 하기?
# t의 index 0부터 p의 len + index까지 자르기


