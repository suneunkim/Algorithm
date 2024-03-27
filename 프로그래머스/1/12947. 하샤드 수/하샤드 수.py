

def solution(x):
    nums = [int(number) for number in str(x)]
    
    total = sum(nums)
    return x % total == 0