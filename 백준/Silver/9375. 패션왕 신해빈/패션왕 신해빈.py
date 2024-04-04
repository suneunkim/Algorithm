# 1. 이중 for문으로 입력받아서 옷 구성을 함수로 전달
# 2. 옷 구성 = [('hat', 'headgear')]
# 3. 옷 구성의 2번째 값을 dict의 key값으로, 가짓수를 +1씩
# count -> {'headgear': 2, 'eyewear': 1}
# 경우의 수 공식 (a1 + 1)* (b1 + 1) ... - 1

from collections import defaultdict

test_case = int(input())

def count_combi(outfits):
    count = defaultdict(int)
    # 2, 3번
    for o in outfits:
        count[o[1]] += 1

    # 경우의 수 구하는 공식
    result = 1
    for key in count:
        result *= (count[key] + 1)
    return result - 1

for _ in range(test_case):
    n = int(input())
    outfits = []
    for _ in range(n):
        name, category = input().split()
        outfits.append((name, category))
    print(count_combi(outfits))