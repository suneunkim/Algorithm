N = int(input())
cards = [] 
# appned 하면 cards는 [('BANANA', 2), ('PLUM', 4), ('BANANA', 3)]

for _ in range(N):
    fruit, count = input().split()
    cards.append((fruit, int(count))) # 튜플

fruit_dics = {"STRAWBERRY": 0, "BANANA": 0, "LIME": 0, "PLUM": 0}

for card in cards:
    fruit_dics[card[0]] += card[1]

for count in fruit_dics.values(): # dict_values([0, 5, 0, 4])
    if count == 5:
        print("YES")
        break
else:
    print("NO")