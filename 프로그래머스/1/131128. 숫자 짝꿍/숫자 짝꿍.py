def solution(X, Y):
    answer = ''
    
    common = set(X) & set(Y)
    if not common:
        return "-1"
    
    for digit in sorted(common, reverse=True):
        count = min(X.count(digit), Y.count(digit))
        answer += digit * count
        
    if answer[0] == "0":
        return "0"
        
    return answer

# x와 y의 교집합 찾기
# 내림차순으로 가장 큰 숫자부터 만들기 // str로 문자열 취급 더하기
# set으로 찾으니 sorted 하니 중복되는 숫자가 제외됨
# count로 중복되는 글자 몇개인지 확인하기