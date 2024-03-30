a = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = 0

n, b = input().split()

n = n[::-1]

for i, n in enumerate(n):
    result += (int(b)**i)*(a.index(n))

print(result)