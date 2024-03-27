def solution(a, b):
    i = 0
    answer = []
    while i < len(a):
        answer.append(a[i] * b[i])
        i += 1
        
    return sum(answer)