# 큰자리수 길이로 만들어서 정렬
def solution(numbers):
    
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    return str(int("".join(numbers)))