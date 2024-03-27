def solution(today, terms, privacies):
    answer = []
    terms_dic = {t[0]: int(t[2:]) * 28 for t in terms}
    # {'A': 168, 'B': 336, 'C': 84}
    
    today = list(map(int, today.split('.')))
    # 2022.05.19 -> [2022, 5, 19]
    today = today[0] * 12 * 28 + today[1] * 28 + today[2]
    # 679551
    
    for index, privacy in enumerate(privacies):
        privacy_date = privacy.split(' ')[0]
        privacy_term = privacy.split(' ')[1]
        # 수집일 날짜를 일수로 변환
        privacy_date = list(map(int, privacy_date.split('.')))
        privacy_date = privacy_date[0] * 12 * 28 + privacy_date[1] * 28 + privacy_date[2]
        # 수집일에 유효기간 일수 더해서 오늘의 일수보다 작다면 유효기간 지남
        if privacy_date + terms_dic[privacy_term] <= today:
            answer.append(index + 1)
    return answer
        

# 약관의 유효기간(월) 일수로 변환한 dic 만들기
# today와 privacies의 date도 일수로 변환해서 비교하기