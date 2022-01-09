def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        a = numbers[i]
        for j in range(i+1, len(numbers)):
            res = a + numbers[j]
            answer.append(res)
            
    return sorted(list(set(answer)))