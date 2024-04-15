# S -> T 뒤에 A를 추가하기, 뒤에 B를 추가하고 뒤집기 가능
# T -> S 뒤에 A를 제거하기, 앞에 B를 제거하고 뒤집기
# 핵심은 거꾸로 T에서 S로 가기.

S = list(input())
T = list(input())

def dfs(t):
    if t == S:
        print(1)
        exit()
    if len(t) == 0:
        return 0
    if t[-1] == 'A':
        dfs(t[:-1]) # 맨 뒤 A면 지우고 다시 확인
    if t[0] == 'B':
        dfs(t[1:][::-1]) # 맨 앞이 B면 지우고 뒤집기

dfs(T)
print(0)