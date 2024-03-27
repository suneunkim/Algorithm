def solution(s, n):
    answer = ''
    for char in s:
        if char.isalpha():
            start = ord("A") if char.isupper() else ord("a")
            answer += chr((ord(char) - start + n) % 26 + start)
        else:
            answer += char
    return answer
            
            

# 65번~90번 A ~ Z 97번~ 122번 a ~ z
# chr(아스키코드) ord(문자) 
# isalpha()로 알파벳인지 확인하고 알파벳이 아니면(공백)
# 해당 문자를 그대로 유지함