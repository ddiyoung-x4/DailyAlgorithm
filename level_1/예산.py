def solution(d, budget):
    answer = 0
    d.sort()
    s = 0
    for i in range(len(d)):
        s += d[i]
        if s > budget:
            break
        answer += 1
    return answer