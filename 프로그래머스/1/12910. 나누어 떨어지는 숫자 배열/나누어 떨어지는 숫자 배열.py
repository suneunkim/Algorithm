def solution(arr, divisor):
    result = []
    
    for num in arr:
        if num % divisor == 0:
            result.append(num)
            
    result.sort()
    
    if len(result) == 0:
        result = [-1]

    return result