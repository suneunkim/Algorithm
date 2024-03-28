from collections import Counter

word = input().upper()

counter = Counter(word) # Counter({'Z': 3, 'A': 1, 'B': 1})

max_count = max(counter.values()) # counter_values([3, 1, 1])

most_char = [char for char, count in counter.items() if count == max_count]

if len(most_char) == 1:
    print(most_char[0])
else:
    print("?")

# Counter -> 컨테이너에 동일한 값의 자료가 몇 개인지를 파악함
# 가장 많이 사용된 알파벳 수를 기준으로 most_char 리스트에 넣기