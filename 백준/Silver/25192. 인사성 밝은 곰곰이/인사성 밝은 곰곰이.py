n = int(input())

count = 0
gom = set()

for _ in range(n):
    i = input()
    if i == 'ENTER': # 초기화하고 카운트 별개로 세기
        gom.clear()
    else:
        if i not in gom:
            count += 1
            gom.add(i)
print(count)

# ENTER 만날때 마다 set를 만들고 합치려했는데 clear가 더 나은듯