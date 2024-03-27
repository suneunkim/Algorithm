def solution(n):
    pattern = "수박" * (n//2)
    if n % 2 != 0:
        pattern += "수"
    return pattern
        