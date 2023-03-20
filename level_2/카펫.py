import math

def solution(brown, yellow):
    answer = []
    
    div_list = getDivisor(yellow)
    for i in range(len(div_list)//2+1):
        x, y = div_list[i], div_list[-(i+1)]
        need_brown = 2*x + 2*y + 4
        if brown == need_brown:
            answer = [x+2, y+2]
    
    return sorted(answer, reverse=True)

def getDivisor(num):
    div_list = []
    
    for i in range(1, int(math.sqrt(num))+1):
        if num % i == 0:
            div_list.append(i)
            if (i**2) != num:
                div_list.append(num // i)
    return sorted(div_list)