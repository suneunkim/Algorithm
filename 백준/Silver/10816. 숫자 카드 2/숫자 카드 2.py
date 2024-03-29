from collections import Counter 

_ = int(input())
N = input().split()
_ = int(input())
M = input().split()

answer = []

counter = Counter(N)

for m in M:
    if m in counter:
        answer.append(str(counter[m]))
    else:
        answer.append('0')
        
print(' '.join(answer))
