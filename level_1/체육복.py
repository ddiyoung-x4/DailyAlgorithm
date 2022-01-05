def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    rmv_list = []
    for std in lost:
        if std in reserve:
            rmv_list.append(std)
    for data in rmv_list:
        lost.remove(data)
        reserve.remove(data)
    for std in lost:
        if std-1 in reserve:
            reserve.remove(std-1)
        elif std+1 in reserve:
            reserve.remove(std+1)
        else:
            answer += 1
            
    return n - answer