def solution(numbers):
    answer = 0
    check = [0 for _ in range(10)]
    
    for number in numbers:
        check[number] = 1
    for i, data in enumerate(check):
        if data == 0:
            answer += i
    return answer

# def solution(numbers):
#     return 45 - sum(numbers)