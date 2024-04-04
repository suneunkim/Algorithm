from heapq import *
from sys import stdin
input = stdin.readline

n = int(input().strip())

entry = {}
out = {}

# 들어온 순서로 dict
for i in range(n):
    entry[i] = input().strip()

for i in range(n):
    a = input().strip()
    out[a] = i

count = 0
for i in range(1, n):
    for j in range(0, i):
        if out[entry[j]] > out[entry[i]]:
            count += 1
            break
print(count)
            
#{0: 'ZG431SN', 1: 'ZG5080K', 2: 'ST123D', 3: 'ZG206A'}
#{'ZG206A': 0, 'ZG431SN': 1, 'ZG5080K': 2, 'ST123D': 3}