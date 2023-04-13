# 수업 최대한 많이 신청하기 문제와 유사
def solution(routes):
    answer = 1
    
    routes.sort(key=lambda x: x[0])
    start = routes[0][0]
    finish = routes[0][1]
    
    for i in range(1, len(routes)):
        if routes[i][0] <= finish:
            if routes[i][1] < finish:
                finish = routes[i][1]
            continue
        else:
            answer += 1
            start = routes[i][0]
            finish = routes[i][1]
    
    return answer
