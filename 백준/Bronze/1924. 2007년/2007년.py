month, day = map(int, (input().split()))

days_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
weekdays = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

total_days = sum(days_in_month[:month]) + day

days_of_week = (total_days - 1) % 7

print(weekdays[days_of_week])

# days_in_month[:3] -> 0, 31, 28
# 3월 14일 -> 0 + 31(1월) + 28(2월) + 14(3월)
# day가 1이면 weekdays에서 "MON"이 나와야하니 1를 빼준다