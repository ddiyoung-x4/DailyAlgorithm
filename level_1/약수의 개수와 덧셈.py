import math

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        root = math.sqrt(i)
        if root - int(root) == 0:
            answer -= i
        else:
            answer += i
            
    return answer