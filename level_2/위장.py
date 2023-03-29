def solution(clothes):
    answer = 0
    
    closet = dict()
    for name, item in clothes:
        closet[item] = closet.get(item, 0) + 1
    
    Sum = 1
    for key in closet.keys():
        Sum *= (closet[key]+1)
    answer = Sum - 1
    
    return answer