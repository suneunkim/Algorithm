def solution(price, money, count):
    total = 0
    
    for num in range(1, count+1):
        total += price * num
    if money - total < 0:
        return total - money
    else:
        return 0