# 길이가 짧은 순, 길이가 같다면 사전 순, 중복 단어 제거
# 사전에 단어의 길이를 key로 단어 추가하기
# 사전의 key 값으로 정렬하기

from collections import defaultdict

n = int(input())
len_word = defaultdict(set)

for _ in range(n):
    word = input()
    len_word[len(word)].add(word)

keys = list(len_word.keys()) # [3, 1, 4, 8, 2, 6, 5] -> word 글자수
keys.sort()

for key in keys:
    words = list(len_word[key]) # 글자수에 맞는 단어들 리스트로
    words.sort()
    for word in words:
        print(word)