def solution(people, limit):
    answer = 0
    
    people.sort(reverse=True)
    boats = []
    for weight in people:
        if not boats:
            boats.append(weight)
            continue
        
        if boats[-1] + weight <= limit:
            boats.pop()
            answer += 1
        else:
            boats.append(weight)
    
    return answer+len(boats)

# 20 50 80 50

# 80 50 50 20
# 80 70 50 50

# 90 80 50 50 20 10
