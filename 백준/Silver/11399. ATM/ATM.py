# 전체 시간을 줄이려면 오름차순 정렬 상태에서 인출

n = int(input())

peoples = list(map(int, input().split()))

peoples.sort() # 오름차순으로 정렬
answer = 0
for i in range(1, n+1):
    answer += sum(peoples[0:i])
print(answer)

# peoples[0:1] -> 앞에서부터 하나만
# peoples[0:2] -> 앞에서부터 두개