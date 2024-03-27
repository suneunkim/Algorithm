def solution(n, lost, reserve):
    
    real_lost = set(lost) - set(reserve)
    
    real_reserve = set(reserve) - set(lost)
    
    for student in real_reserve:
        if student - 1 in real_lost:
            real_lost.remove(student - 1)
        elif student + 1 in real_lost:
            real_lost.remove(student + 1)
    
    return n - len(real_lost)

# 가져온 학생이 도난당할 수 있으니 set으로 경우기 겹치는 학생 제외
# 여벌이 있는 학생이 빌려주는 경우 lost 리스트에서 해당 학생 제외
# lost 리스트에 남아있는 학생은 수업을 못들음