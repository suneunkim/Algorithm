from collections import Counter

name = input()
count = 0
odd_char = ''

counter = Counter(name)

for char, freq in counter.items():
    if freq % 2 == 1:
        count += 1
        odd_char = char
        if count > 1:
            print("I'm Sorry Hansoo")
            exit()

half_answer = ''

for char, freq in sorted(counter.most_common()):
    half_answer += char * (freq // 2)

if odd_char:
    answer = half_answer + odd_char + half_answer[::-1]
else:
    answer = half_answer + half_answer[::-1]
    
print(answer)

# 홀수 빈도수의 문자열이 2개 이상이면 회문이 안됨
# 빈도수가 높은 문자부터 추가
# odd_char 홀수 빈도수의 문자열 가운데 넣기
# Counter.most_common() -> 빈도가 높은 요소 순서의 튜플