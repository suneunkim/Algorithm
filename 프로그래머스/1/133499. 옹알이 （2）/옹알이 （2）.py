def solution(babbling):
    count = 0
    can_speak = ["aya", "ye", "woo", "ma"]
    ex_word = "yemawoo"
    
    for word in babbling:
        for can in can_speak:
            if can * 2 not in word:
                word = word.replace(can, ' ')
        if word.isspace():
            count += 1
            
    return count

# 발음이 2번 연속되는 경우 제외하기
# "yemawoo".replace("aya", ' ') -> "yemawoo" 그대로
# "yemawoo".replace("ye", ' ') -> "mawoo" ye는 공백으로 지워짐
# isspace() 는 문자열이 모두 공백이어야 True

# 처음에는 for in 으로 can_speak를 인덱스로 접근해서 startswidh 시도
# 순서대로 안나오면 반복문을 다시 돌아야함..