def solution(s):
    answer = [0, 0]
    while s != "1":
        l = s.count("1")
        answer[1] += len(s)-l 
        s = bin(l)[2:]
        answer[0] += 1
    
    return answer