def solution(array, commands):
    answer = []
    for index in range(len(commands)):
        i, j, k = commands[index]
        result = sorted(array[i-1:j])
        answer.append(result[k-1])
        
    return answer