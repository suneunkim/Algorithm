def solution(s):
    words = s.split(' ')
    answer = []
    for word in words:
        converted_word = ''
        for index in range(len(word)):
            if index % 2 == 0:
                converted_word += word[index].upper()
            else:
                converted_word += word[index].lower()
        answer.append(converted_word)
    return ' '.join(answer)

#range -> enumerate 변경해볼것
# split() , split(' ')

# try -> 3글자, 인덱스는 0,1,2이다.
# t는 첫번째 글자이며 인덱스는 0 -> 대문자로!
# 대소문자 변환시키고 리스트에 넣어서 join으로 공백 넣기
# join은 ''.join(리스트)