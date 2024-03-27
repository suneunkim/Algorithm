def solution(num):
    count = 0
    # num이 1이 될 때 까지 짝수인지 홀수인지에 따라 다른 작업
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
            
        count += 1

        if count == 500:
            return -1
            
    return count