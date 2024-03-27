import datetime
def solution(a, b):
    
    year = 2016
    month = a
    day = b
    
    date = datetime.date(year,month,day)
    
    weekday = date.strftime("%A")
    
    print(weekday)
    
    answer = weekday[:3].upper()
    
    return answer