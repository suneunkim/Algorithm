N = input()
new_score = []
scores = list(map(int,input().split())) # [40, 80, 60]

M = max(scores)

for score in scores:
    new_score.append(score / M * 100)

answer = sum(new_score) / len(new_score)
    
print(answer)